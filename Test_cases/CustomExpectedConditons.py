class element_has_exactly_the_same_text(object):
  """An expectation for checking that an element has a exactly the same text as given.

  locator - used to find the element
  returns the WebElement once it has the exactly the same name as given.
  """
  def __init__(self, locator, text):
    self.locator = locator
    self.text = text

  def __call__(self, driver):
    element = driver.find_element(*self.locator)   # Finding the referenced element
    if self.text == element.text:
        return element
    else:
        return False