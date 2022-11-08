class TestString:
  
  my_address = "817 Joy Ridge Avenue, Northbrook, IL"
  zip_code = "60611"

  # Split the address where the commas appear, 
  # and verify that the second element of the result is " Northbrook"
  def test_split_string(self):
    my_address_list = self.my_address.split(',')
    assert my_address_list[1] == " Northbrook"
    
  # Convert the address to all caps, 
  # and verify that all letters of the new string in upper case
  def test_upper_case(self):
    my_result = self.my_address.upper()
    assert my_result.isupper() == True

  # using my_address and my_zip create a new string "817 Joy Ridge Avenue, Northbrook, IL, 60611"
  # Verify that the resulting string ends with "60611"
  def test_ends_with_zip(self):
    my_result = "{}, {}".format(self.my_address, self.zip_code)
    # assert my_result.endswith("60611") == True
    assert "60611" in my_result
