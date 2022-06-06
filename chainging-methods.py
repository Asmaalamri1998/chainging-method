class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposite(self,amount):
        self.account_balance+=amount
        return self
   
    def make_withdrawal(self, amount):
        self.account_balance-=amount
        return self


    def display_user_balance(self):

       print(f"the name of the user is {self.name} and the account balance is {self.account_balance}")
       return self

    def transfer_money(self, other_user, amount):
        other_user.account_balance+=amount
        self.account_balance-=amount
        return self

mohammed=User("Mohammed","mohammed@gmail.com")
asma= User("Asma", "Asma@gmail.com")
lateen= User("lateen","lateem@gmail.com")

asma.make_deposite(5000).make_deposite(2000).make_withdrawal(1000).make_withdrawal(500).transfer_money(lateen,1000).display_user_balance()

lateen.make_deposite(1000).make_withdrawal(1000).display_user_balance()

