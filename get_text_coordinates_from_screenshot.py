import cv2
import easyocr


class Lang:
    ENG = 'en'
    GERMAN = 'de'


class TextRecognition:
    def get_all_text_from_img(self, img_path: str, lang: list) -> dict:
        # prepare image
        img = cv2.imread(img_path)
        # instance text detector

        reader = easyocr.Reader(lang)
        # detect text on image
        text_ = reader.readtext(img)
        # prepare result with coordinates
        result = {}
        for t in text_:
            coordinates, text, index = t
            result[text] = coordinates
        # return
        return result

    def get_block_coordinates(self, img_path: str, lang: list, text: str) -> dict:
        text_from_img = self.get_all_text_from_img(
            img_path=img_path,
            lang=lang
        )
        result = {}
        for key in text_from_img:
            if key.find(text) != -1:
                result[key] = text_from_img[key]
        return result

    def get_block_center_coordinates(self, img_path: str, lang: list, text: str) -> dict:

        text_from_img = self.get_all_text_from_img(
            img_path=img_path,
            lang=lang
        )

        for i in text_from_img:
            print(f'\nWord: {i}\nCoordinates: {text_from_img[i]}\n')

        blocks_coordinates = {}
        for key in text_from_img:
            if key.find(text) != -1:
                blocks_coordinates[key] = text_from_img[key]

        result = {}
        for key in blocks_coordinates:
            coordinates = blocks_coordinates[key]
            width = round((coordinates[0][0] + coordinates[1][0]) / 2)
            height = round((coordinates[0][1] + coordinates[3][1]) / 2)
            result[key] = [width, height]

        return result


if __name__ == '__main__':
    language = Lang()
    text_recognition = TextRecognition()

    image_eng = 'resources/screenshots/mb.png'

    print(
        text_recognition.get_block_center_coordinates(
            img_path=image_eng,
            lang=[language.ENG],
            text='DISPLAY_CENTRAL'
        )
    )
