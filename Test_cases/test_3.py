from selenium import webdriver
from pytest import mark
from time import sleep


@mark.task3
def test_3(app_config):
    driver = getattr(webdriver, app_config.which_browser)()
    url = 'https://antycaptcha.amberteam.pl:5443/exercises/exercise3?seed=97cb6030-c84a-43b8-94c3-99a39b0f54ef'

    try:
        driver.get(url)

        dropDownList = driver.find_element_by_xpath('//*[@id="s13"]/option[5]')
        button_Check = driver.find_element_by_id('solution')
        result = driver.find_element_by_id('trail')
        
        dropDownList.click()
        sleep(1)
        button_Check.click()
        sleep(1)

        assert result.text == 'OK. Good answer'
    finally:
        driver.close()
        driver.quit()
