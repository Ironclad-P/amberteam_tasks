from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pytest import mark
from time import sleep

@mark.task3
def test_3(app_setup, task3_url):
    driver = app_setup
    driver.get(task3_url)
    wait = WebDriverWait(driver,100)

    dropDownListElement = driver.find_element_by_xpath('//*[@id="s13"]/option[5]')
    button_Check = driver.find_element_by_id('solution')
    result = driver.find_element_by_id('trail')
    
    dropDownListElement.click()
    wait.until(ec.text_to_be_present_in_element((By.ID, 'trail'), 's13'))
    button_Check.click()
    wait.until(ec.text_to_be_present_in_element((By.ID, 'trail'), 'OK'))
    assert result.text == 'OK. Good answer'