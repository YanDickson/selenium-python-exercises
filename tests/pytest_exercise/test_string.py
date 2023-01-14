my_address = "817 Joy Ridge Avenue, Northbrook, IL"
zip_code = "60611"

# Split the address where the commas appear, 
# and verify that the second element of the result is " Northbrook"
def test_split_string():
  my_address_list = my_address.split(',')
  assert my_address_list[1] == " Northbrook"

# using my_address and my_zip create a new string "817 Joy Ridge Avenue, Northbrook, IL, 60611"
# Verify that the resulting string ends with "60611"
def test_ends_with_zip():
  my_result = "{}, {}".format(my_address, zip_code)
  assert my_result.endswith(zip_code) == True
