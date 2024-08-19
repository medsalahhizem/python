class BankAccount:
    all_accounts=[]
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.01, balance=0): 
      self.int_rate = int_rate
      self.balance=balance
      BankAccount.all_accounts.append(self)
      
    def deposit(self, amount):
      if (self.balance>amount):
        self.balance+=amount
      else:
        print("you don't have this amount")
      
    def withdraw(self, amount):
        if (self.balance>amount):
         self.balance-=amount
        else:
          print( "Insufficient funds: Charging a $5 fee")
          if (self.balance>5):
           self.balance-=5
          else:
           print(f"we charged you with{self.balance}and you have to pay the rest ")
           
        
    def display_account_info(self):
      print(f"the acount is rate is {self.int_rate} and his balance is {self.balance} ")
      
    def yield_interest(self):
        self.balance*=(1+self.balance)
    @classmethod
    def All_account(cls):
        for account in cls.all_accounts:
            account.display_account_info()
    

user1=BankAccount(0.1,100)
user2=BankAccount(0.2,500)

user1.deposit(50)
user1.display_account_info()
user1.withdraw(100)
user1.display_account_info()
user1.yield_interest()
user1.display_account_info()

user2.display_account_info()
user2.deposit(1000)

user3=BankAccount(0.2,1000)

print("using the method class to print all instances of a Bank Account's info")
BankAccount.All_account()