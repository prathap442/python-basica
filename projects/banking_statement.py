import pdb
class Account():
  def __init__(self,**kwargs):
    for (key,value) in kwargs.items(): 
      setattr(self,key,value)
    self.amount = self.account_amount
    self.min_balance = self.account_min_balance
    self.bank = self.bank_name

  def deposit(self,amount):
    self.account_amount += amount


class Savings(Account):
  def __init__(self, bank_name="LVB"):
    self.account_type = "savings"
    self.bank_name = bank_name
    account_data = {
      "account_amount": 1000,
      "account_min_balance": 2000,
      "bank": bank_name
    }
    super().__init__(**account_data)
    
  def account_analogy(self):
    print('the account amount:{} minbalance:{}'.format(self.amount,self.min_balance))

  def with_draw(self,amount):
    if(self.account_amount-int(amount) > self.account_min_balance):
      self.account_amount = (int(self.account_amount) - int(amount))
      print('Yeah you can with draw the amount {}'.format(amount))
    else:
      print('No you cannot with draw since you need to maintain the min balance of {self.account_min_balance}')

  # this is the destructor method in python3
  def __del__(self):
    print('Account is closed and blocked')

pdb.set_trace()

 