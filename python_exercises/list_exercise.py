'''
Given the following list called 'fruits', 
complete the following tasks on line 7, 11 and 15
'''
fruits = ['apple', 'orange', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# Add 'strawberry' to the end of the list
fruits.append('strawberry')
print(fruits)

# Find the number of times 'banana' appears in the list
my_count = fruits.count("banana")
print(my_count)

# Remove the first instance of 'apple' from the list
fruits.remove("apple")
print(fruits)

# Get the second to fourth elements of the list and assign this sublist to a variable
elements = fruits[1:4]
print(elements)

# Iterate through the list and convert each item to uppercase
for fruit in fruits:
  _fruit = fruit.upper()
  print(_fruit)
