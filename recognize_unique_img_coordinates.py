"""
Let's now go over this code.
We import OpenCV module.
We then create a variable, image, which contains the image we want to search. In this case, it is 'Rainforest.png'.
We show this image.
We then create a grayscale version of this image. This simplifies the image.

We then create another variable, template, which represents the subset image that we want to search for within the
larger image, image ('Rainforest.png'). This image is named 'Yellowing-leaf.png'.

We then have another variable, result, which stores basically whether there is a match found.

We then create a tuple of values that allows us to get the location of the match, assuming there is a match. The
variable, max_loc, represents the

Next, we have another tuple, height and width, that contain the height and width of the template image, or the target
image we are searching for within the larger image. We have these values because we are going to highlight the image
once found.

We then have a variable, opposite_corner, which represents the bottom right of the rectangle we will create. If we
take max_loc[0] and add the width and max_loc[1] and add the height, we have obtained the bottom right corner.

max_loc represents the top left corner.
We then use the cv2.rectangle() function to draw a rectangle around the match. We do this in a red color with a line
thickness of 5.

We then show the image.
And this is how we can match an image embedded in another image in Python using OpenCV.
"""

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

# draw red rectangle near small image on a big image
result = cv2.matchTemplate(big_image_prepared, small_image, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
height, width = small_image.shape[:2]
top_left = max_loc
bottom_right = (top_left[0] + width, top_left[1] + height)
cv2.rectangle(big_image, top_left, bottom_right, (0, 0, 255), 5)

# show big image with red rectangle near small image
cv2.imshow('ChessOne', big_image)
cv2.waitKey(0)

# prepare coordinates of the center of the small image
width = round(top_left[0] + width/2)
height = round(top_left[1] + height/2)
print(f'Coordinates of the center of the small image: width {width} and height {height}')

# close all opened windows
cv2.destroyAllWindows()
