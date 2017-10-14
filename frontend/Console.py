# read in commands from user/file in future
class Console:
	command = None
	accountNumber = None
	amount = None
	accountName = None



	def commandInput(self):
		
		commandIn = raw_input(("Command:"))
		self.command = commandIn
		return self.command

		




