# cd frontend
# empty transaction summary file
>frontend/transactionsummary.txt

# this script covers the scope of one test case
# another surrounding script runs this script once for every test case

# run the program using the test files as the input parameters, 
# setting testMode, and capturing the output in a variable
# `cat tests/$1/test_$2` pipes what is in the test case into the program line by line
output=$(python frontend/qbasic.py tests/$1/accounts/$2 frontend/transactionsummary.txt testMode << EOF
`cat tests/$1/test_$2`
EOF)

# now simply compare the captured output with the expected output files
expected_output=`cat tests/$1/expected_output_$2`
if [ "$output" = "$expected_output" ];
then
	echo "-----passed output test"
	echo "1" >> tests/testResults
	# when a test passes, append a 1 into the results file
else
	echo "-----failed output test"
	echo "expected: $expected_output"
	echo "got: $output"
	echo "0" >> tests/testResults
	# when a test fails, append a 0 into the results file
fi

# similarly compare the generated summary files with the expected summary files
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

