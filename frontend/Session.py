class Session:
	accountType = None 
	loggedInUser = False
	loggedInAgent = False
	loggedInGeneral = False

	#login function
	def login(self,accountType):
		loggedInGeneral = self.loggedInGeneral
		if(loggedInGeneral == True):
			print("already logged in")
		elif(accountType == "user"):
			print("logged in User Mode")
			self.loggedInGeneral = True
			self.loggedInUser = True
		elif(accountType == "teller"):
			print("logged in Agent mode")
			self.loggedInGeneral = True
			self.loggedInAgent = True
		else: 
			print("fatal error")


