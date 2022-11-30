from pages.products_page import ProductsPage

laptop_select_value = 'laptop'
search_phrase = 'pants'

def test_filter_by_laptops(browser):
  products_page = ProductsPage(browser)

  # Given the user is on the product page
  browser.get(products_page.url)

  # When the user selects a category
  products_page.select_category_value(laptop_select_value)

  # Then the results should be of the selected category
  for category in products_page.product_categories() :
    text = category.text
    assert text == 'laptop'

def test_search_for_products(browser):
  products_page = ProductsPage(browser)
  
  # Given teh user is on the products page
  browser.get(products_page.url)

  # When the user searches for a products
  products_page.search_field().send_keys(search_phrase)

  # Then the item names in the results should contain the search phrase
  for item in products_page.product_name_list():
    assert search_phrase in (item.text).lower() 
    