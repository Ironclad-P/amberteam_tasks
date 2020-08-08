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
    buttonB2 = driver.find_element_by_id('btnButton2')
    buttonCheck = driver.find_element_by_id('solution')
    result = driver.find_element_by_id('trail')

    numberOfSteps = len(driver.find_elements_by_xpath('/html/body/div/table/tbody/tr'))
    instruction = []
    textToAssert = ''

    for i in range(2, numberOfSteps + 1):
        step = driver.find_element_by_xpath("/html/body/div/table/tbody/tr[{}]/td[2]/code".format(i)).text
        instruction.append(step)

    for x in instruction:
        if x == 'B1':
            textToAssert += 'b1'
            buttonB1.click()
            wait.until(EC.text_to_be_present_in_element((By.ID, 'trail'), textToAssert))
        else:
            textToAssert += 'b2'
            buttonB2.click()
            wait.until(EC.text_to_be_present_in_element((By.ID, 'trail'), textToAssert))

    buttonCheck.click()
    wait.until(EC.text_to_be_present_in_element((By.ID, 'trail'), 'OK'))
    assert result.text == 'OK. Good answer'
