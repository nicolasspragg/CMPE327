# read in commands from user/file in future
class Console:
	command = None
	accountNumber = None
	fromAccountNumber = None
	toAccountNumber = None
	amount = None
	accountName = None
	accountType = None

	def commandInput(self):
		
		commandIn = raw_input(("Command:"))
		self.command = commandIn
		return self.command

	def accountNumberInput(self):
		accountNumberIn = raw_input(("Account number:"))
		self.accountNumber = accountNumberIn
		return self.accountNumber
	
	def fromAccountNumberInput(self):
		accountNumberIn = raw_input(("Account number (from):"))
		self.fromAccountNumber = accountNumberIn
		return self.fromAccountNumber
	
	def toAccountNumberInput(self):
		accountNumberIn = raw_input(("Account number (to):"))
		self.toAccountNumber = accountNumberIn
		return self.toAccountNumber

	def amountInput(self):
		amountIn = raw_input(("amount:"))
		self.amount = amountIn
		return self.amount

	def accountNameInput(self):
		accountNameIn = raw_input(("Account name:"))
		self.accountName = accountNameIn
		return self.accountName

	def accountTypeInput(self):
		accountTypeIn = raw_input(("Account type:"))
		self.accountType = accountTypeIn
		return self.accountType



		




