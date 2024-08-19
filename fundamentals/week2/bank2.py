class BankAccount:
    all_accounts=[]
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0, balance=0): 
      self.int_rate = int_rate
      self.balance=balance
      BankAccount.all_accounts.append(self)
      
    def deposit(self, amount):
      if (self.balance>amount):
        self.balance-=amount
      else:
        print("you don't have this amount")
      
    def withdraw(self, amount):
      self.balance+=amount
    def display_account_info(self):
      print(f"the acount is rate is {self.int_rate} and his balance is {self.balance} ")
    def yield_interest(self):
        self.balance*=(1+self.balance)
    @classmethod
    def All_account(cls):
        for account in cls.all_accounts:
            account.display_account_info() 
            
            
            
            
# class User:
#     accounts=[]
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.accounts.append(BankAccount(int_rate=0.02, balance=1000))
        
    

    
#     def make_deposit(self,amount,nb):
#         self.accounts[nb].deposit(amount)		# we can call the BankAccount instance's methods
    
#     def make_withdraw(self,amount,nb):
#         self.accounts[nb].withdraw(amount)
        
#     def display_user_balance(self,nb):
#         self.accounts[nb].display_account_info()
        
#     def transfert(self,amount,receiver,nb):
#       self.make_deposit(amount)
#       receiver.accounts[nb].withdraw(amount)
      
# User1=User("salah","hizem")
# User1.make_deposit(500,0)
# User1.display_user_balance(0)
# User1.make_withdraw(1000,0)
# User1.display_user_balance(0)

# user2=User("hizem","salah")
# User1.transfert(55,user2,0)

# User1.display_user_balance()
# User1.display_user_balance()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []  # Initialize an empty list for accounts

    def add_account(self, int_rate=0.02, balance=1000):
        new_account = BankAccount(int_rate=int_rate, balance=balance)
        self.accounts.append(new_account)

    def make_deposit(self, amount, nb):
        self.accounts[nb].deposit(amount)

    def make_withdraw(self, amount, nb):
        self.accounts[nb].withdraw(amount)

    def display_user_balance(self, nb):
        self.accounts[nb].display_account_info()

    def transfer(self, amount, receiver, nb):
        if self.accounts[nb].balance>= amount:
            self.make_deposit(amount, nb)
            receiver.make_withdraw(amount, 0)
        else:
            print("Insufficient funds for transfer.")


# Testing the classes
User1 = User("Salah", "salah@example.com")
User1.add_account()  # Add a new account
User1.add_account(int_rate=0.03, balance=5000)  # Add another account with different parameters

User1.make_deposit(500, 0)
User1.display_user_balance(0)  
User1.make_withdraw(1000, 1)  # Withdraw from the second account
User1.display_user_balance(1)  # Output: The account's interest rate is 0.03 and its balance is 4000

User2 = User("Hizem", "hizem@example.com")
User2.add_account(balance=2000)  # Add an account for User2

User1.transfer(300, User2, 0)  # Salah transfers 300 to Hizem's first account
User1.display_user_balance(0)  # Output: The account's interest rate is 0.02 and its balance is 1200
User2.display_user_balance(0)  # Output: The account's interest rate is 0.02 and its balance is 2300