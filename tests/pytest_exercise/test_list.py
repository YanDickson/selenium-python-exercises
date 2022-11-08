import pytest

@pytest.mark.unit
class TestList:
  
  fruits = ['apple', 'orange', 'pear', 'banana', 'kiwi', 'apple', 'banana']

  # verify that "avocado" is not in the list `fruits`
  def test_not_in_list(self):
    assert "avocado" not in self.fruits

  # add "strawberry" to the end of the list 
  # and verify that 'strawberry' is now the last element in that list
  def test_add_element(self):
    self.fruits.append("strawberry")
    assert self.fruits[-1] == "strawberry"

  # remove the first instance of "apple" from the list
  # verify that only one instance of ‘apple’ remains is now in the list
  # verify that the first element in `fruits` is not ‘apple’
  def test_list(self):
    self.fruits.remove("apple")
    count = self.fruits.count("apple")
    assert count == 1
    assert self.fruits[0] != "apple"