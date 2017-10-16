
class Validity:

	validCommandsList = ['login','logout','createacct','deleteacct','deposit','withdraw','transfer']
	validCommand = None
	validAccountNumber = None
	validAmount = None
	validAccountName = None
	machineState = True # machine mode 




	#checks if command being tried is valid
	def checkCommand(self,command,validCommandsList):
		if command in validCommandsList:
			print("valid command")
			self.validCommand = True
		else:
			print("invalid command")
			self.validCommand = False


	# check if accountNumber is valid
	def checkAccountNumber(self,accountNumber):
		numDigits = len(str((accountNumber)))
		zerothDigit = str(accountNumber[0])
		if(numDigits > 7 or numDigits < 7):
			print("invalid account number")
			self.validAccount = False
		elif(zerothDigit == 0):
			print("invalid account number")
			self.validAccountNumber = False
		else:
			print("valid account number")
			self.validAccountNumber = True

    #check if amount is valid
    #this is currently broken
	def checkAmount(self,amount, machineState):
		if(machineState == True):
			if(amount < 0 or amount > 100000):
				self.validAmount = False
				print("invalid amount1")
			else:
				print("valid amount2")
				self.validAmount = True
		elif(machineState == False):
			if(amount < 0 or amount > 99999999):
				print("invalid amount3")
				self.validAmount = False
			else:
				print("valid Amount4")
				self.validAmount = True
		else:
			print("fatal error")
		


	def checkAccountName(self,accountName):
		if(accountName.isalnum() == False or len(accountName) > 30 or len(accountName) < 3 or accountName.startswith(" ") or accountName.endswith(" ")):
			print("Invalid  name")
			self.validAccountName = False
		else:
			print("Valid name")
			self.validAccountName = True














