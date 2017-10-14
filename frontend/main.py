from Console import Console
from Validity import Validity
import sys, os

def main():
	userInput = Console()
	tester = Validity()
	cmd = userInput.commandInput()
	print(cmd)

	tester.checkCommandValid(cmd,tester.validCommandsList)
	




main()