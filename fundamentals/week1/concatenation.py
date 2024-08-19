# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello", name)  # with a comma
print("Hello " + name)  # with a +

# 3. print "Hello 42!" with the number in a variable
number = 42
print("Hello", number)  # with a comma
print("Hello " + str(number))  # with a +  -- converting number to string

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2))  # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.")  # with an f-string





# Summary
# Comma (print("Hello", name)):

# Adds spaces between arguments.
# Handles different data types automatically.
# Plus Sign (print("Hello " + name)):

# Requires explicit conversion to string if concatenating with non-string types.
# Does not add spaces automatically; you need to include them yourself if needed.