# OCR PageObjectModel 

**page** = screenshot, which we are getting from bench (ex.: home_screen)
**locator** = coordinates of the element on the page (ex.: _HOME_BUTTON = [930,213])

```python
_HOME_BUTTON = [930,213]

def press_home_button(screen):
    screen.locator(_HOME_BUTTON).click()
```