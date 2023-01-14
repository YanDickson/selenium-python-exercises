from selenium.webdriver.common.by import By

class ThankYouPage:

  # CLASS VARIABLES
  url = 'https://webdriveruniversity.com/Contact-Us/contact-form-thank-you.html'

  # INSTANCE VARIABLES
  def __init__(self, browser):
    self.browser = browser

  # ELEMENT LOCATORS
  def page_heading(self):
    return self.browser.find_element(By.TAG_NAME, 'h1')
