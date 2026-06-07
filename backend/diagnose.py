import cv2
import numpy as np

for f in ['test.jpg', 'dark.jpg', 'indian.jpg']:
    img = cv2.imread(f)
    if img is None:
        print(f'{f}: Could not read file')
        continue
    img = cv2.resize(img, (400, 400))
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    center = lab[150:250, 150:250].reshape(-1, 3)
    avg = center.mean(axis=0)
    b_centered = avg[2] - 128
    L_adjusted = avg[0] - 50
    ITA = float(__import__('numpy').degrees(__import__('numpy').arctan2(L_adjusted, b_centered + 1e-6)))
    print(f'{f}: L={avg[0]:.1f} a={avg[1]:.1f} b={avg[2]:.1f} ITA={ITA:.1f}')