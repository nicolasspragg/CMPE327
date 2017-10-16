from Console import Console
from Validity import Validity
from Session import Session
from Actions import Actions
import sys, os

atmOn = True
accountsList = None
transactionSummary = None

def qbasic():
	global atmOn, accountsList, transactionSummary
	print accountsList

	userInput = Console()
	tester = Validity()
	currentSession = Session()
	actions = Actions()

	while atmOn == True:
		cmd = userInput.commandInput()
		if cmd == "off":
			atmOn = False
		elif(cmd == "login"):
			currentSession.login()
		elif(cmd == "logout"):
			currentSession.logout(transactionSummary)
		elif(cmd == "create"):
			actions.create(currentSession, transactionSummary)
		elif(cmd == "delete"):
			actions.delete(currentSession, transactionSummary)
		elif(cmd == "deposit"):
			actions.deposit(currentSession, transactionSummary)
		elif(cmd == "withdraw"):
			actions.withdraw(currentSession, transactionSummary)
		elif(cmd == "transfer"):
			actions.transfer(currentSession, transactionSummary)

	transactionSummary.close()
		
def loadAccounts():
	global accountsList
	accountsListFile = sys.argv[1]
	accountsList = open(accountsListFile, 'r').readlines()
	accountsList = map(int, accountsList)

def loadSummaryFile():
	global transactionSummary
	transactionSummaryFile = sys.argv[2]
	transactionSummary = open(transactionSummaryFile, 'a')

loadAccounts()
loadSummaryFile()
qbasic()