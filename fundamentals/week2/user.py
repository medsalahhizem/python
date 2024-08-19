class User:		
    def __init__(self,first_name,last_name,age,is_rewards_member=False,gold_card_points=0):
        self.first_name =first_name
        self.last_name = last_name 
        self.age = age
        self.is_rewards_member =is_rewards_member 
        self.gold_card_points=gold_card_points

def display_info(self):
  print(f"user is {self.first_name} {self.last_name}.He is{self.age} years old.The information about getting his reward is {self.is_rewards_member}.He has  {self.gold_card_points} gold card points .")
x=User("salah","hizem",5,False,5)
display_info(x)

def enroll(self):
  self.is_rewards_member=True
  self.gold_card_points=200
enroll(x)
display_info(x)

def spend_points(self, amount):
  self.gold_card_points+=amount
spend_points(x,200)
display_info(x)




print ("the second method with chaining")
class User:		
    def __init__(self, first_name, last_name, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age
        self.is_rewards_member = is_rewards_member 
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(f"User is {self.first_name} {self.last_name}. He is {self.age} years old. The information about getting his reward is {self.is_rewards_member}. He has {self.gold_card_points} gold card points.")
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self
X = User("Salah", "Hizem", 5, False, 5)
X.display_info().enroll().spend_points(50).display_info()
