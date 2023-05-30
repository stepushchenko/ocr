import cv2

# paths to the images
big_image_path = 'resources/screenshots/chess5.png'
small_image_path = 'resources/scraps/chess3.png'

# prepare big image
big_image = cv2.imread(big_image_path)
big_image_prepared = cv2.cvtColor(big_image, cv2.COLOR_BGR2GRAY)

# show big image
cv2.imshow('ChessOne', big_image)
cv2.waitKey(0)

# prepare small image
small_image = cv2.imread(small_image_path, 0)

# draw red rectangle near small image
result = cv2.matchTemplate(big_image_prepared, small_image, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
height, width = small_image.shape[:2]
top_left = max_loc
bottom_right = (top_left[0] + width, top_left[1] + height)
cv2.rectangle(big_image, top_left, bottom_right, (0, 0, 255), 5)

# show big image with red rectangle near small image
cv2.imshow('ChessOne', big_image)
cv2.waitKey(0)

# close all opened windows
cv2.destroyAllWindows()
