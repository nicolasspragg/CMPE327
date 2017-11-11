import sys, os

#global variables

currentValidAccountList = None
transactionSummary = None
currentMasterAccountsList = None
newMasterAccountsFile = None
newValidAccountsFile = None
tempAccountNumbers = []

def loadValidAccountList():
	global currentValidAccountList
	currentValidAccountListFile = sys.argv[1]
	currentValidAccountList = open(currentValidAccountListFile, 'r').readlines()
	currentValidAccountList = map(int, currentValidAccountList)


def loadCurrentMasterAccountsList():
	global currentMasterAccountsList
	currentMasterAccountsListFile = sys.argv[2]
	currentMasterAccountsList = open(currentMasterAccountsListFile, 'r').readlines()
	currentMasterAccountsList = map(str, currentMasterAccountsList)

def loadTransActionSummary():
	global transactionSummary
	transactionSummaryFile = sys.argv[3]
	transactionSummary = open(transactionSummaryFile, 'r').readlines()
	transactionSummary = map(str, transactionSummary)

def parseTransactionSummary(): 
	global transactionSummary


	for item in transactionSummary:
		action = item[:3]
		accountNumInTs = item[5:11]
		amount = item[13:15]
		accountToNumber = item[17:23]
		accountName = item[24:]
		print(accountName)

		if(action == "NEW"):
			#call create handler
			handleCreate(accountNumInTs, accountName)
		elif(action == "DEL"): 
			#call delete handler
			handleDelete()
		elif(action == "DEP"):
			#call deposit handler
			handleDeposit()
		elif(action == "WDR"):
			#call withdraw handler
			handleWithdraw()
		elif(action == "XFR"):
			#call transfer handler
			handleTransfer()
		elif(action == "EOS"):
			#end of file 
			return

def handleCreate(accountNumInTs, accountName):
	global tempAccountNumbers, currentValidAccountList, currentMasterAccountsList, newMasterAccountsFile, newValidAccountsFile

	if(accountNumInTs in currentValidAccountList):
		#failure
		print("Not a unique account number")
		return
	else:
		#add to lists etc etc










	#end
	tempAccountNumbers.append(accountNumInTs)



loadValidAccountList()
loadCurrentMasterAccountsList()
loadTransActionSummary()
parseTransactionSummary()

