from Console import Console
# from Validity import Validity
from Session import Session
from Actions import Actions
import sys, os

# global variables
atmOn = True
accountsList = None
transactionSummary = None
testMode = False
if len(sys.argv) == 4:
	if (sys.argv[3] == "testMode"):
		testMode = True

# "Main program"
# Overall program intention: QBasic is a program for atm users and bank tellers to
# perform bank transactions (users and tellers) and managerial chores (tellers only).
# Input files: validaccounts.txt and transactionsummary.txt
# Output files: transactionsummary.txt (output gets appended to original)
# How to run the program:
	# python qbasic.py validaccounts.txt transactionsummary.txt
def qbasic():
	global atmOn, accountsList, transactionSummary, testMode

	userInput = Console()
	# tester = Validity()
	currentSession = Session()
	actions = Actions()

	# infinite loop while bank machine is "on"
	while atmOn == True:
		# retrieve user input
		try:
			cmd = userInput.commandInput(testMode)
		except EOFError:
			cmd = "off"

		# go through the possible input cases
		if cmd == "off":
			atmOn = False
			# ends the program
		elif(cmd == "login"):
			currentSession.login(testMode)
		elif(cmd == "logout"):
			currentSession.logout(transactionSummary)
		elif(cmd == "create"):
			actions.create(currentSession, transactionSummary, testMode)
		elif(cmd == "delete"):
			actions.delete(currentSession, transactionSummary)
		elif(cmd == "deposit"):
			actions.deposit(currentSession, transactionSummary)
		elif(cmd == "withdraw"):
			actions.withdraw(currentSession, transactionSummary)
		elif(cmd == "transfer"):
			actions.transfer(currentSession, transactionSummary)

	transactionSummary.close()

# load the valid accounts text file into a global list of ints
def loadAccounts():
	global accountsList
	accountsListFile = sys.argv[1]
	accountsList = open(accountsListFile, 'r').readlines()
	accountsList = map(int, accountsList)

# load an "open file" int a global variable, which other methods can write to
def loadSummaryFile():
	global transactionSummary
	transactionSummaryFile = sys.argv[2]
	transactionSummary = open(transactionSummaryFile, 'a')

loadAccounts()
loadSummaryFile()
qbasic()