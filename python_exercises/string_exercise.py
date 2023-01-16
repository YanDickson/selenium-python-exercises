'''
Given the below string `my_address`, use strings methods
 to complete the following tasks: 
'''
my_address = "817 Joy Ridge Avenue, Northbrook, IL"
zip_code = "60611"

# Split the address where the commas appear and assign the result to a new variable
my_address_list = my_address.split(', ')
print(my_address_list)

# Given a second string, zip_code = "60611", 
# use all methods of concatenation from the slides to make 
# the string "817 Joy Ridge Avenue, Northbrook, IL, 60611"

# Using + operator
full_address0 = my_address + "," + " " + zip_code

# Using format() function
full_address1 = '{}, {}'.format(my_address, zip_code)

# Using f-string
full_address2 = f'{my_address}, {zip_code}'

print(full_address0)
print(full_address1)
print(full_address2)
