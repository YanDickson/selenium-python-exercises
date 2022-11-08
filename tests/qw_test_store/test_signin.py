from pages.sign_page import SigninPage
from pages.my_account_page import MyAccountPage

class TestSigninPage:

  def test_valid_user_signin(self, browser):
    # Create instances of page object classes
    signin_page = SigninPage(browser)
    my_account_page = MyAccountPage(browser)

    # Given the user is on the sign in page
    signin_page.navigate()

    # When the user signs in as a valid user
    signin_page.signin_user("test-user@yopmail.com", "testuser")

    # Then the URL should be the my account URL
    assert my_account_page.url in my_account_page.current_url()

    # And the Account tab should be dosplayed
    assert my_account_page.page_tab().is_displayed() == True
