
class Validity:

validCommandsList = ['login','logout','createacct','deleteacct','deposit','withdraw','transfer']
validCommand = None
validAccountNumber = None
validAmount = None
validAccountName = None
machineState = True # machine mode 


	def __init__(self):
		self.validCommand = validCommand
		self.validAccountNumber = validAccountNumber
		self.validAmount = validAmount
		self.machineState = machineState
		self.validAccountName = validAccountName



	#checks if command being tried is valid
	def checkCommandValid(command,validCommandsList):
		if command in validCommandsList:
			print("valid command")
			validCommand = true
		else:
			validCommand = false


	# check if accountNumber is valid
	def checkAccountNumber(accountNumber):
		numDigits = len(str(abs(num)))
		zerothDigit = str(accountNumber[0])
		if(numDigits > 7 or numDigits < 7):
			validAccount = False
		elif(zerothDigit = 0):
			validAccountNumber = False
		else:
			validAccountNumber = True

    #check if amount is valid
	def checkAmount(amount, machineState):
		if(machineState):
			if(amount < 0 or amount > 100000):
				validAmount = False
		if(!machineState):
			if(amount < 0 or amount > 99999999):
				validAmount = False
		else:
			validAmount = True


	def checkAccountName(accountName):
		if(accountName.isalnum() == False or len(accountName) > 30 or len(accountName) <  or accountName.startwith(" ") or accountName.endswith(" ")):
			validAccountName = False
		else:
			validAccountName = True














