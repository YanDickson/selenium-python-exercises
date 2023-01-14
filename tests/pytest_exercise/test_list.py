fruits = ['apple', 'orange', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# verify that "avocado" is not in the list `fruits`
def test_not_in_list():
  assert "avocado" not in fruits

# add "strawberry" to the end of the list 
# and verify that 'strawberry' is now the last element in that list
def test_add_item():
  fruits.append("strawberry")
  assert fruits[-1] == "strawberry"

# remove the first instance of "apple" from the list
# verify that only one instance of ‘apple’ remains is now in the list
def test_remove_item():
  fruits.remove("apple")
  count = fruits.count("apple")
  assert count == 1

# iterate through the list and convert each item to uppercase 
# verify that each was converted
def test_iterate():
  for fruit in fruits:
    _fruit = fruit.upper()
    assert _fruit.isupper() == True