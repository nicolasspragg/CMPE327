from Session import Session
from Console import Console
userInput = Console()

class Actions:
	def create(self, session, transactionSummary):
		if session.loggedInGeneral == True:
			if session.loggedInAgent == True:
				accountNumber = userInput.accountNumberInput()
				accountName = userInput.accountNameInput()
				transactionSummary.write("NEW " + accountNumber + " 000 0000000 " + accountName + "\n")
			else:
				print "no permissions"
		else:
			print "not logged in"
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
	def deposit(self, session, transactionSummary):
		if session.loggedInGeneral == True:
			accountNumber = userInput.accountNumberInput()
			amount = userInput.amountInput()
			transactionSummary.write("DEP " + accountNumber + " " + amount + " 0000000 ***\n")
		else:
			print "not logged in"
	def withdraw(self, session, transactionSummary):
		if session.loggedInGeneral == True:
			accountNumber = userInput.accountNumberInput()
			amount = userInput.amountInput()
			transactionSummary.write("WDR " + accountNumber + " " + amount + " 0000000 ***\n")
		else:
			print "not logged in"
	def transfer(self, session, transactionSummary):
		if session.loggedInGeneral == True:
			fromAccountNumber = userInput.fromAccountNumberInput()
			toAccountNumber = userInput.toAccountNumberInput()
			amount = userInput.amountInput()
			transactionSummary.write("XFR " + fromAccountNumber + " " + amount + " " + toAccountNumber + " ***\n")
		else:
			print "not logged in"
