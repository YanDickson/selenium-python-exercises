from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductDetailsPage:

  # CLASS VARIABLES
  hooded_shirt_url = 'https://ui-automation-camp.vercel.app/products/quality-sweatshirt-hooded'

  # INSTANCE VARIABLES
  def __init__(self, browser):
    self.browser = browser
  
  # LOCATORS
  def add_to_cart_button(self):
    return self.browser.find_element(By.ID, 'add-to-cart')

  # PAGE METHODS
  def add_item_to_cart(self, url):
    '''Waits for the cart to be rendered and adds item to cart'''
    self.browser.get(url)
    wait = WebDriverWait(self.browser, 10)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'top-cart'), '$0.00'))
    self.add_to_cart_button().click()
