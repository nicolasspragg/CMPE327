# utility methods to read in commands/inputs from users
class Console:
	# transaction variables
	command = None
	accountNumber = None
	fromAccountNumber = None
	toAccountNumber = None
	amount = None
	accountName = None
	accountType = None

	# returns a general command
	def commandInput(self):
		commandIn = raw_input(("Command:"))
		self.command = commandIn
		return self.command

	# returns an account number
	def accountNumberInput(self):
		accountNumberIn = raw_input(("Account number:"))
		self.accountNumber = accountNumberIn
		return self.accountNumber
	
	# returns a from account number (for transfers)
	def fromAccountNumberInput(self):
		accountNumberIn = raw_input(("Account number (from):"))
		self.fromAccountNumber = accountNumberIn
		return self.fromAccountNumber
	
	# returns a to account number (for transfers)
	def toAccountNumberInput(self):
		accountNumberIn = raw_input(("Account number (to):"))
		self.toAccountNumber = accountNumberIn
		return self.toAccountNumber

	# returns a transaction amount
	def amountInput(self):
		amountIn = raw_input(("amount:"))
		self.amount = amountIn
		return self.amount

	# returns an account name
	def accountNameInput(self):
		accountNameIn = raw_input(("Account name:"))
		self.accountName = accountNameIn
		return self.accountName

	# returns an account type (for logins)
	def accountTypeInput(self):
		accountTypeIn = raw_input(("Account type:"))
		self.accountType = accountTypeIn
		return self.accountType



		




