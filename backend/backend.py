import sys, os, copy

#global variables

currentValidAccountList = None
transactionSummary = None
currentMasterAccountsList = None
newMasterAccountsFile = None
newValidAccountsFile = []
numToNameMap = {}
accToAmountMap = {}
recentlyCreated = []
recentlyDeleted = []

def loadValidAccountList():
	global currentValidAccountList
	currentValidAccountListFile = sys.argv[1]
	currentValidAccountList = open(currentValidAccountListFile, 'r').readlines()
	currentValidAccountList = map(str.rstrip, currentValidAccountList)
	newValidAccountsFile = currentValidAccountList[:]


def loadCurrentMasterAccountsList():
	global currentMasterAccountsList, newMasterAccountsFile
	currentMasterAccountsListFile = sys.argv[2]
	currentMasterAccountsList = open(currentMasterAccountsListFile, 'r').readlines()
	currentMasterAccountsList = map(str.rstrip, currentMasterAccountsList)
	newMasterAccountsFile = currentMasterAccountsList[:]

def loadTransActionSummary():
	global transactionSummary
	transactionSummaryFile = sys.argv[3]
	transactionSummary = open(transactionSummaryFile, 'r').readlines()
	transactionSummary = map(str.rstrip, transactionSummary)

def parseTransactionSummary(): 
	global transactionSummary


	for item in transactionSummary:
		action = item.split()[0]
		accountNumInTs = item.split()[1]
		amount = item.split()[2]
		accountToNumber = item.split()[3]
		accountName = item.split()[4]

		if(action == "NEW"):
			#call create handler
			handleCreate(accountNumInTs, accountName)
		elif(action == "DEL"): 
			#call delete handler
			handleDelete(accountNumInTs, accountName)
		elif(action == "DEP"):
			#call deposit handler
			handleDeposit(accountNumInTs, amount)
		elif(action == "WDR"):
			#call withdraw handler
			handleWithdraw(accountNumInTs, amount)
		elif(action == "XFR"):
			#call transfer handler
			handleTransfer()
		elif(action == "EOS"):
			#end of file 
			return

def handleCreate(accountNumInTs, accountName):
	global recentlyCreated, currentValidAccountList, currentMasterAccountsList, newMasterAccountsFile, newValidAccountsFile, recentlyDeleted
	if(accountNumInTs in newMasterAccountsFile or accountNumInTs in recentlyCreated or accountNumInTs in recentlyDeleted):
		#failure
		print("not unique")
		return
	else:
		#add to lists
		newValidAccountsFile.append(int(accountNumInTs))
		newMasterAccountsFile.append(accountNumInTs + " 000 " + accountName)
		recentlyCreated.append(accountNumInTs)

		

def handleDelete(accountNumInTs, accountName):
	global recentlyCreated, recentlyDeleted, currentValidAccountList, currentMasterAccountsList, newMasterAccountsFile, newValidAccountsFile,numToNameMap, accToAmountMap
	name = numToNameMap[accountNumInTs]
	name = name.strip()
	accountName = accountName.strip()
	
	if(name != accountName):
		print("Not a match ")
		return
		
	else:
		amountInAccount = accToAmountMap[accountNumInTs]
		if (int(amountInAccount) == 000):
			#can delete
			newMasterAccountsFile.remove(accountNumInTs + " 000 " +accountName)
			try:
				recentlyCreated.remove(accountNumInTs)
			except ValueError:
				pass
			recentlyDeleted.append(accountNumInTs)
			mapAccountNumToAmount()
			#print newMasterAccountsFile
			#print recentlyCreated
			#print recentlyDeleted
		else:
			#print("account must have no funds")
			return 



def handleDeposit(accountNumInTs, amount):
	global recentlyCreated, recentlyDeleted, currentValidAccountList, currentMasterAccountsList, newMasterAccountsFile, newValidAccountsFile,numToNameMap, accToAmountMap
	print accToAmountMap
	if(accountNumInTs not in recentlyDeleted):
		name = numToNameMap[accountNumInTs]
		oldAmount = accToAmountMap[accountNumInTs]
		index = newMasterAccountsFile.index(accountNumInTs + " " + oldAmount + " " + name)

		amount = int(amount)
		oldAmount = int(oldAmount)

		amount += oldAmount

		amount = str(amount)


		newMasterAccountsFile[index] = (accountNumInTs +" " + amount + " " + name)
		mapAccountNumToAmount()
		print newMasterAccountsFile
	else:
		print("account has been deleted can't deposit")
		return


def handleWithdraw(accountNumInTs, amount):
	global recentlyCreated, recentlyDeleted, currentValidAccountList, currentMasterAccountsList, newMasterAccountsFile, newValidAccountsFile,numToNameMap, accToAmountMap

	if(accountNumInTs not in recentlyDeleted):
		name = numToNameMap[accountNumInTs]
		oldAmount = accToAmountMap[accountNumInTs]
		index = newMasterAccountsFile.index(accountNumInTs + " " + oldAmount + " " + name)

		amount = int(amount)
		oldAmount = int(oldAmount)
		print amount
		print oldAmount

		amount = oldAmount - amount

		if(amount < 0):
			print("can't make account negative")
			return
		else:
			amount = str(amount)
			newMasterAccountsFile[index] = (accountNumInTs +" " + amount + " " + name)
			mapAccountNumToAmount()
	else:
		print("account has been deleted can't withdraw")
		return
	




		 	
def mapNumToName():
	global newMasterAccountsFile, numToNameMap
	for item in newMasterAccountsFile:
		accountNumber = item[:7]
		accountName = item [12:]
		numToNameMap[accountNumber] = accountName

def mapAccountNumToAmount():
	global newMasterAccountsFile, accToAmountMap
	for item in newMasterAccountsFile:
		accountNumber = item[:7]
		amount = item.split()[1]
		accToAmountMap[accountNumber] = amount

	

loadValidAccountList()
loadCurrentMasterAccountsList()
loadTransActionSummary()
mapNumToName()
mapAccountNumToAmount()
parseTransactionSummary()

