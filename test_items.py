from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button(browser):
    browser.get(link)
    button1=browser.find_elements(By.CLASS_NAME,"btn-add-to-basket")
#find_elemetS for correct assert work
    assert button1, "The buy-button is not found"
