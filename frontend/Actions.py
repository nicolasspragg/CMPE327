from Session import Session
from Console import Console
userInput = Console()

# implementations of all possible actions a logged-in user can perform
# these methods write to the transaction summary file
class Actions:
	# create an account (teller mode only)
	def create(self, session, transactionSummary, accountsList, testMode):
		if session.loggedInGeneral == True:
			if session.loggedInAgent == True:
				accountNumber = userInput.accountNumberInput(testMode)
				accountName = userInput.accountNameInput(testMode)
				if (int(accountNumber) in accountsList):
					print("Error: account already exists")
				else:
					print("Creating account " + accountNumber)
					transactionSummary.write("NEW " + accountNumber + " 000 0000000 " + accountName + "\n")	
			else:
				print "Error: illegal action"
		else:
			print "Error: Not logged in"
	# delete an account (teller mode only)
	def delete(self, session, transactionSummary, accountsList, testMode):
		if session.loggedInGeneral == True:
			if session.loggedInAgent == True:
				accountNumber = userInput.accountNumberInput(testMode)
				accountName = userInput.accountNameInput(testMode)
				if (int(accountNumber) in accountsList):
					print("Deleted account " + accountNumber + " " + accountName)
					transactionSummary.write("DEL " + accountNumber + " 000 0000000 " + accountName + "\n")
				else:
					print("Error: Invalid account number")
			else:
				print "Error: illegal action"
		else:
			print "Error: Not logged in"
	# deposit an amount to an account
	def deposit(self, session, transactionSummary, testMode):
		if session.loggedInGeneral == True:
			accountNumber = userInput.accountNumberInput(testMode)
			amount = userInput.amountInput(testMode)
			print("Depositing $" + str(int(amount)/100) + " into " + accountNumber)
			transactionSummary.write("DEP " + accountNumber + " " + amount+" 0000000 ***\n")
		else:
			print "Error: Not logged in"
	# withdraw an amount from an account
	def withdraw(self, session, transactionSummary, accountNumber, amount, totalAmount, testMode):
		if session.loggedInGeneral == True:
			# totalAmount += int(amount)
			if (session.loggedInUser == True and totalAmount > 100000):
				# machine mode has a max withdrawal of $1000
				print("Error: Max amount already withdrawn ($1000)")
			else:
				print("Withdrawing $" + str(int(amount)/100) + " from " + accountNumber)
				transactionSummary.write("WDR " + accountNumber + " " + amount + " 0000000 ***\n")
		else:
			print "Error: Not logged in"
	# transfer an amount between two accounts
	def transfer(self, session, transactionSummary, testMode):
		if session.loggedInGeneral == True:
			fromAccountNumber = userInput.fromAccountNumberInput(testMode)
			toAccountNumber = userInput.toAccountNumberInput(testMode)
			amount = userInput.amountInput(testMode)
			print("Transferring $" + str(int(amount)/100) + " from " + fromAccountNumber +" to " + toAccountNumber )
			transactionSummary.write("XFR " + fromAccountNumber + " " + amount + " " + toAccountNumber + " ***\n")
		else:
			print "Error: Not logged in"
