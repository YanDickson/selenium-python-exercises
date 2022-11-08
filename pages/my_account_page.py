from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MyAccountPage:

  ### CLASS VARIABLES ###
  url = 'https://qw-test-store-prod.netlify.app/myaccount/'
  partial_title = "My Account"

  ### INSTANCE VARIABLES ###
  def __init__(self, browser):
    self.browser = browser

  ### ELEMENT LOCATORS ###
  def my_account_tab(self):
    return self.browser.find_element(By.LINK_TEXT, 'My Account')

  def page_tab(self):
    return self.browser.find_element(By.CSS_SELECTOR, '[href="/myaccount/"]')

  ### PAGE METHODS ###
  def current_url(self):
    # waits for title to contain partial page title
    wait = WebDriverWait(self.browser, 10)
    wait.until(EC.title_contains(self.partial_title))
    url = self.browser.current_url
    return url
