fruits = ['apple', 'orange', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# verify that "avocado" is not in the list `fruits`
def test_not_in_list():
  assert "avocado" not in fruits

# add "strawberry" to the end of the list 
# and verify that 'strawberry' is now the last element in that list
def test_add_element():
  fruits.append("strawberry")
  assert fruits[-1] == "strawberry"

# remove the first instance of "apple" from the list
# verify that only one instance of ‘apple’ remains is now in the list
# verify that the first element in `fruits` is not ‘apple’
def test_list():
  fruits.remove("apple")
  count = fruits.count("apple")
  assert count == 1
  assert fruits[0] != "apple"