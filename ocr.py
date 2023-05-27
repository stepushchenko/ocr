# for Mac: brew install tesseract
# for Windows: pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from pytesseract import pytesseract, Output
from PIL import Image


class Lang:
    ENG = 'eng'
    RUS = 'rus'
    GERMAN = 'deu'


class GetCoordinates:

    def get_center_coordinate(self, img: str, word: str, lang: str):

        img = Image.open(img)  # open image
        image_data = pytesseract.image_to_data(img, lang=lang, output_type=Output.DICT)  # prepare image for analyzing

        if word in image_data['text']:
            index = image_data['text'].index(word)  # get the current word position in the list
            left = image_data['left'][index]  # left point coordinate
            top = image_data['top'][index]  # top point coordinate
            width = image_data['width'][index]  # the width
            height = image_data['height'][index]  # the height
            result_left = left + round(width/2)
            result_top = top + round(height/2)
            return f'Coordinates of the center of the word {word} are: {result_left}-{result_top}'


if __name__ == '__main__':
    get_coordinates = GetCoordinates()

    print(get_coordinates.get_center_coordinate(
        img='resources/example.png',
        lang=Lang.ENG,
        word='Search'
    ))

    print(get_coordinates.get_center_coordinate(
        img='resources/mb.png',
        lang=Lang.GERMAN,
        word='Abstands-Assistent'
    ))
