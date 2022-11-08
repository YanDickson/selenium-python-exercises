from pages.inventory_page import InventoryPage
from pages.product_detail_page import ProductDetailPage

partial_title = "Multi_Vibe"
item_name = "Multi-Vibe"

class TestProductDetails:
  
  def test_navigate_to_product_details(self, browser):
    # Create instances of page object classes
    inventory_page = InventoryPage(browser)
    product_detail_page = ProductDetailPage(browser)

    # Given the QW Test Store is displayed
    inventory_page.navigate()

    # When I click on Multi-Vibe
    inventory_page.get_item(inventory_page.multi_vibe_path).click()

    # Then I should be navigated to the product URL 
    item_url = product_detail_page.current_url(partial_title)
    assert item_url.endswith(inventory_page.multi_vibe_path) == True

    # And the page heading should be Multi-Vibe
    assert product_detail_page.page_heading().text == item_name

    # And the heading should be displayed
    assert product_detail_page.page_heading().is_displayed() == True
