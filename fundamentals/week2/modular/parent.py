local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"
# in the same file, add the following below the User class
print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())

print(__name__)
# it gives you the name of the  file withour extension .py

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)

print(local_val)
  
