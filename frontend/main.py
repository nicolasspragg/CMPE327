from Console import Console
from Validity import Validity
import sys, os

def main():
	userInput = Console()
	tester = Validity()
	#cmd = userInput.commandInput()
	#accountNum = userInput.accountNumberInput()
	#accountName = userInput.accountNameInput()
	amt = userInput.amountIn()
	print(amt)

	tester.checkAmount(amt,False)



main()