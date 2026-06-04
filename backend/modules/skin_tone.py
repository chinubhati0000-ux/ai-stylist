import cv2
import numpy as np
from sklearn.cluster import KMeans

# Fitzpatrick scale thresholds
FITZPATRICK = [
    (55,  "Very Fair"),
    (41,  "Fair"),
    (28,  "Intermediate"),
    (10,  "Tan"),
    (-30, "Brown"),
    (-99, "Dark"),
]

# Color palettes based on undertone
COLOR_PALETTES = {
    "Warm":    ["Coral", "Mustard", "Olive", "Peach", "Terracotta", "Warm Red", "Camel", "Gold"],
    "Cool":    ["Lavender", "Silver", "Navy", "Emerald", "Rose", "Icy Pink", "Cobalt", "Mauve"],
    "Neutral": ["Camel", "Ivory", "Teal", "Burgundy", "Forest Green", "Dusty Rose", "Jade", "Blush"],
}

AVOID_COLORS = {
    "Warm":    ["Stark White", "Cool Grey", "Icy Blue", "Black"],
    "Cool":    ["Orange", "Mustard", "Warm Brown", "Yellow"],
    "Neutral": ["Very few restrictions - most colors work"],
}

OUTFIT_TIPS = {
    "Warm":    "Go for earth tones, warm neutrals, and rich jewel tones. Avoid stark white — try off-white or cream instead.",
    "Cool":    "Go for jewel tones, pastels, and cool neutrals. Silver jewelry suits you better than gold.",
    "Neutral": "You can wear almost any color. Both gold and silver jewelry work well for you.",
}

def detect_skin_tone(image_path: str) -> dict:
    # Read image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not read image — check the file path")

    # Resize for faster processing
    img_resized = cv2.resize(img, (256, 256))

    # --- Step 1: Create skin mask using YCrCb color space ---
    ycrcb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2YCrCb)
    mask = cv2.inRange(ycrcb, (0, 133, 77), (255, 173, 127))

    # --- Step 2: Get skin pixels in LAB color space ---
    lab = cv2.cvtColor(img_resized, cv2.COLOR_BGR2LAB)
    skin_pixels = lab[mask > 0]

    if len(skin_pixels) < 50:
        raise ValueError("Not enough skin detected — use a clearer front-facing photo")

    # --- Step 3: K-Means clustering to find dominant skin color ---
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    kmeans.fit(skin_pixels)
    dominant_idx = np.bincount(kmeans.labels_).argmax()
    dominant_color = kmeans.cluster_centers_[dominant_idx]
    L, a, b = float(dominant_color[0]), float(dominant_color[1]), float(dominant_color[2])

    # --- Step 4: ITA angle to classify skin tone ---
    ITA = float(np.degrees(np.arctan((L - 50) / (b + 1e-6))))
    tone_label = "Dark"
    for threshold, label in FITZPATRICK:
        if ITA > threshold:
            tone_label = label
            break

    # --- Step 5: Undertone from a* and b* values ---
    if a > 128 and b > 128:
        undertone = "Warm"
    elif b < 125:
        undertone = "Cool"
    else:
        undertone = "Neutral"

    return {
        "tone_label": tone_label,
        "undertone": undertone,
        "ITA_angle": round(ITA, 2),
        "LAB_values": {
            "L": round(L, 1),
            "a": round(a, 1),
            "b": round(b, 1)
        },
        "best_colors": COLOR_PALETTES[undertone],
        "avoid_colors": AVOID_COLORS[undertone],
        "outfit_tip": OUTFIT_TIPS[undertone],
        "skin_pixels_found": int(len(skin_pixels)),
    }