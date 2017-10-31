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
	def commandInput(self, testMode):
		if testMode == False:
			commandIn = raw_input(("Command:"))
		else:
			commandIn = raw_input()
		self.command = commandIn
		return self.command

	# returns an account number
	def accountNumberInput(self, testMode):
		if testMode == False:
			accountNumberIn = raw_input(("Account number:"))
		else:
			accountNumberIn = raw_input()
		self.accountNumber = accountNumberIn
		return self.accountNumber
	
	# returns a from account number (for transfers)
	def fromAccountNumberInput(self, testMode):
		if testMode == False:
			accountNumberIn = raw_input(("Account number (from):"))
		else:
			accountNumberIn = raw_input()
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
	def accountNameInput(self, testMode):
		if testMode == False:
			accountNameIn = raw_input(("Account name:"))
		else:
			accountNameIn = raw_input()
		self.accountName = accountNameIn
		return self.accountName

	# returns an account type (for logins)
	def accountTypeInput(self, testMode):
		if testMode == False:
			accountTypeIn = raw_input(("Account type:"))
		else:
			accountTypeIn = raw_input()
		self.accountType = accountTypeIn
		return self.accountType



		




