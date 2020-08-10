from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pytest import mark

@mark.task4
def test_4(app_setup, task4_url):
    driver = app_setup
    driver.get(task4_url)
    wait = WebDriverWait(driver,10)

    numberOfGroups = len(driver.find_elements_by_xpath('/html/body/div/div/h5'))            # number of groups in the task
    numberOfSteps = len(driver.find_elements_by_xpath('/html/body/div/table/tbody/tr'))     # number of steps in instruction
    numberOfOptions = len(driver.find_elements_by_xpath('/html/body/div/div[1]/input'))     # number of radio buttons to select in group
    colorsName = ['Beluga Brown', 'Mango Orange', 'Verdoro Green',
                    'Freudian Gilt', 'Pink Kong', 'Duck Egg Blue',
                    'Anti - Establishment Mint', 'Amberlite Firemist']          # Posible color names to select
    instructions = []           # empty list for instructions in the task
    optDict = {}            # empty dictionary for group, color name keys with radio button value
    currentOut = driver.find_element_by_id('trail')         # outcome web element
    currentOutTxt = currentOut.text         # string for compare changes after selected option (Trail...)
    btnCheck = driver.find_element_by_id('solution')

    for i in range(2, numberOfSteps + 1):           # create list of steps to execute
        step = driver.find_element_by_xpath("/html/body/div/table/tbody/tr[{}]/td[2]/code".format(i)).text
        instructions.append(step)

    for g in range (1, numberOfGroups + 1):         # create dictionary to all radio button groups 
        group = driver.find_elements_by_xpath('/html/body/div/div[{}]/input'.format(g))
        for x in range (1, numberOfOptions + 1):            # create 2 keys dictionary for a group.
            valueName = group[x - 1].get_attribute('value')
            groupIdx = group[x - 1].get_attribute('name')
            optDict[groupIdx ,colorsName[x - 1]] = valueName            # eg. (s0, Beluga Brown) = v01

    for select, groupNumber in zip(instructions, range(numberOfGroups)):          # loop to execute instruction steps
        keys = ('s' + str(groupNumber), select)
        if keys in optDict:
            value = optDict[keys]           # value for specific radio button in the group
        driver.find_element_by_xpath(".//input[@type='radio' and @value='{}']".format(value)).click()
        wait.until_not(EC.text_to_be_present_in_element((By.ID, 'trail'), currentOutTxt))           # waiting until text change
        currentOutTxt = currentOut.text         # assigne new text value to compare in next loop step
    
    btnCheck.click()
    wait.until(EC.text_to_be_present_in_element((By.ID, 'trail'), 'OK'))            # wait until possible outcome appear (NOT OK / Ok. Good answer)
    
    currentOutTxt = currentOut.text         # assigne new text value to assert
    assert currentOutTxt == 'OK. Good answer'