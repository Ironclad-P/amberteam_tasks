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

    numberOfOptions = len(driver.find_elements_by_xpath('//*[@id="s13"]/option'))           # number of radio buttons to select in group
    optDict = {}            # empty dictionary for group, color name keys with radio button value
    oneStep = driver.find_element_by_xpath("/html/body/div/table/tbody/tr[2]/td[2]/code").text          # 
    btnCheck = driver.find_element_by_id('solution')
    currentOut = driver.find_element_by_id('trail')         # outcome web element
    currentOutTxt = currentOut.text         # string for compare changes after selected option (Trail...)

    for o in range (1, numberOfOptions + 1):            # create dictionary of color name and it option[] value
        optDict[driver.find_element_by_xpath('//*[@id="s13"]/option[{}]'.format(o)).text] = o
    dropDownList = driver.find_element_by_xpath('//*[@id="s13"]/option[{}]'.format(optDict[oneStep]))
    
    dropDownList.click()
    wait.until_not(EC.text_to_be_present_in_element((By.ID, 'trail'), currentOutTxt))           # waiting until text change
    currentOutTxt = currentOut.text         # assigne new text value to compare in next step

    btnCheck.click()
    wait.until(EC.text_to_be_present_in_element((By.ID, 'trail'), 'OK'))            # wait until possible outcome appear (NOT OK / Ok. Good answer)

    currentOutTxt = currentOut.text         # assigne new text value to assert
    assert currentOutTxt == 'OK. Good answer'