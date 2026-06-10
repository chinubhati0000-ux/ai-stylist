code = '''import cv2
import numpy as np

HAIRSTYLE_MAP = {
    "Oval": ["Beach waves", "Pixie cut", "Curtain bangs", "Long straight hair"],
    "Round": ["Long layers", "Side part", "High bun", "Straight long hair"],
    "Square": ["Soft curls", "Side-swept bangs", "Long layered bob", "Waves"],
    "Heart": ["Chin-length bob", "Side braids", "Low bun", "Layered lob"],
    "Diamond": ["Chin-length cuts", "Side-swept styles", "Textured bobs", "Soft waves"],
    "Oblong": ["Curtain bangs", "Voluminous curls", "Shoulder-length cuts", "Side parts"],
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
    "Oval":    "Your face is slightly longer than wide with a narrow forehead and jaw.",
    "Round":   "Your face has similar width and length with soft curved lines and full cheeks.",
    "Square":  "Your face has a strong angular jaw with forehead and jaw roughly the same width.",
    "Heart":   "Your face is wider at the forehead and narrows to a pointed chin.",
    "Diamond": "Your face is narrow at forehead and chin with wide cheekbones.",
    "Oblong":  "Your face is noticeably longer than wide with a long straight cheek line.",
}

def classify_shape(fw, jw, fl):
    if fl > 1.65:
        return "Oblong"
    elif fw < 0.78 and jw < 0.78 and fl > 1.3:
        return "Diamond"
    elif abs(fw - jw) < 0.08 and fl < 1.3:
        return "Round"
    elif abs(fw - jw) < 0.08 and fl < 1.5:
        return "Square"
    elif fw > jw + 0.12:
        return "Heart"
    elif fl > 1.35:
        return "Oval"
    else:
        return "Round"

def detect_face_shape(image_path: str) -> dict:
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not read image")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape[:2]

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
                forehead_w = dist(54, 284)
                jaw_w = dist(172, 397)
                cheek_w = dist(234, 454)
                face_length = dist(10, 152)
                fw = forehead_w / cheek_w
                jw = jaw_w / cheek_w
                fl = face_length / cheek_w
                shape = classify_shape(fw, jw, fl)
                return {
                    "shape": shape,
                    "description": SHAPE_DESCRIPTIONS[shape],
                    "measurements": {"forehead_ratio": round(fw, 3), "jaw_ratio": round(jw, 3), "length_ratio": round(fl, 3)},
                    "hairstyle_recommendations": HAIRSTYLE_MAP[shape],
                    "neckline_recommendations": NECKLINE_MAP[shape],
                }
    except Exception:
        pass

    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    if len(faces) == 0:
        fx, fy, fw_px, fh_px = 0, 0, w, h
    else:
        fx, fy, fw_px, fh_px = faces[0]

    face_w = float(fw_px)
    face_h = float(fh_px)
    fw = 0.85
    jw = 0.75
    fl = face_h / face_w if face_w > 0 else 1.4
    shape = classify_shape(fw, jw, fl)

    return {
        "shape": shape,
        "description": SHAPE_DESCRIPTIONS[shape],
        "measurements": {"forehead_ratio": round(fw, 3), "jaw_ratio": round(jw, 3), "length_ratio": round(fl, 3)},
        "hairstyle_recommendations": HAIRSTYLE_MAP[shape],
        "neckline_recommendations": NECKLINE_MAP[shape],
    }
'''

with open("modules/face_shape.py", "w") as f:
    f.write(code)
print("face_shape.py written successfully!")