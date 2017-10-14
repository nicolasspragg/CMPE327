
class Validity:

validCommandsList = ['login','logout','createacct','deleteacct','deposit','withdraw','transfer']
validCommand = None
validAccountNumber = None
validAmount = None
machineState = true # machine mode 

	def __init__(self):
		self.validCommand = validCommand
		self.validAccountNumber = validAccountNumber
		self.validAmount = validAmount
		self.machineState = machineState



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
			validAccount = false
		elif(zerothDigit = 0):
			validAccountNumber = false
		else:
			validAccountNumber = true


	def checkAmount(amount, machineState):
		if(machineState):
			if(amount < 0 or amount > 100000):
				validAmount = false
		if(!machineState):
			if(amount < 0 or amount > 99999999):
				validAmount = false
		else:
			validAmount = true














