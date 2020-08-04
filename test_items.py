import time


def test_find_addtobasket_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    button = browser.find_elements_by_class_name('btn-add-to-basket')
    assert button, 'Button not found!'
    # time.sleep(30)  # для проверки соответствия языка сайта запрашивамогу языку
