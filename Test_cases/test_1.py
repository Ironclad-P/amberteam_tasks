from selenium import webdriver
from pytest import mark
from time import sleep


@mark.task1
def test_1(app_config):
    driver = getattr(webdriver, app_config.which_browser)()
    url = 'https://antycaptcha.amberteam.pl:5443/exercises/exercise1?seed=52a1bfe6-fd37-4587-a5cc-27a00a978d48'

    try:
        driver.get(url)

        button_B1 = driver.find_element_by_id('btnButton1')
        button_Check = driver.find_element_by_id('solution')
        result = driver.find_element_by_id('trail')

        i = 0
        while i < 3:
            button_B1.click()
            i = i + 1
            sleep(1)
        
        button_Check.click()
        sleep(1)
        assert result.text == 'OK. Good answerv'
    finally:
        driver.close()
        driver.quit()