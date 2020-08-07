from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pytest import mark

@mark.task1
def test_1(app_setup, task1_url):
    driver = app_setup
    driver.get(task1_url)
    wait = WebDriverWait(driver,10)

    buttonB1 = driver.find_element_by_id('btnButton1')
    buttonCheck = driver.find_element_by_id('solution')
    result = driver.find_element_by_id('trail')

    for x in range(1,4):
        text = 'b1' * x
        buttonB1.click()
        wait.until(EC.text_to_be_present_in_element((By.ID, 'trail'), text))
    
    buttonCheck.click()
    wait.until(EC.text_to_be_present_in_element((By.ID, 'trail'), 'OK'))
    assert result.text == 'OK. Good answer'
