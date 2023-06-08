import cv2
import numpy as np

# paths to the images
big_image_path = 'resources/screenshots/mb.png'
small_image_path = 'resources/scraps/radioButton.png'

# get big image from a path
img_rgb = cv2.imread(big_image_path)
assert img_rgb is not None, "file could not be read, check with os.path.exists()"

# prepare big image
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread(small_image_path, cv2.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"

# search for a small image in a big image
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

# get the center of each shape
centers = set()
i = 0

for pt in zip(*loc[::-1]):
    if i == 0 or i % 9 == 0:
        center_x = pt[0] + w // 2
        center_y = pt[1] + h // 2
        center = (center_x, center_y)
        centers.add(center)
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        cv2.circle(img_rgb, center, 3, (0, 255, 2), 1)
        print(center)
    i += 1

# show big image with red rectangles and green centers
cv2.imshow('ChessOne', img_rgb)
cv2.waitKey(0)

# sort the centers based on y-coordinate and x-coordinate
sorted_centers = sorted(centers, key=lambda c: (c[1], c[0]))

# # print the sorted centers of each shape
# for center in sorted_centers:
#     print(f"Shape center: {center}")
