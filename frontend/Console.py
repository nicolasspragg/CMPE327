from Validity import Validity

enforcer = Validity()

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
		global enforcer
		if testMode == False:
			commandIn = raw_input(("Command:"))
		else:
			commandIn = raw_input()
		if (enforcer.checkCommand(commandIn) == True):
			self.command = commandIn
			return self.command
		else:
			return "ignore"

	# returns an account number
	def accountNumberInput(self, testMode):
		global enforcer
		if testMode == False:
			accountNumberIn = raw_input(("Account number:"))
		else:
			accountNumberIn = raw_input()
		if (enforcer.checkAccountNumber(accountNumberIn) == True):
			self.accountNumber = accountNumberIn
			return self.accountNumber
		else:
			return "ignore"
	
	# returns a from account number (for transfers)
	def fromAccountNumberInput(self, testMode):
		global enforcer
		if testMode == False:
			accountNumberIn = raw_input(("Account number (from):"))
		else:
			accountNumberIn = raw_input()
		if (enforcer.checkAccountNumber(accountNumberIn) == True):
			self.accountNumber = accountNumberIn
			return self.accountNumber
		else:
			return "ignore"
	
	# returns a to account number (for transfers)
	def toAccountNumberInput(self, testMode):
		global enforcer
		if testMode == False:
			accountNumberIn = raw_input(("Account number (to):"))
		else:
			accountNumberIn = raw_input()
		if (enforcer.checkAccountNumber(accountNumberIn) == True):
			self.accountNumber = accountNumberIn
			return self.accountNumber
		else:
			return "ignore"

	# returns a transaction amount
	def amountInput(self, testMode):
		if testMode == False:
			amountIn = raw_input(("amount:"))
		else:
			amountIn = raw_input()
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



		




