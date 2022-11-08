from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductDetailPage:

  ### CLASS VARIABLES ###
  woodsy_url = 'https://qw-test-store-prod.netlify.app/product/f2944a96-07e1-44b2-9a02-7bd564085570/'
  
  ### INSTANCE VARIABLES ###
  def __init__(self, broswer):
    self.browser = broswer

  ### ELEMENT LOCATORS ###
  def page_heading(self):
    return self.browser.find_element(By.CSS_SELECTOR, 'div.item div.header')

  def add_to_cart_button(self):
    return self.browser.find_element(By.CSS_SELECTOR, 'div > button')

  def added_to_cart(self):
    return self.browser.find_element(By.CLASS_NAME, 'check')

  ### PAGE METHODS ###
  def current_url(self, partial_title):
    # add wait for title to contain product name
    wait = WebDriverWait(self.browser, 10)
    wait.until(EC.title_contains(partial_title))
    url = self.browser.current_url
    return url

  def add_item_to_cart(self):
    button = self.add_to_cart_button()
    button.click()
    wait = WebDriverWait(self.browser, 10)
    wait.until(EC.visibility_of(self.added_to_cart()))
