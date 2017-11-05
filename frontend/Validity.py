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
	def checkAccountNumber(self,accountNumber, type):
		numDigits = len(str((accountNumber)))
		zerothDigit = str(accountNumber[0])
		if(numDigits > 7):
			print("Error: " + type + "Account number too long")
			return False
		elif(numDigits < 7):
			print("Error: " + type + "Account number too short")
			return False
		elif(zerothDigit == "0"):
			print("Error: " + type + "Account number can't start with 0")
			return False
		else:
			return True

    #check if amount is valid
    #this is currently broken
	def checkAmount(self,amount, session):
		if(session.loggedInUser == True):
			if(int(amount) < 0):
				print("Error: Can't use negative number")
				return False
			elif(int(amount) > 100000):
				print("Error: Max allowed is $1,000")
				return False
			else:
				return True
		else:
			if(int(amount) < 0):
				print("Error: Can't use negative number")
				return False
			elif(int(amount) > 99999999):
				print("Error: Max allowed is $999,999.99")
				return False
			else:
				# print("valid Amount4")
				return True

#broken
	def checkAccountName(self,accountName):
		if(accountName.isalnum() == False or len(accountName) > 30 or len(accountName) < 3 or accountName.startswith(" ") or accountName.endswith(" ")):
			print("Invalid  name")
			self.validAccountName = False
		else:
			print("Valid name")
			self.validAccountName = True














