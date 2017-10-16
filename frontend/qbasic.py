from Console import Console
from Validity import Validity
from Session import Session
import sys, os

def qbasic():
	userInput = Console()
	tester = Validity()
	newSession = Session()

	cmd = userInput.commandInput()


	if(cmd == "login"):
		accType = userInput.accountTypeInput() 
		newSession.login(accType)
	elif(cmd == "logout"):
		





	




	




qbasic()