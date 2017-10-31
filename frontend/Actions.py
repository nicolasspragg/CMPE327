from Session import Session
from Console import Console
userInput = Console()

# implementations of all possible actions a logged-in user can perform
# these methods write to the transaction summary file
class Actions:
	# create an account (teller mode only)
	def create(self, session, transactionSummary, testMode):
		if session.loggedInGeneral == True:
			if session.loggedInAgent == True:
				accountNumber = userInput.accountNumberInput(testMode)
				accountName = userInput.accountNameInput(testMode)
				print("Creating account " + accountNumber)
				transactionSummary.write("NEW " + accountNumber + " 000 0000000 " + accountName + "\n")
			else:
				print "no permissions"
		else:
			print "not logged in"
	# delete an account (teller mode only)
	def delete(self, session, transactionSummary):
		if session.loggedInGeneral == True:
			if session.loggedInAgent == True:
				accountNumber = userInput.accountNumberInput()
				accountName = userInput.accountNameInput()
				transactionSummary.write("DEL " + accountNumber + " 000 0000000 " + accountName + "\n")
			else:
				print "no permissions"
		else:
			print "not logged in"
	# deposit an amount to an account
	def deposit(self, session, transactionSummary):
		if session.loggedInGeneral == True:
			accountNumber = userInput.accountNumberInput()
			amount = userInput.amountInput()
			transactionSummary.write("DEP " + accountNumber + " " + amount + " 0000000 ***\n")
		else:
			print "not logged in"
	# withdraw an amount from an account
	def withdraw(self, session, transactionSummary):
		if session.loggedInGeneral == True:
			accountNumber = userInput.accountNumberInput()
			amount = userInput.amountInput()
			transactionSummary.write("WDR " + accountNumber + " " + amount + " 0000000 ***\n")
		else:
			print "not logged in"
	# transfer an amount between two accounts
	def transfer(self, session, transactionSummary):
		if session.loggedInGeneral == True:
			fromAccountNumber = userInput.fromAccountNumberInput()
			toAccountNumber = userInput.toAccountNumberInput()
			amount = userInput.amountInput()
			transactionSummary.write("XFR " + fromAccountNumber + " " + amount + " " + toAccountNumber + " ***\n")
		else:
			print "not logged in"
