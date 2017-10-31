# from the top level directory, run "sh tests/test.sh"
cd frontend
# empty transaction summary file
# for every test folder
	# for each test name
		# run the thing and compare
python qbasic.py validaccounts.txt transactionsummary.txt testMode << EOF
login
agent
create
4444444
testname
logout
EOF