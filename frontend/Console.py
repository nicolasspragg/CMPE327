# read in commands from user/file in future
class Console:
	command = None
	accountNumber = None
	amount = None
	accountName = None

	def commandInput(self):
		
		commandIn = raw_input(("Command:"))
		self.command = commandIn
		return self.command

	def accountNumberInput(self):
		accountNumberIn = raw_input(("Account number "))
		self.accountNumber = accountNumberIn
		return self.accountNumber

	def amountIn(self):
		amountIn = raw_input(("amount:"))
		self.amount = amountIn
		return self.amount

	def accountNameInput(self):
		accountNameIn = raw_input(("Account name:"))
		self.accountName = accountNameIn
		return self.accountName


		




