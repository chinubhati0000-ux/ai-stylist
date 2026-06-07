import cv2
import numpy as np
from sklearn.cluster import KMeans

FITZPATRICK = [
    (55,  "Very Fair"),
    (41,  "Fair"),
    (28,  "Intermediate"),
    (10,  "Tan"),
    (-30, "Brown"),
    (-99, "Dark"),
]

COLOR_PALETTES = {
    "Warm":    ["Coral", "Mustard", "Olive", "Peach", "Terracotta", "Warm Red", "Camel", "Gold"],
    "Cool":    ["Lavender", "Silver", "Navy", "Emerald", "Rose", "Icy Pink", "Cobalt", "Mauve"],
    "Neutral": ["Camel", "Ivory", "Teal", "Burgundy", "Forest Green", "Dusty Rose", "Jade", "Blush"],
}

AVOID_COLORS = {
    "Warm":    ["Stark White", "Cool Grey", "Icy Blue", "Black"],
    "Cool":    ["Orange", "Mustard", "Warm Brown", "Yellow"],
    "Neutral": ["Very few restrictions"],
}

OUTFIT_TIPS = {
    "Warm":    "Go for earth tones, warm neutrals, and rich jewel tones. Avoid stark white — try off-white or cream instead.",
    "Cool":    "Go for jewel tones, pastels, and cool neutrals. Silver jewelry suits you better than gold.",
    "Neutral": "You can wear almost any color. Both gold and silver jewelry work well for you.",
}

def get_skin_mask(img):
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    mask1 = cv2.inRange(ycrcb, (0, 133, 77), (255, 173, 127))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask2 = cv2.inRange(hsv, (0, 15, 50), (25, 200, 255))
    mask = cv2.bitwise_or(mask1, mask2)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)
    return mask

def detect_skin_tone(image_path: str) -> dict:
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not read image")

    img = cv2.resize(img, (400, 400))
    mask = get_skin_mask(img)
    skin_pixels_bgr = img[mask > 0]

    if len(skin_pixels_bgr) < 100:
        raise ValueError("Not enough skin detected — use a clearer front-facing photo")

    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    skin_pixels_lab = lab[mask > 0]

    n_clusters = min(4, len(skin_pixels_lab) // 50)
    n_clusters = max(2, n_clusters)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(skin_pixels_lab)

    counts = np.bincount(kmeans.labels_)
    dominant_idx = counts.argmax()
    dominant = kmeans.cluster_centers_[dominant_idx]

    L_raw = float(dominant[0])
    a_raw = float(dominant[1])
    b_raw = float(dominant[2])

    # Convert OpenCV LAB (0-255) to standard LAB range
    L_std = L_raw * 100.0 / 255.0
    a_std = a_raw - 128.0
    b_std = b_raw - 128.0

    # ITA angle using standard LAB values
    ITA = float(np.degrees(np.arctan2((L_std - 50.0), (b_std + 1e-6))))

    # Fitzpatrick scale from ITA
    tone_label = "Dark"
    for threshold, label in FITZPATRICK:
        if ITA > threshold:
            tone_label = label
            break

    # Undertone from b* channel
    if b_std > 5:
        undertone = "Warm"
    elif b_std < 0:
        undertone = "Cool"
    else:
        undertone = "Neutral"

    return {
        "tone_label": tone_label,
        "undertone": undertone,
        "ITA_angle": round(ITA, 2),
        "LAB_values": {
            "L": round(L_std, 1),
            "a": round(a_std, 1),
            "b": round(b_std, 1)
        },
        "best_colors": COLOR_PALETTES[undertone],
        "avoid_colors": AVOID_COLORS[undertone],
        "outfit_tip": OUTFIT_TIPS[undertone],
        "skin_pixels_found": int(len(skin_pixels_lab)),
    }