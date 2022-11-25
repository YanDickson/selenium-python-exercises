from pages.products_page import ProductsPage
import pytest

class TestProducts:
  @pytest.mark.parametrize('value, category', [('shoes', 'shoes'), ('pant', 'pants'), ('couch', 'couch')])
  def test_category_filter(self, browser, value, category):
    products_page = ProductsPage(browser)

    # Given the user is on the product page
    browser.get(products_page.url)

    # When the user selects a category
    products_page.select_category_value(value)

    # Then the results should be of the selected category
    for element in products_page.product_categories() :
      text = element.text
      assert text == category

 
  @pytest.mark.parametrize('search_phrase', ['pants', 'laptop', 'shoe'])
  def test_search_for_products(self, browser, search_phrase):
    products_page = ProductsPage(browser)
    
    # Given teh user is on the products page
    browser.get(products_page.url)

    # When the user searches for a products
    products_page.search_field().send_keys(search_phrase)

    # Then the item names in the results should contain the search phrase
    for item in products_page.product_name_list():
      assert search_phrase in (item.text).lower()
    