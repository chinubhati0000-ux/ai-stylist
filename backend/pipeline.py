from modules.skin_tone import detect_skin_tone
from modules.face_shape import detect_face_shape
from modules.makeup import get_makeup_recommendations

def analyze_face(image_path: str) -> dict:
    # Run all modules
    skin  = detect_skin_tone(image_path)
    shape = detect_face_shape(image_path)
    makeup = get_makeup_recommendations(
        skin["tone_label"],
        skin["undertone"],
        shape["shape"]
    )

    return {
        "skin":   skin,
        "shape":  shape,
        "makeup": makeup,
    }