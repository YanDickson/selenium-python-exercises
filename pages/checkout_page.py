from selenium.webdriver.common.by import By

class CheckoutPage:

  # INSTANCE VARIABLES
  def __init__(self, browser):
    self.browser = browser

  # PAGE ELEMENTS
  def iframe(self):
    return self.browser.find_element(By.CSS_SELECTOR, '.stripe_checkout_app')

  def email_field(self):
    return self.browser.find_element(By.ID, 'email')

  def name(self):
    return self.browser.find_element(By.ID, 'billing-name')

  def address(self):
    return self.browser.find_element(By.ID, 'billing-street')

  def zip(self):
    return self.browser.find_element(By.ID, 'billing-zip')

  def city(self):
    return self.browser.find_element(By.ID, 'billing-city')

  def submit_button(self):
    return self.browser.find_element(By.ID, 'submitButton')

  def card_number(self):
    return self.browser.find_element(By.ID, 'card_number')

  def expiration_field(self):
    return self.browser.find_element(By.ID, 'cc-exp')

  def cvc_field(self):
    return self.browser.find_element(By.ID, 'cc-csc')

  # PAGE METHODS
  def switch_to_frame(self):
    self.browser.switch_to.frame('stripe_checkout_app')

  def check_out(self, email, name, address, city, zip, card_number, exp_date, cvc):
    self.switch_to_frame()
    self.email_field().send_keys(email)
    self.name().send_keys(name)
    self.address().send_keys(address)
    # self.city().send_keys(city)
    self.zip().send_keys(zip)
    self.submit_button().click()
    self.card_number().send_keys(card_number)
    self.expiration_field().send_keys(exp_date)
    self.cvc_field().send_keys(cvc)
    self.submit_button().click()
