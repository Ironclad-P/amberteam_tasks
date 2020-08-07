from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pytest import mark
from time import sleep

@mark.task4
def test_4(app_setup, task4_url):
    driver = app_setup
    driver.get(task4_url)
    wait = WebDriverWait(driver,100)

    group0 = driver.find_element_by_xpath(".//input[@type='radio' and @value='v60']")
    group1 = driver.find_element_by_xpath(".//input[@type='radio' and @value='v41']")
    group2 = driver.find_element_by_xpath(".//input[@type='radio' and @value='v82']")
    group3 = driver.find_element_by_xpath(".//input[@type='radio' and @value='v73']")
    button_Check = driver.find_element_by_id('solution')
    result = driver.find_element_by_id('trail')
    
    group0.click()
    wait.until(ec.text_to_be_present_in_element((By.ID, 'trail'), '[6'))
    group1.click()
    wait.until(ec.text_to_be_present_in_element((By.ID, 'trail'), '[6, 4'))
    group2.click()
    wait.until(ec.text_to_be_present_in_element((By.ID, 'trail'), '[6, 4, 8'))
    group3.click()
    wait.until(ec.text_to_be_present_in_element((By.ID, 'trail'), '[6, 4, 8, 7]'))

    button_Check.click()
    wait.until(ec.text_to_be_present_in_element((By.ID, 'trail'), 'OK'))
    assert result.text == 'OK. Good answer'