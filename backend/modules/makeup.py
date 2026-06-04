# Makeup recommendations based on skin tone and undertone

FOUNDATION_SHADES = {
    "Very Fair": {
        "Warm":    ["MAC NC10", "Fenty 110W", "Maybelline 120W"],
        "Cool":    ["MAC NW10", "Fenty 110N", "Maybelline 120C"],
        "Neutral": ["MAC N10",  "Fenty 110",  "Maybelline 120"],
    },
    "Fair": {
        "Warm":    ["MAC NC15", "Fenty 130W", "Maybelline 220W"],
        "Cool":    ["MAC NW15", "Fenty 130N", "Maybelline 220C"],
        "Neutral": ["MAC NC20", "Fenty 140",  "Maybelline 220"],
    },
    "Intermediate": {
        "Warm":    ["MAC NC25", "Fenty 240W", "Maybelline 330W"],
        "Cool":    ["MAC NW25", "Fenty 240N", "Maybelline 330C"],
        "Neutral": ["MAC NC30", "Fenty 250",  "Maybelline 330"],
    },
    "Tan": {
        "Warm":    ["MAC NC35", "Fenty 340W", "Maybelline 340W"],
        "Cool":    ["MAC NW35", "Fenty 340N", "Maybelline 340C"],
        "Neutral": ["MAC NC40", "Fenty 350",  "Maybelline 340"],
    },
    "Brown": {
        "Warm":    ["MAC NC45", "Fenty 420W", "Maybelline 380W"],
        "Cool":    ["MAC NW45", "Fenty 420N", "Maybelline 380C"],
        "Neutral": ["MAC NC50", "Fenty 430",  "Maybelline 380"],
    },
    "Dark": {
        "Warm":    ["MAC NC55", "Fenty 490W", "Maybelline 380W"],
        "Cool":    ["MAC NW55", "Fenty 490N", "Maybelline 380C"],
        "Neutral": ["MAC NC60", "Fenty 498",  "Maybelline 390"],
    },
}

BLUSH_SHADES = {
    "Warm":    ["Peachy coral", "Warm terracotta", "Apricot", "Brick rose"],
    "Cool":    ["Soft pink", "Berry rose", "Mauve", "Baby pink"],
    "Neutral": ["Dusty rose", "Nude pink", "Soft peach", "Natural rose"],
}

LIP_SHADES = {
    "Warm": {
        "everyday": ["Nude brown", "Peachy pink", "Warm beige"],
        "bold":     ["Brick red", "Coral red", "Warm orange-red"],
    },
    "Cool": {
        "everyday": ["Soft pink", "Mauve nude", "Rose"],
        "bold":     ["Classic red", "Berry", "Plum", "Magenta"],
    },
    "Neutral": {
        "everyday": ["Nude pink", "Rose brown", "Soft mauve"],
        "bold":     ["True red", "Raspberry", "Deep rose"],
    },
}

EYE_MAKEUP = {
    "Warm":    ["Bronze and copper eyeshadow", "Brown eyeliner", "Gold shimmer lid", "Warm terracotta crease"],
    "Cool":    ["Silver and grey eyeshadow", "Black eyeliner", "Icy pink shimmer", "Plum crease"],
    "Neutral": ["Champagne eyeshadow", "Brown-black eyeliner", "Rose gold shimmer", "Taupe crease"],
}

FACE_SHAPE_BLUSH_TECHNIQUE = {
    "Oval":    "Apply blush to the apples of cheeks and blend upward toward temples.",
    "Round":   "Apply blush diagonally from cheekbones toward temples to elongate face.",
    "Square":  "Apply blush on the apples only and blend softly — avoid temples.",
    "Heart":   "Apply blush low on cheeks and blend downward to balance wide forehead.",
    "Diamond": "Apply blush horizontally across cheekbones to add width.",
    "Oblong":  "Apply blush horizontally across cheeks to add width to the face.",
}

def get_makeup_recommendations(tone_label: str, undertone: str, face_shape: str) -> dict:
    foundation = FOUNDATION_SHADES.get(tone_label, FOUNDATION_SHADES["Intermediate"])
    shades = foundation.get(undertone, foundation["Neutral"])

    return {
        "foundation_shades": shades,
        "blush": BLUSH_SHADES[undertone],
        "lip_everyday": LIP_SHADES[undertone]["everyday"],
        "lip_bold": LIP_SHADES[undertone]["bold"],
        "eye_makeup": EYE_MAKEUP[undertone],
        "blush_technique": FACE_SHAPE_BLUSH_TECHNIQUE.get(face_shape, "Apply blush to apples of cheeks."),
        "pro_tip": f"For {undertone.lower()} undertones, choose {'gold' if undertone == 'Warm' else 'silver' if undertone == 'Cool' else 'gold or silver'} jewelry to complement your makeup."
    }