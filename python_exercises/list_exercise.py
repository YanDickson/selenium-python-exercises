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

# Iterate through the list and convert each item to uppercase
for fruit in fruits:
  _fruit = fruit.upper()
  print(_fruit)
