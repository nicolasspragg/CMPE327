from Console import Console
userInput = Console()

class Session:
	accountType = None 
	loggedInUser = False
	loggedInAgent = False
	loggedInGeneral = False

	#login function
	def login(self):
		loggedInGeneral = self.loggedInGeneral
		if(loggedInGeneral == True):
			print("already logged in")
		else:
			accountType = userInput.accountTypeInput() 
			if(accountType == "atm"):
				print("logged in user Mode")
				self.loggedInGeneral = True
				self.loggedInUser = True
			elif(accountType == "agent"):
				print("logged in teller mode")
				self.loggedInGeneral = True
				self.loggedInAgent = True
			else: 
				print("fatal error")

	def logout(self):
		self.accountType = None 
		self.loggedInUser = False
		self.loggedInAgent = False
		self.loggedInGeneral = False


