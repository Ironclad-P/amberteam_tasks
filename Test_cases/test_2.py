from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pytest import mark

@mark.task2
def test_2(app_setup, task2_url):
    driver = app_setup
    driver.get(task2_url)
    wait = WebDriverWait(driver,10)

    editBox = driver.find_element_by_id('t14')          # Edit box field
    btnB1 = driver.find_element_by_id('btnButton1')         # B1 button
    btnCheck = driver.find_element_by_id('solution')            # Check button
    numberOfSteps = len(driver.find_elements_by_xpath('/html/body/div/table/tbody/tr'))     # number of steps in instruction
    instruction = []           # empty list for instructions in the task
    currentOut = driver.find_element_by_id('trail')         # outcome web element
    currentOutTxt = currentOut.text         # string for compare changes after selected option (Trail...)

    for i in range(2, numberOfSteps + 1):           # create list of steps to execute
        step = driver.find_element_by_xpath("/html/body/div/table/tbody/tr[{}]/td[2]/code".format(i)).text
        instruction.append(step)
    
    editBox.clear()         # clear the text field
    editBox.send_keys(instruction[0])           # enter text from step 1 into the text field
    btnB1.click()
    wait.until_not(EC.text_to_be_present_in_element((By.ID, 'trail'), currentOutTxt))

    btnCheck.click()
    wait.until(EC.text_to_be_present_in_element((By.ID, 'trail'), 'OK'))            # wait until possible outcome appear (NOT OK / Ok. Good answer)
    
    currentOutTxt = currentOut.text         # assigne new text value to assert
    assert currentOutTxt == 'OK. Good answer'