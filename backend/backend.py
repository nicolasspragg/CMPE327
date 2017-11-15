import sys, os, copy
#This program processes the merged summary file and makes changes to the master account file/ valid accounts list 
#based on whats in the summary file

#global variables to store the files, lists and maps

currentValidAccountList = None
transactionSummary = None
currentMasterAccountsList = None
newMasterAccountsFile = None
newValidAccountsFile = []
numToNameMap = {}
accToAmountMap = {}
recentlyCreated = []
recentlyDeleted = []
skip = []

#copy valid accounts list into new list
def loadValidAccountList():
	global currentValidAccountList
	currentValidAccountListFile = sys.argv[1]
	currentValidAccountList = open(currentValidAccountListFile, 'r').readlines()
	currentValidAccountList = map(str.rstrip, currentValidAccountList)
	newValidAccountsFile = currentValidAccountList[:]

#copy the master accounts list into new list
def loadCurrentMasterAccountsList():
	global currentMasterAccountsList, newMasterAccountsFile
	currentMasterAccountsListFile = sys.argv[2]
	currentMasterAccountsList = open(currentMasterAccountsListFile, 'r').readlines()
	currentMasterAccountsList = map(str.rstrip, currentMasterAccountsList)
	newMasterAccountsFile = currentMasterAccountsList[:]

#load in the transaction summary
def loadTransActionSummary():
	global transactionSummary
	transactionSummaryFile = sys.argv[3]
	transactionSummary = open(transactionSummaryFile, 'r').readlines()
	transactionSummary = map(str.rstrip, transactionSummary)

#this function parses the transaction summmary by taking all the actions in the first column of the file and running
#different handler functions depending on the action
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
			handleTransfer(accountNumInTs, amount, accountToNumber)
		elif(action == "EOS"):
			#end of file 
			return
#This function checks if the account trying to be creasted has a unique account number. If it is, it add the new account to the master accounts file
def handleCreate(accountNumInTs, accountName):
	global recentlyCreated, currentValidAccountList, currentMasterAccountsList, newMasterAccountsFile, newValidAccountsFile, recentlyDeleted
	if(accountNumInTs in newMasterAccountsFile or accountNumInTs in recentlyCreated):
		#failure
		print("not unique")
		return
	else:
		#add to lists
		newValidAccountsFile.append(int(accountNumInTs))
		newMasterAccountsFile.append(accountNumInTs + " 000 " + accountName)
		recentlyCreated.append(accountNumInTs)

	
#This function checks if the name on the account being deleted matches the name associated with that account in the master accounts file. 
def handleDelete(accountNumInTs, accountName):
	global skip, recentlyCreated, recentlyDeleted, currentValidAccountList, currentMasterAccountsList, newMasterAccountsFile, newValidAccountsFile,numToNameMap, accToAmountMap
	try:
		name = numToNameMap[accountNumInTs]
	except KeyError:
		print("invalid account number")
		return
	name = name.strip()
	accountName = accountName.strip()
	
	skip.append(accountNumInTs)

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
		else:
			print("account must have no funds")
			return 

#Writes to new valid accounts list
def writeNewValidAccounts(skip, currentValidAccountList):
	f = open('backend/newValidAccounts', 'w').close() # empty the file
	f = open('backend/newValidAccounts', 'w')
	for account in currentValidAccountList:
		if account not in skip:
			f.write(account+"\n")
	f.close()

#writes to new master accounts list
def writeNewMasterAccounts(newMasterAccountsFile):
	f = open('backend/MasterAccountsFile', 'w')
	for account in newMasterAccountsFile:
			f.write(account+"\n")
	f.close()

#function checks if the account hasn't been deleted, and adds money to the account if it hasn't. 
def handleDeposit(accountNumInTs, amount):
	global recentlyCreated, recentlyDeleted, currentValidAccountList, currentMasterAccountsList, newMasterAccountsFile, newValidAccountsFile,numToNameMap, accToAmountMap
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
	else:
		print("account has been deleted can't deposit")
		return

#Function checks if the account hasn't been deleted, and checks if the amount being withdrawn doesn't cause the account balance to go negative. 
def handleWithdraw(accountNumInTs, amount):
	global recentlyCreated, recentlyDeleted, currentValidAccountList, currentMasterAccountsList, newMasterAccountsFile, newValidAccountsFile,numToNameMap, accToAmountMap

	if(accountNumInTs not in recentlyDeleted):
		name = numToNameMap[accountNumInTs]
		oldAmount = accToAmountMap[accountNumInTs]
		index = newMasterAccountsFile.index(accountNumInTs + " " + oldAmount + " " + name)

		amount = int(amount)
		oldAmount = int(oldAmount)
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
	
#Function works the same way as withdraw, but checks that the account sending money doesn't go negative. 
def handleTransfer(accountNumInTs, amount, accountToNumber):
	global recentlyCreated, recentlyDeleted, currentValidAccountList, currentMasterAccountsList, newMasterAccountsFile, newValidAccountsFile,numToNameMap, accToAmountMap
	if(accountNumInTs not in recentlyDeleted):
		if(accountToNumber not in recentlyDeleted):
			name = numToNameMap[accountNumInTs]
			nameTo = numToNameMap[accountToNumber]
			oldAmount = accToAmountMap[accountNumInTs]
			oldAmountTo = accToAmountMap[accountToNumber]
			index = newMasterAccountsFile.index(accountNumInTs + " " + oldAmount + " " + name)
			indexTo = newMasterAccountsFile.index(accountToNumber + " " + oldAmountTo + " " + nameTo)

			amount = int(amount)
			oldAmount = int(oldAmount)
			oldAmountTo = int(oldAmountTo)

			amountTo = oldAmountTo + amount
			oldAmount -= amount

			if oldAmount < 0:
				print("can't make account negative")
				return
			else:
				amountTo = str(amountTo)
				oldAmount = str(oldAmount)


				newMasterAccountsFile[index] = (accountNumInTs +" " + oldAmount + " " + name)
				newMasterAccountsFile[indexTo] = (accountToNumber +" " + amountTo + " " + nameTo)
				mapAccountNumToAmount()
		else:
			print("From account has been deleted can't transfer")
			return
	else:
		print("From account has been deleted can't transfer")
		return


#Creates a simple [account number : name] dictionary to quicly match them later		 	
def mapNumToName():
	global newMasterAccountsFile, numToNameMap
	for item in newMasterAccountsFile:
		accountNumber = item[:7]
		accountName = item [12:]
		numToNameMap[accountNumber] = accountName
#Creates a simple [account number : amount] dictionary to quicly match them later	
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
writeNewValidAccounts(skip, currentValidAccountList)
writeNewMasterAccounts(newMasterAccountsFile)

