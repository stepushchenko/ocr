import cv2
import numpy


class MultiplyImageCoordinates:

    def prepare_image(
            self,
            image_path: str
    ):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image

    def get_coordinates_small_imgs_in_big_img(
            self,
            big_img,
            small_img,
            threshold: float = 0.8
    ):
        w, h = small_img.shape[::-1]
        res = cv2.matchTemplate(big_img, small_img, cv2.TM_CCOEFF_NORMED)
        loc = numpy.where(res >= threshold)

        # get the center of each shape
        result = []
        i = 0
        for pt in zip(*loc[::-1]):
            if i == 0 or i % 9 == 0:
                center_x = pt[0] + w // 2
                center_y = pt[1] + h // 2
                result.append((center_x, center_y))
            i += 1
        return result


if __name__ == '__main__':
    multiply_img_coordinates = MultiplyImageCoordinates()
    big_image_path = 'resources/screenshots/mb.png'
    small_image_path = 'resources/scraps/radioButton.png'  # 2 elements
    big_image = multiply_img_coordinates.prepare_image(big_image_path)
    small_image = multiply_img_coordinates.prepare_image(small_image_path)
    print(
        multiply_img_coordinates.get_coordinates_small_imgs_in_big_img(
            big_img=big_image,
            small_img=small_image
        )
    )
