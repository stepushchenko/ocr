import cv2

# paths to the images
big_image_path = 'resources/screenshots/mb.png'
small_image_path = 'resources/scraps/homeButton.png'

# prepare images
big_image = cv2.imread(big_image_path)
big_image_prepared = cv2.cvtColor(big_image, cv2.COLOR_BGR2GRAY)
small_image = cv2.imread(small_image_path, 0)

# prepare full list of coordinates
result = cv2.matchTemplate(big_image_prepared, small_image, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
height, width = small_image.shape[:2]
top_left = max_loc

# prepare coordinates of the center of the small image
width = round(top_left[0] + width/2)
height = round(top_left[1] + height/2)
print(f'Coordinates of the center of the small image: width {width} and height {height}')
