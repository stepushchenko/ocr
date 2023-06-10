import cv2


class UniqueImageCoordinates:
    def prepare_image(
            self,
            image_path: str
    ):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image

    def get_center_coordinates(
            self,
            big_image,
            small_image
    ):
        result = cv2.matchTemplate(big_image, small_image, cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        height, width = small_image.shape[:2]
        top_left = max_loc
        width = round(top_left[0] + width/2)
        height = round(top_left[1] + height/2)
        return width, height


if __name__ == '__main__':
    unique_img_coordinates = UniqueImageCoordinates()
    big_image_path = 'resources/screenshots/mb.png'
    small_image_path = 'resources/scraps/homeButton.png'  # 1 element
    big_image = unique_img_coordinates.prepare_image(big_image_path)
    small_image = unique_img_coordinates.prepare_image(small_image_path)
    width, height = unique_img_coordinates.get_center_coordinates(
        big_image=big_image,
        small_image=small_image
    )
    print(f'Coordinates of the center: width {width}, height {height}')
