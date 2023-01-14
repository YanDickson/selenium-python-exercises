from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
  
  # INSTANCE VARIABLES
  def __init__(self, browser):
    self.browser = browser

  # ELEMENT LOCATORS

  def checkout_button(self):
    return self.browser.find_element(By.CLASS_NAME, 'snipcart-button-primary')

  def name_field(self):
    return self.browser.find_element(By.NAME, 'name')

  def email_field(self):
    return self.browser.find_element(By.NAME, 'email')

  def street_address(self):
    return self.browser.find_element(By.NAME, 'address1')

  def city_field(self):
    return self.browser.find_element(By.NAME, 'city')

  def country_field(self):
    return self.browser.find_element(By.CSS_SELECTOR, '[id^="country_"]')

  def state_field(self):
    return self.browser.find_element(By.CSS_SELECTOR, '[id^="province_"]')

  def zip_field(self):
    return self.browser.find_element(By.CSS_SELECTOR, '[name="postalCode"]')

  def submit_button(self):
    return self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

  def payment_frame(self):
    return self.browser.find_element(By.CSS_SELECTOR, '[src^="https://payment"]')

  def card_field(self):
    return self.browser.find_element(By.ID, 'card-number')

  def expiry_field(self):
    return self.browser.find_element(By.ID, 'expiry-date')

  def cvv_field(self):
    return self.browser.find_element(By.ID, 'cvv')

  def order_invoice(self):
    return self.browser.find_element(By.CLASS_NAME, 'snipcart-order__invoice-number')

  # PAGE METHODS

  def checkout_items(self):
    wait = WebDriverWait(self.browser, 10)
    # Click checkout button
    self.checkout_button().click()
    # Fill and send billing information
    self.name_field().send_keys('Test User')
    self.email_field().send_keys('test505@yopmail.com')
    self.street_address().send_keys('123 Test Street')
    self.city_field().send_keys('Chicago')
    self.country_field().send_keys('United States', Keys.ENTER)
    self.state_field().send_keys('Illinois', Keys.ENTER)
    self.zip_field().send_keys('60611')
    self.submit_button().click()

    # Wait, move to frame and fill payment information
    wait.until(EC.visibility_of(self.payment_frame()))
    self.browser.switch_to.frame(self.payment_frame())
    self.card_field().send_keys('4242 4242 4242 4242')
    self.expiry_field().send_keys('08/23')
    self.cvv_field().send_keys('123')

    # Exit frame and submit information
    self.browser.switch_to.default_content()
    self.submit_button().click()
    