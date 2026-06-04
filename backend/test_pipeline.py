from pipeline import analyze_face
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "test.jpg"

result = analyze_face(image_path)

print("\n========== FULL ANALYSIS ==========")
print(f"\n--- SKIN ---")
print(f"Tone:      {result['skin']['tone_label']}")
print(f"Undertone: {result['skin']['undertone']}")
print(f"ITA Angle: {result['skin']['ITA_angle']}")
print(f"Best Colors: {', '.join(result['skin']['best_colors'][:4])}")

print(f"\n--- FACE SHAPE ---")
print(f"Shape:     {result['shape']['shape']}")
print(f"Description: {result['shape']['description']}")
print(f"Top Hairstyle: {result['shape']['hairstyle_recommendations'][0]}")

print(f"\n--- MAKEUP ---")
print(f"Foundation: {', '.join(result['makeup']['foundation_shades'])}")
print(f"Blush:      {result['makeup']['blush'][0]}")
print(f"Lip (daily): {result['makeup']['lip_everyday'][0]}")
print(f"Lip (bold):  {result['makeup']['lip_bold'][0]}")
print(f"Eyes:        {result['makeup']['eye_makeup'][0]}")
print(f"Blush tip:   {result['makeup']['blush_technique']}")
print(f"Pro tip:     {result['makeup']['pro_tip']}")
print("\n====================================")