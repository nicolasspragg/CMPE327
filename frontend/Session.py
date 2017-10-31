from Console import Console
userInput = Console()

# control the sessions of users through the use of booleans belonging to class instantiations
class Session:
	accountType = None 
	loggedInUser = False
	loggedInAgent = False
	loggedInGeneral = False

	# called when user enters "login"
	# asks for an account mode and updates the appropriate session variables
	def login(self, testMode):
		loggedInGeneral = self.loggedInGeneral
		if loggedInGeneral == True:
			print("already logged in")
		else:
			accountType = userInput.accountTypeInput(testMode) 
			if(accountType == "atm"):
				print("Logged in user account")
				self.loggedInGeneral = True
				self.loggedInUser = True
			elif(accountType == "agent"):
				print("Logged in teller account")
				self.loggedInGeneral = True
				self.loggedInAgent = True
			else: 
				print("fatal error")

	# called when user enters "logout"
	# sets all the session variables to false and writes to the transaction summary file
	def logout(self, transactionSummary):
		self.accountType = None 
		self.loggedInUser = False
		self.loggedInAgent = False
		self.loggedInGeneral = False
		print("Logging out")
		transactionSummary.write("EOS 0000000 000 0000000 ***\n")


