from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pytest import mark
from CustomExpectedConditons import element_has_exactly_the_same_text as EqTxt

@mark.task1
def test_1(app_setup, task1_url):
    driver = app_setup
    driver.get(task1_url)
    wait = WebDriverWait(driver,10)

    btnB1 = driver.find_element_by_id('btnButton1')         # B1 button
    btnB2 = driver.find_element_by_id('btnButton2')         # B2 button
    btnCheck = driver.find_element_by_id('solution')        # Check button
    steps = driver.find_elements_by_css_selector('td >code')            # pointer to all box texts in instruction 
    numberOfSteps = len(steps)         # number of steps in instruction + expected outcome
    instruction = []           # empty list for instructions in the task
    currentOut = driver.find_element_by_id('trail')         # outcome web element
    currentOutTxt = currentOut.text         # string for compare changes after selected option (Trail...)

    for i in range(numberOfSteps - 1):           # create list of teststeps to execute
        step = steps[i].text
        instruction.append(step)

    for x in instruction:          # loop to execute instruction steps
        if x == 'B1':
            btnB1.click()
            wait.until_not(EqTxt((By.ID, 'trail'), currentOutTxt))
            currentOutTxt = currentOut.text         # assigne new text value to assert
        else:
            btnB2.click()
            wait.until_not(EqTxt((By.ID, 'trail'), currentOutTxt))
            currentOutTxt = currentOut.text         # assigne new text value to assert

    btnCheck.click()
    wait.until(EC.text_to_be_present_in_element((By.ID, 'trail'), 'OK'))            # wait until possible outcome appear (NOT OK / Ok. Good answer)

    currentOutTxt = currentOut.text         # assigne new text value to assert
    assert currentOutTxt == 'OK. Good answer'
