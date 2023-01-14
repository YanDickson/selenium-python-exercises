from selenium.webdriver.common.by import By

class ContactUsPage:

  # CLASS VARIABLES
  url = 'https://webdriveruniversity.com/Contact-Us/contactus.html'

   
  def __init__(self, browser):
    self.browser = browser

  # ELEMENT LOCATORS
  def first_name_field(self):
    return self.browser.find_element(By.NAME, 'first_name')

  def last_name_field(self):
    return self.browser.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]')

  def email_field(self):
    return self.browser.find_element(By.NAME, 'email')

  def comments_field(self):
    return self.browser.find_element(By.TAG_NAME, 'textarea')

  def submit_button(self):
    return self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

  # PAGE METHODS
  def fill_and_submit_form(self):
    self.first_name_field().send_keys('Test')
    self.last_name_field().send_keys('User')
    self.email_field().send_keys('test@user.com')
    self.comments_field().send_keys('This is a test.')
    self.submit_button().click()
