from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class ProductsPage:

  # CLASS VARIABLES
  url = 'https://ui-automation-camp.vercel.app/products#'

  # INSTANCE VARIABLES
  def __init__(self, browser):
    self.browser = browser

  # LOCATORS
  def category_dropdown(self):
    return self.browser.find_element(By.ID, 'category')

  def product_categories(self): 
    return self.browser.find_elements(By.CLASS_NAME, 'css-1ccau2i')

  def search_field(self):
    return self.browser.find_element(By.ID, 'search')

  def product_name_list(self):
    return self.browser.find_elements(By.CLASS_NAME, 'css-1n64n71')

  # PAGE METHODS
  def select_category_text(self, text):
    list = Select(self.category_dropdown())
    list.select_by_visible_text(text)
