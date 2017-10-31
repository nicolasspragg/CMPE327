# from the top level directory, run "sh tests/test.sh"
cd frontend
# empty transaction summary file
>transactionsummary.txt

# for every test folder
	# for each test name
		# run the thing and compare

output=$(python qbasic.py validaccounts.txt transactionsummary.txt testMode << EOF
`cat ../tests/create/test_create`
EOF)

expected_output=`cat ../tests/create/expected_output_create`
if [ "$output" = "$expected_output" ];
then
	echo "pass output test"
else
	echo "fail output test"
fi

summary=`cat transactionsummary.txt`
expected_summary=`cat ../tests/create/expected_summary_create`

if [ "$summary" = "$expected_summary" ];
then
	echo "pass summary test"
else
	echo "fail summary test"
fi
