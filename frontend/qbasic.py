from Console import Console
from Validity import Validity
import sys, os

def main():
	userInput = Console()
	tester = Validity()

	accountNum = userInput.accountNumberInput()
	print(accountNum)
	tester.checkAccountNumber(accountNum) 

	cmd = userInput.commandInput()
	print(cmd)
	tester.checkCommand(cmd,tester.validCommandsList)
#broken
	amt = userInput.amountIn()
	print(amt)
	tester.checkAmount(amt,True)

	accName = userInput.accountNameInput()
	print(accName)
	tester.checkAccountName(accName)


accountsListFile = sys.argv[1]
accountsList = open(accountsListFile, 'r').readlines()
accountsList = map(int, accountsList)
print accountsList
main()