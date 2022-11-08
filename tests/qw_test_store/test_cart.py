from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
import time

email = 'test@test.com'
name = 'Test User'
address = '123 Test User'
zip = '60611'
city = 'Kingston'
card_number = '4111111111111111'
exp_date = '11/24'
cvc = '123'

class TestCart:
  
  def test_add_item(self, browser):
    # Create instances of page object classes
    product_detail_page = ProductDetailPage(browser)
    inventory_page = InventoryPage(browser)
    cart_page = CartPage(browser)

    # Given the user is on the product details page
    browser.get(product_detail_page.woodsy_url)

    # When the user clicks the Add to Cart button
    product_detail_page.add_item_to_cart()

    # Then the item should be in the cart
    cart_page.navigate()
    is_it_displayed = cart_page.item_name(inventory_page.woodsy_path).is_displayed()
    assert is_it_displayed == True

  def test_purchase_item(self, browser):
    # Create instances of page object classes
    product_detail_page = ProductDetailPage(browser)
    checkout_page = CheckoutPage(browser)
    cart_page = CartPage(browser)

    # Given an item is in the cart
    browser.get(product_detail_page.woodsy_url)
    product_detail_page.add_item_to_cart()
    cart_page.navigate()

    # When the user checks out
    cart_page.checkout_button().click()
    checkout_page.check_out(email, name, address, city, zip, card_number, exp_date, cvc)

    # Then the user should see a success message
    time.sleep(5)
    