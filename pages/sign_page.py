from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SigninPage:

  ### CLASS VARIABLES ###
  url = 'https://qw-test-store-prod.netlify.app/login/'
  partial_title = 'Login'

  ### INSTANCE VARIABLES ###
  def __init__(self, browser):
    self.browser = browser

  ### ELEMENT LOCATORS ###
  def email_field(self):
    return self.browser.find_element(By.ID, 'email')

  def password_field(self):
    return self.browser.find_element(By.NAME, 'password')

  def submit_button(self):
    return self.browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

  def error_message(self):
    return self.browser.find_element(By.CSS_SELECTOR, 'div.error p')

  def error_heading(self):
    return self.browser.find_element(By.CSS_SELECTOR, 'div.error div.header')

  ### PAGE METHODS ###
  def navigate(self):
    self.browser.get(self.url)

  def enter_email(self, email):
    email_field = self.email_field()
    email_field.send_keys(email)

  def enter_password(self, password):
    password_field = self.password_field()
    password_field.send_keys(password)

  def click_submit(self):
    submit_button = self.submit_button()
    submit_button.click()

  def signin_user(self, email, password):
    self.enter_email(email)
    self.enter_password(password)
    self.click_submit()

  # Returns the URL of the current page
  def current_url(self):
    # waits for title to contain partial page title
    wait = WebDriverWait(self.browser, 10)
    wait.until(EC.title_contains(self.partial_title))
    url = self.browser.current_url
    return url
