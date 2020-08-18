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

    groups = driver.find_elements(By.CSS_SELECTOR, 'h5')
    numberOfGroups = len(groups)            # number of groups in the task
    steps = driver.find_elements(By.CSS_SELECTOR, 'td > code')
    numberOfSteps = len(steps)          # number of steps in instruction
    
    numberOfOptions = 8         # number of radio buttons to select in group
    colorsName = ['Beluga Brown', 'Mango Orange', 'Verdoro Green',
                    'Freudian Gilt', 'Pink Kong', 'Duck Egg Blue',
                    'Anti - Establishment Mint', 'Amberlite Firemist']          # Posible color names to select
    
    instructions = []           # empty list for instructions in the task
    optDict = {}            # empty dictionary for group, color name keys with radio button value
    currentOut = driver.find_element(By.ID, 'trail')         # outcome web element
    currentOutTxt = currentOut.text         # string for compare changes after selected option (Trail...)
    btnCheck = driver.find_element(By.ID, 'solution')

    for i in range(numberOfSteps - 1):           # create list of steps to execute
        step = steps[i].text
        instructions.append(step)

    for g in range (numberOfGroups):         # create dictionary to all radio button groups 
        group = driver.find_elements(By.CSS_SELECTOR, "input[name*='s{}']".format(g))
        for x in range (numberOfOptions):            # create 2 keys dictionary for a group.
            valueName = group[x].get_attribute('value')
            groupIdx = group[x].get_attribute('name')
            optDict[groupIdx ,colorsName[x]] = valueName            # eg. (s0, Beluga Brown) = v01

    for select, groupNumber in zip(instructions, range(numberOfGroups)):          # loop to execute instruction steps
        keys = ('s' + str(groupNumber), select)
        if keys in optDict:
            value = optDict[keys]           # value for specific radio button in the group
        driver.find_element(By.CSS_SELECTOR, "input[value*='{}']".format(value)).click()
        wait.until_not(EC.text_to_be_present_in_element((By.ID, 'trail'), currentOutTxt))           # waiting until text change
        currentOutTxt = currentOut.text         # assigne new text value to compare in next loop step
    
    btnCheck.click()
    wait.until(EC.text_to_be_present_in_element((By.ID, 'trail'), 'OK'))            # wait until possible outcome appear (NOT OK / Ok. Good answer)
    
    currentOutTxt = currentOut.text         # assigne new text value to assert
    assert currentOutTxt == 'OK. Good answer'