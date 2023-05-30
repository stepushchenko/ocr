import cv2
import numpy as np

# paths to the images
big_image_path = 'resources/screenshots/chess1.png'
small_image_path = 'resources/scraps/chess2.png'

# get big image from a path
img_rgb = cv2.imread(big_image_path)
assert img_rgb is not None, "file could not be read, check with os.path.exists()"

# prepare big image
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread(small_image_path, cv2.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"

# search for a small images in a big image
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
center_coordinates = []
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

# todo: prepare a dict with coordinates of the center of each found image

# show big image with red rectangle
cv2.imshow('ChessOne', img_rgb)
cv2.waitKey(0)
