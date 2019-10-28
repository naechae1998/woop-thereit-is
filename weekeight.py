class bankaccount:

	def __init__(self,account_number,balance):
		self.account_number = account_number
		self.balance =float(balance)

	def deposit(self,amount):
		amount = float(input("what do you want to deposit?"))
		self.balance += amount
		return self.balance
	def withdraw(self,amount):
		if amount <= self.balance:
			self.balance -= amount
		else:
			print("insufficient funds")
			return self.balance
    
    
class checking(bankaccount):
	
	def __init__(self,account_number,balance,minbal,fees):
		bankaccount.__init__(self, acount_number,balance)
		self.fee = fees
		self.minbal = minbal
		print("your prepaid acount is ready to be set up")
		print("the fee for this account is $"+ self.fee +"\n the minimum balance is $" + self.minbal)
		
	def deposit(self): 
		amount = float(input("Enter amount to be deposited: "))
		self.balance += amount
		print("\n Amount Deposited:", amount)
	def withdrawal(self, amount,):
		if self.balance - amount-5>=50:
			self.balance -= amount
			return amount
		else:
			return 'Your withdrawal amount is ${} which exceeds you acountfunds You have:' \
                   '\n${} '.format(amount, self.balance, limit)

class savings(bankaccount):
	def deposit(self): 
		amount = float(input("Enter amount to be deposited: "))
		self.balance += amount
		print("\n Amount Deposited:", amount)
		print(amount*0.02)
		

print("welcome to ALTUVE bank!")
userinput= input("Press 1 to open an acoount ")
if userinput  is 1:
 mybankacount=bankaccount(self,account_number,balance, amount)
 print (mybankacount)
