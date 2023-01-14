from pages.camp_store.cart_page import CartPage
from pages.camp_store.product_details_page import ProductDetailsPage

def test_checkout(browser):
  cart_page = CartPage(browser)
  product_details_page = ProductDetailsPage(browser)

  # Given an item is added to the cart
  product_details_page.add_item_to_cart(
    product_details_page.hooded_shirt_url
  )

  # When the checkout process is completed
  cart_page.checkout_items()    

  # Then the user should see the thank you page
  invoice = cart_page.order_invoice()
  assert invoice.is_displayed() == True
  assert '#/order/' in browser.current_url
