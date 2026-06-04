from modules.face_shape import detect_face_shape
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "test.jpg"

try:
    result = detect_face_shape(image_path)
    print("\n=== FACE SHAPE ANALYSIS ===")
    print(f"Face Shape:  {result['shape']}")
    print(f"Description: {result['description']}")
    print(f"\nMeasurements:")
    print(f"  Forehead ratio: {result['measurements']['forehead_ratio']}")
    print(f"  Jaw ratio:      {result['measurements']['jaw_ratio']}")
    print(f"  Length ratio:   {result['measurements']['length_ratio']}")
    print(f"\nHairstyle Recommendations:")
    for h in result['hairstyle_recommendations']:
        print(f"  - {h}")
    print(f"\nNeckline Recommendations:")
    for n in result['neckline_recommendations']:
        print(f"  - {n}")
except Exception as e:
    print(f"Error: {e}")