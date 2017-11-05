validCommandsList = ['login','logout','create','delete','deposit','withdraw','transfer']

class Validity:

	validCommand = None
	validAccountNumber = None
	validAmount = None
	validAccountName = None
	machineState = True # machine mode 

	#checks if command being tried is valid
	def checkCommand(self, command):
		global validCommandsList
		if command in validCommandsList:
			return True
		else:
			# print("invalid command")
			return False

	# check if accountNumber is valid
	def checkAccountNumber(self,accountNumber):
		numDigits = len(str((accountNumber)))
		zerothDigit = str(accountNumber[0])
		if(numDigits > 7):
			print("Error: Account number too long")
			return False
		elif(numDigits < 7):
			print("Error: Account number too short")
			return False
		elif(zerothDigit == "0"):
			print("Error: Account number can't start with 0")
			return False
		else:
			return True

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
		

#broken
	def checkAccountName(self,accountName):
		if(accountName.isalnum() == False or len(accountName) > 30 or len(accountName) < 3 or accountName.startswith(" ") or accountName.endswith(" ")):
			print("Invalid  name")
			self.validAccountName = False
		else:
			print("Valid name")
			self.validAccountName = True














