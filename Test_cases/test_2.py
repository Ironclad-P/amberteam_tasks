from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pytest import mark

@mark.task2
def test_2(app_setup, task2_url):
    driver = app_setup
    driver.get(task2_url)
    wait = WebDriverWait(driver,10)

    editBox = driver.find_element_by_id('t14')
    buttonB1 = driver.find_element_by_id('btnButton1')
    buttonCheck = driver.find_element_by_id('solution')
    result = driver.find_element_by_id('trail')

    numberOfSteps = len(driver.find_elements_by_xpath('/html/body/div/table/tbody/tr'))
    instruction = []
    textToAssert = ''

    for i in range(2, numberOfSteps + 1):
        step = driver.find_element_by_xpath("/html/body/div/table/tbody/tr[{}]/td[2]/code".format(i)).text
        instruction.append(step)
    
    editBox.clear()
    editBox.send_keys(instruction[0])
    textToAssert += instruction[0]
    
    if instruction[1] == 'B1':
        textToAssert += 'b1'
        buttonB1.click()
        wait.until(ec.text_to_be_present_in_element((By.ID, 'trail'), textToAssert))
    
    buttonCheck.click()
    wait.until(ec.text_to_be_present_in_element((By.ID, 'trail'), 'OK'))
    assert result.text == 'OK. Good answer'