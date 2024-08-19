# Variable Declaration
my_new_favorite_language = 'Python'  # variable declaration, initialize string

# Log Statement
print("Hello, World!")  # log statement

# Type Check
print(type(my_new_favorite_language))  # type check

# Length Check
print(len(my_new_favorite_language))  # length check

# Comments
# Single line comment
# This is a single line comment

# Multiline comment
"""
This is
a multiline
comment
"""

# Data Types
## Primitive
### Boolean
is_python_fun = True  # boolean

### Numbers
my_favorite_number = 42  # number

### Strings
my_greeting = "Hello"  # string

## Composite
### List
#### Initialize
my_list = [1, 2, 3, 4, 5]  # list initialization

#### Access Value
print(my_list[2])  # access value

#### Change Value
my_list[2] = 10  # change value

#### Add Value
my_list.append(6)  # add value

#### Delete Value
del my_list[2]  # delete value

### Tuples
#### Initialize
my_tuple = (1, 2, 3, 4, 5)  # tuple initialization

#### Access Value
print(my_tuple[2])  # access value

#### Change Value
# tuples are immutable, this will cause a TypeError

#### Add Value
 # tuples are immutable, this will cause an AttributeError

#### Delete Value
 # tuples are immutable, this will cause a TypeError

### Dictionary
#### Initialize
my_dict = {'name': 'Alice', 'age': 25}  # dictionary initialization

#### Access Value
print(my_dict['name'])  # access value

#### Change Value
my_dict['age'] = 26  # change value

#### Add Value
my_dict['city'] = 'New York'  # add value

#### Delete Value
del my_dict['age']  # delete value

# Conditionals
if my_new_favorite_language == 'Python':
    print("You're using Python!")  # if statement
elif my_new_favorite_language == 'JavaScript':
    print("You're using JavaScript!")  # else if statement
else:
    print("You're using another language!")  # else statement

# For Loop
for i in range(5):  # start, stop, increment
    print(i)  # sequence

for i in range(5):
    if i == 2:
        break  # break statement
    print(i)

for i in range(5):
    if i == 2:
        continue  # continue statement
    print(i)

# While Loop
count = 0
while count < 5:  # start
    print(count)
    count += 1  # stop, increment

# Function
def greet(name):  # parameter
    return f"Hello, {name}!"  # return statement

print(greet("Salah"))  # argument

# Bonus: Errors
# NameError: name <variable name> is not defined
# print(non_existent_variable)

# TypeError: 'tuple' object does not support item assignment
# my_tuple[2] = 10

# KeyError: 'favorite_team'
# print(my_dict['favorite_team'])

# IndexError: list index out of range
# print(my_list[10])

# IndentationError: unexpected indent
#   print("Indentation error")

# AttributeError: 'tuple' object has no attribute 'pop'
my_tuple.pop()

# AttributeError: 'tuple' object has no attribute 'append'
my_tuple.append(6)

# Tuples
## Change Value
my_tuple[1] = 20  # This will raise a TypeError because tuples are immutable

## Add Value
my_tuple += (6,)  # This creates a new tuple with the added value

## Delete Value
del my_tuple[1]  # This will raise a TypeError because tuples are immutable
