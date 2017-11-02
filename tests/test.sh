# from the top level directory, run "sh tests/test.sh"
# cd frontend
# empty transaction summary file
>frontend/transactionsummary.txt

# for every test folder
	# for each test name
		# run the thing and compare

output=$(python frontend/qbasic.py frontend/validaccounts.txt frontend/transactionsummary.txt testMode << EOF
`cat tests/$1/test_$2`
EOF)

expected_output=`cat tests/$1/expected_output_$2`
if [ "$output" = "$expected_output" ];
then
	echo "-----passed output test"
	echo "1" >> tests/testResults
else
	echo "-----failed output test"
	echo "expected: $expected_output"
	echo "got: $output"
	echo "0" >> tests/testResults
fi

summary=`cat frontend/transactionsummary.txt`
expected_summary=`cat tests/$1/expected_summary_$2`

if [ "$summary" = "$expected_summary" ];
then
	echo "-----passed summary test"
	echo "1" >> tests/testResults
else
	echo "-----failed summary test"
	echo "expected: $expected_summary"
	echo "got: $summary"
	echo "0" >> tests/testResults
fi

