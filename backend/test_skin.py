from modules.skin_tone import detect_skin_tone
import sys

# Test with any image path you provide
image_path = sys.argv[1] if len(sys.argv) > 1 else "test.jpg"

try:
    result = detect_skin_tone(image_path)
    print("\n=== SKIN TONE ANALYSIS ===")
    print(f"Skin Tone:  {result['tone_label']}")
    print(f"Undertone:  {result['undertone']}")
    print(f"ITA Angle:  {result['ITA_angle']}")
    print(f"LAB Values: L={result['LAB_values']['L']} a={result['LAB_values']['a']} b={result['LAB_values']['b']}")
    print(f"Best Colors: {', '.join(result['best_colors'][:4])}")
    print(f"Avoid: {', '.join(result['avoid_colors'][:3])}")
    print(f"Tip: {result['outfit_tip']}")
    print(f"Skin pixels found: {result['skin_pixels_found']}")
except Exception as e:
    print(f"Error: {e}")