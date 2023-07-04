from selenium.webdriver.common.by import By

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_cart(browser):
    browser.get(LINK)
    # time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket').get_attribute('value')
    assert len(button) > 0, 'Add to cart button not found. (Кнопка добавления в корзину не найдена)'
