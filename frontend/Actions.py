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
				print "Error: illegal action"
		else:
			print "Error: Not logged in"
	# delete an account (teller mode only)
	def delete(self, session, transactionSummary, testMode):
		if session.loggedInGeneral == True:
			if session.loggedInAgent == True:
				accountNumber = userInput.accountNumberInput(testMode)
				accountName = userInput.accountNameInput(testMode)
				print("Deleted account " + accountNumber + " " + accountName)
				transactionSummary.write("DEL " + accountNumber + " 000 0000000 " + accountName + "\n")
			else:
				print "Error: illegal action"
		else:
			print "Error: Not logged in"
	# deposit an amount to an account
	def deposit(self, session, transactionSummary, testMode):
		if session.loggedInGeneral == True:
			accountNumber = userInput.accountNumberInput(testMode)
			amount = userInput.amountInput(testMode)
			print("Depositing $" + amount + "into" + accountNumber)
			transactionSummary.write("DEP " + accountNumber + " " + amount+" 0000000 ***\n")
		else:
			print "Error: Not logged in"
	# withdraw an amount from an account
	def withdraw(self, session, transactionSummary, testMode):
		if session.loggedInGeneral == True:
			accountNumber = userInput.accountNumberInput(testMode)
			amount = userInput.amountInput(testMode)
			print("Withdrawing $" +amount+ " from " +accountNumber)
			transactionSummary.write("WDR " + accountNumber + " " + amount + " 0000000 ***\n")
		else:
			print "Error: Not logged in"
	# transfer an amount between two accounts
	def transfer(self, session, transactionSummary, testMode):
		if session.loggedInGeneral == True:
			fromAccountNumber = userInput.fromAccountNumberInput(testMode)
			toAccountNumber = userInput.toAccountNumberInput(testMode)
			amount = userInput.amountInput(testMode)
			print("Transferring $" + amount +" "+ "from " + fromAccountNumber +"to " + toAccountNumber )
			transactionSummary.write("XFR " + fromAccountNumber + " " + amount + " " + toAccountNumber + " ***\n")
		else:
			print "Error: Not logged in"
