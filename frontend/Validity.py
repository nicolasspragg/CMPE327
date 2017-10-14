
class Validity:

	validCommandsList = ['login','logout','createacct','deleteacct','deposit','withdraw','transfer']
	validCommand = None
	validAccountNumber = None
	validAmount = None
	validAccountName = None
	machineState = True # machine mode 




	#checks if command being tried is valid
	def checkCommandValid(self,command,validCommandsList):
		if command in validCommandsList:
			print("valid command")
			self.validCommand = True
		else:
			print("invalid command")
			self.validCommand = False


	# check if accountNumber is valid
	def checkAccountNumber(self,accountNumber):
		numDigits = len(str(abs(num)))
		zerothDigit = str(accountNumber[0])
		if(numDigits > 7 or numDigits < 7):
			self.validAccount = False
		elif(zerothDigit == 0):
			self.validAccountNumber = False
		else:
			self.validAccountNumber = True

    #check if amount is valid
	def checkAmount(self,amount, machineState):
		if(machineState):
			if(amount < 0 or amount > 100000):
				self.validAmount = False
		if(machineState == False):
			if(amount < 0 or amount > 99999999):
				self.validAmount = False
		else:
			self.validAmount = True


	def checkAccountName(self,accountName):
		if(accountName.isalnum() == False or len(accountName) > 30 or len(accountName) < 3 or accountName.startwith(" ") or accountName.endswith(" ")):
			self.validAccountName = False
		else:
			self.validAccountName = True














