import cv2
import easyocr
# import matplotlib.pyplot as plt

image_path = 'resources/screenshots/text.png'

# prepare image
img = cv2.imread(image_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# detect text on image
text_ = reader.detect(img)

for t in text_:
    print(t)

# issue with pyend
# more details here: https://github.com/pandas-dev/pandas/issues/27532#issuecomment-514044754
