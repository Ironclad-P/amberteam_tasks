from selenium import webdriver
from pytest import mark
from time import sleep


@mark.task2
def test_2(app_config):
    driver = getattr(webdriver, app_config.which_browser)()
    url = 'https://antycaptcha.amberteam.pl:5443/exercises/exercise2?seed=45b24f59-6579-4087-ad13-f6f5949aace5'
    
    try:
        driver.get(url)

        editBox = driver.find_element_by_id('t14')
        button_B1 = driver.find_element_by_id('btnButton1')
        button_Check = driver.find_element_by_id('solution')
        result = driver.find_element_by_id('trail')
        
        editBox.clear()
        editBox.send_keys('Evening level television.')
        sleep(1)
        button_B1.click()
        sleep(1)
        button_Check.click()
        sleep(1)

        assert result.text == 'OK. Good answer'
    finally:
        driver.close()
        driver.quit()
