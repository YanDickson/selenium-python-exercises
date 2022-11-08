from selenium.webdriver.common.by import By

class InventoryPage:

  ### CLASS VARIABLES ###
  url = 'https://qw-test-store-prod.netlify.app/'
  multi_vibe_path = '/product/e1f683cd-2e31-4791-ade4-dab13f67b043/'
  woodsy_path = '/product/f2944a96-07e1-44b2-9a02-7bd564085570/'

  ### INSTANCE VARIABLES ###
  def __init__(self, browser):
    self.browser = browser

  ### ELEMENT LOCATORS ###
  def get_item(self, item_path):
    return self.browser.find_element(By.CSS_SELECTOR, '[href="{}"]'.format(item_path))

  ### PAGE METHODS ###
  def navigate(self):
    self.browser.get(self.url)
