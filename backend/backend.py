import sys, os

#global variables

currentValidAccountList = None
transactionSummary = None
currentMasterAccountsList = None
newMasterAccountsFile = None
newValidAccountsFile = None




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
	global transactionSummary, actionList

	print transactionSummary

	for item in transactionSummary:
		if(item[:3] == "NEW"):
			#call create handler
			print("found new")
		elif(item[:3] == "DEL"): 
			#call delete handler
			print("found del")
		elif(item[:3] == "DEP"):
			#call deposit handler
			print("found dep")
		elif(item[:3] == "WDR"):
			#call withdraw handler
			print("found withdraw")
		elif(item[:3] == "XFR"):
			#call transfer handler
			print("found transfer")
		elif(item[:3] == "EOS"):
			#end of file 
			return
















loadValidAccountList()
loadCurrentMasterAccountsList()
loadTransActionSummary()
parseTransactionSummary()

