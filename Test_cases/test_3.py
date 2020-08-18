from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pytest import mark

@mark.task3
def test_3(app_setup, task3_url):
    driver = app_setup
    driver.get(task3_url)
    wait = WebDriverWait(driver,10)

    options = driver.find_elements(By.CSS_SELECTOR, "option[value*='v']")         # pointer to all options from dropdown list
    numberOfOptions = len(options)           # number of option from dropdown list
    optDict = {}            # empty dictionary for group, color name keys with radio button value
    oneStep = driver.find_element(By.CSS_SELECTOR, 'td > code').text         # pointer to all box texts in instruction 
    btnCheck = driver.find_element(By.ID, 'solution')            # check button
    currentOut = driver.find_element(By.ID, 'trail')         # outcome web element
    currentOutTxt = currentOut.text         # string for compare changes after selected option (Trail...)

    for o in range (numberOfOptions):            # create dictionary of color name and it option[] value
        optDict[options[o].text] = o

    dropDownList = options[optDict[oneStep]] 
    dropDownList.click()
    wait.until_not(EC.text_to_be_present_in_element((By.ID, 'trail'), currentOutTxt))           # waiting until text change
    currentOutTxt = currentOut.text         # assigne new text value to compare in next step

    btnCheck.click()
    wait.until(EC.text_to_be_present_in_element((By.ID, 'trail'), 'OK'))            # wait until possible outcome appear (NOT OK / Ok. Good answer)

    currentOutTxt = currentOut.text         # assigne new text value to assert
    assert currentOutTxt == 'OK. Good answer'