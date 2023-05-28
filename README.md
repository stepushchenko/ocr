# Installation

```bash
# activate venv
pip3 install -r requirements.txt  # install requirements
```

# OCR PageObjectModel


```python
# screenshots types
    # screenshot of the home screen where app icons placed
        # the main idea of the screen is stable (the list of apps)
        # the screenshot resolution and aspect ratio might be different 
        # the screenshot height are not imported and width are important 
        # we may save coordinates of the elements as pixes for height and % for width 
        
        # координаты [ширина, высота]
        # элемент [400, 200] на скриншоте [1400, 700]
        
        # Если ширина нового скриншота такая же или меньше дефолтного, а высота нового скриншота такая же или меньше, то делаем расчет новых координат:
            # допустим на вход пришел скрин нужного экрана, но в разрешении [1280, 620], когда дефолтный был [1400, 700]
            # значит, чтобы определить местоположение элемента на полученном скриншоте
            # надо пересчитать дефолтные координаты к новому разрешению
            # 1280 - это 91.42% от дефолтного значения 1400, значит дефолтные координаты надо умножить на 0.9142
            # новые координаты [366, 183]
            # полученные координаты возвращаем для осуществления клика по элементу 
            
def get_screenshot_path() -> str:
    # get screenshot from bench screen
    # save screenshot to the resources folder
    # return the path to the screenshot
    return 'resources/example.png'

def get_screenshot_resolution(screenshot_path: str) -> tuple:
    # get image from a path
    # return image resolution
    pass

def get_suitable_default_screenshot_resolution(screen: dict, input_screenshot_resolution: tuple) -> tuple:
    # from the list of default resolutions for current screen
    # select resolution which is available for using with new_screenshot_resolution
    pass

def get_percent_of_difference(default_screenshot_resolution: tuple, input_screenshot_resolution: tuple) -> float:
    # calculate and return percent of difference
    pass

def get_calculated_coordinates(default_coordinates: tuple, percent_of_difference: float) -> tuple:
    # get default coordinates 
    # calculate new coorditates
    # return tuple with new coordinates 
    pass

def get_new_coordinates_for_element(
        screen: dict,
        element_title: str,
        input_screenshot_path: str) -> tuple:
    input_screen_resolution = get_screenshot_resolution(screenshot_path=input_screenshot_path)
    suitable_default_screenshot_resolution = get_suitable_default_screenshot_resolution(
        screen=screen,
        input_screenshot_resolution=input_screen_resolution)
    percent_of_difference = get_percent_of_difference(
        default_screenshot_resolution=suitable_default_screenshot_resolution,
        input_screenshot_resolution=input_screen_resolution)
    return get_calculated_coordinates(
        default_coordinates=screen[suitable_default_screenshot_resolution][element_title],
        percent_of_difference=percent_of_difference
    )

# home screenshot elements
home_screen = {
    (1320, 900): {
        'button_home': (930,820),
        'icon_radio_app': (190, 13)
    }
}

def test_open_radio_app_from_home_screen():
    home_button_coordinates = get_new_coordinates_for_element(
        screen=home_screen,
        element_title='button_home',
        input_screenshot_path=get_screenshot_path()
    )
    # press the home button
    # get new coordinates for Radio app icon
    # press the Radio app icon
    # check the Radio app opened


# PLAN
# done: научились высчитывать новые координаты для элемента и кликать по этим координатам
# todo: научиться определять результат теста через: 
    # done: наличие текста на скриншоте
    # todo: наличие картинки на скриншоте 
```