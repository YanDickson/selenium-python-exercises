from pages.webdriver_university.contact_us_page import ContactUsPage
from pages.webdriver_university.thank_you_page import ThankYouPage
from selenium.webdriver.common.by import By
import time

def test_contact_us(browser):
  '''This test is designed without the use of page objects'''

  contact_us_url = 'https://webdriveruniversity.com/Contact-Us/contactus.html'
  thank_you_url = 'https://webdriveruniversity.com/Contact-Us/contact-form-thank-you.html'

  # Given the user is on the contact us page
  browser.get(contact_us_url)

  # When the user fills out and submits the form
  first_name_field = browser.find_element(By.NAME, 'first_name')
  last_name_field = browser.find_element(By.CSS_SELECTOR, '[placeholder="Last Name"]')
  email_field = browser.find_element(By.NAME, 'email')
  comments_field = browser.find_element(By.TAG_NAME, 'textarea')
  submit_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')

  first_name_field.send_keys('Test')
  last_name_field.send_keys('User')
  email_field.send_keys('test@user.com')
  comments_field.send_keys('This is a test.')
  submit_button.click()

  # Then the user should see a thank you message
  thank_you_heading = browser.find_element(By.TAG_NAME, 'h1')
  assert thank_you_heading.is_displayed() == True
  assert thank_you_heading.text == 'Thank You for your Message!'

  # And the current URL should be the Thank You URL
  assert browser.current_url == thank_you_url
  time.sleep(1) # sleep added for visual demonstration

def test_contact_us_object(browser):
  '''This test demonstates creating tests with page objects'''

  contact_us_page = ContactUsPage(browser)
  thank_you_page = ThankYouPage(browser)

  # Given the user is on the contact us page
  browser.get(contact_us_page.url)

  # When the user fills out and submits the form
  contact_us_page.fill_and_submit_form()

  # Then the user should see a thank you message
  assert thank_you_page.page_heading().text == 'Thank You for your Message!'

  # And the current URL should be the Thank You URL
  assert thank_you_page.url == browser.current_url
  time.sleep(1) # sleep added for visual demonstration
  