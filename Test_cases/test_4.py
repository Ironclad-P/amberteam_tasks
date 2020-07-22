from selenium import webdriver
from pytest import mark
from time import sleep


@mark.task4
def test_4(app_config):
    driver = getattr(webdriver, app_config.which_browser)()
    url = 'https://antycaptcha.amberteam.pl:5443/exercises/exercise4?seed=b80e6fa0-bf53-47ae-b34c-5d7037fe3f4f'
    
    try:
        driver.get(url)

        group0 = driver.find_element_by_xpath(".//input[@type='radio' and @value='v60']")
        group1 = driver.find_element_by_xpath(".//input[@type='radio' and @value='v41']")
        group2 = driver.find_element_by_xpath(".//input[@type='radio' and @value='v82']")
        group3 = driver.find_element_by_xpath(".//input[@type='radio' and @value='v73']")
        button_Check = driver.find_element_by_id('solution')
        result = driver.find_element_by_id('trail')
        
        group0.click()
        sleep(0.5)
        group1.click()
        sleep(0.5)
        group2.click()
        sleep(0.5)
        group3.click()
        sleep(0.5) 
        button_Check.click()
        sleep(1)

        assert result.text == 'OK. Good answersv'
    finally:
        driver.close()
        driver.quit()