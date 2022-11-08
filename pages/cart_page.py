from selenium.webdriver.common.by import By

class CartPage:

  # CLASS VARIABLES
  page_url = 'https://qw-test-store-prod.netlify.app/cart/'

  # INSTANCE VARIABLES
  def __init__(self, browser):
    self.browser = browser

  # ELEMENT LOCATORS
  def item_name(self, item_path):
    return self.browser.find_element(By.CSS_SELECTOR, f'[href="{item_path}"]')

  def checkout_button(self):
    return self.browser.find_element(By.CLASS_NAME, 'black')

  # PAGE METHODS
  def navigate(self):
    self.browser.get(self.page_url)
    