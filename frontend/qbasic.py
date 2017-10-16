from Console import Console
from Validity import Validity
from Session import Session
from Actions import Actions
import sys, os

atmOn = True
accountsList = None

def qbasic():
	global atmOn, accountsList
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
			currentSession.logout()
		elif(cmd == "create"):
			actions.create(currentSession)
		elif(cmd == "delete"):
			actions.delete(currentSession)
		elif(cmd == "deposit"):
			actions.deposit(currentSession)
		elif(cmd == "withdraw"):
			actions.withdraw(currentSession)
		elif(cmd == "transfer"):
			actions.transfer(currentSession)

		
def loadAccounts():
	global accountsList
	accountsListFile = sys.argv[1]
	accountsList = open(accountsListFile, 'r').readlines()
	accountsList = map(int, accountsList)

loadAccounts()
qbasic()