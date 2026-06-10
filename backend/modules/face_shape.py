import cv2
import numpy as np

HAIRSTYLE_MAP = {
    "Oval": [
        "Beach waves — any length works",
        "Pixie cut — shows off your balanced features",
        "Curtain bangs — frames the face beautifully",
        "Long straight hair — elegant and classic",
    ],
    "Round": [
        "Long layers — adds length and slims the face",
        "Side part — creates asymmetry and length",
        "High bun — elongates the face",
        "Straight long hair with no volume at sides",
    ],
    "Square": [
        "Soft curls — softens the jawline",
        "Side-swept bangs — breaks the angular look",
        "Long layered bob — adds movement",
        "Waves starting below the chin",
    ],
    "Heart": [
        "Chin-length bob — balances wide forehead",
        "Side braids — draws attention downward",
        "Low bun — balances proportions",
        "Layered lob with volume at jaw",
    ],
    "Diamond": [
        "Chin-length cuts — widens the narrow chin",
        "Side-swept styles — softens cheekbones",
        "Textured bobs — adds width at jaw",
        "Soft waves from chin level",
    ],
    "Oblong": [
        "Curtain bangs — shortens the face",
        "Voluminous curls — adds width",
        "Shoulder-length cuts — best length",
        "Side parts with volume at sides",
    ],
}

NECKLINE_MAP = {
    "Oval":    ["V-neck", "Scoop neck", "Boat neck", "Most necklines work"],
    "Round":   ["V-neck", "Deep V", "Square neck", "Plunging neckline"],
    "Square":  ["Round neck", "Cowl neck", "Off-shoulder", "Sweetheart"],
    "Heart":   ["Boat neck", "Square neck", "Off-shoulder", "Halter"],
    "Diamond": ["Halter neck", "Off-shoulder", "Sweetheart", "Strapless"],
    "Oblong":  ["Boat neck", "Crew neck", "Wide necklines", "Turtleneck"],
}

SHAPE_DESCRIPTIONS = {
    "Oval":    "Your face is slightly longer than wide with a narrow forehead and jaw. This is considered the most balanced face shape.",
    "Round":   "Your face has similar width and length with soft, curved lines and full cheeks.",
    "Square":  "Your face has a strong, angular jaw with forehead and jaw roughly the same width.",
    "Heart":   "Your face is wider at the forehead and narrows to a pointed chin.",
    "Diamond": "Your face is narrow at forehead and chin with wide cheekbones — the rarest face shape.",
    "Oblong":  "Your face is noticeably longer than wide with a long straight cheek line.",
}

def detect_face_shape(image_path: str) -> dict:
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not read image")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape[:2]

    # Try MediaPipe first
    try:
        import mediapipe as mp
        mp_face_mesh = mp.solutions.face_mesh
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        with mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            min_detection_confidence=0.1
        ) as face_mesh:
            results = face_mesh.process(img_rgb)

            if results.multi_face_landmarks:
                lm = results.multi_face_landmarks[0].landmark

                def pt(idx):
                    return np.array([lm[idx].x * w, lm[idx].y * h])

                def dist(a, b):
                    return float(np.linalg.norm(pt(a) - pt(b)))

                forehead_w  = dist(54, 284)
                jaw_w       = dist(172, 397)
                cheek_w     = dist(234, 454)
                face_length = dist(10, 152)

                fw = forehead_w / cheek_w
                jw = jaw_w / cheek_w
                fl = face_length / cheek_w

                shape = classify_shape(fw, jw, fl)

                return {
                    "shape": shape,
                    "description": SHAPE_DESCRIPTIONS[shape],
                    "measurements": {
                        "forehead_ratio": round(fw, 3),
                        "jaw_ratio": round(jw, 3),
                        "length_ratio": round(fl, 3),
                    },
                    "hairstyle_recommendations": HAIRSTYLE_MAP[shape],
                    "neckline_recommendations": NECKLINE_MAP[shape],
                }
    except Exception:
        pass

    # Fallback — use OpenCV Haar cascade face detection
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30)
    )

    if len(faces) == 0:
        # Last resort — assume face fills the image
        fx, fy, fw_px, fh_px = 0, 0, w, h
    else:
        fx, fy, fw_px, fh_px = faces[0]

    # Estimate ratios from bounding box
    face_w = float(fw_px)
    face_h = float(fh_px)

    # Estimate proportions
    fw = 0.85   # forehead ratio estimate
    jw = 0.75   # jaw ratio estimate
    fl = face_h / face_w if face_w > 0 else 1.4

    # Refine using face region
    face_region = gray[fy:fy+fh_px, fx:fx+fw_px]
    if face_region.size > 0:
        top_third    = face_region[:fh_px//3, :]
        bottom_third = face_region[2*fh_px//3:, :]

        top_w    = np.sum(top_third > 100)
        bottom_w = np.sum(bottom_third > 100)

        if top_w > 0 and bottom_w > 0:
            ratio = top_w / bottom_w
            if ratio > 1.2: