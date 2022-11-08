"""
This module contains shared fixtures.
"""

import pytest
import selenium.webdriver

@pytest.fixture
def browser():
  """
  Initializes browser and quits the browser at the end of the test run
  """

  # Initialize the ChromeDriver instance
  # ChromeDriver is initialized and connected to a live Chrome browser
  b = selenium.webdriver.Chrome()

  # Make its calls wait up to 10 seconds for elements to appear
  # For every call WebDriver will wait up to 10 seconds before timing out
  b.implicitly_wait(30)

  # Return the WebDriver instance for the setup
  # This is returned temporarily
  yield b

  # Clean up phase starts here
  # Quit the WebDriver instance for the cleanup
  b.quit()