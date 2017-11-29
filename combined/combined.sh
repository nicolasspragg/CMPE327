#python frontend/qbasic.py frontend/validaccounts.txt frontend/transactionsummary.txt testMode


#python backend/backend.py Backend/ValidAccounts backend/MasterAccountsFile backend/MergedSummary


# cd frontend
# empty transaction summary file
>frontend/transactionsummary.txt

# this script covers the scope of one test case
# another surrounding script runs this script once for every test case

# run the program using the test files as the input parameters, 
# setting testMode, and capturing the output in a variable
# `cat tests/$1/test_$2` pipes what is in the test case into the program line by line
output=$(python frontend/qbasic.py tests/create/accounts/create frontend/transactionsummary.txt testMode << EOF
`cat combined/inputs/1`
EOF)
cp frontend/transactionsummary.txt combined/outputs
mv combined/outputs/transactionsummary.txt combined/outputs/1
>frontend/transactionsummary.txt

output=$(python frontend/qbasic.py tests/deposit/accounts/validDepositTellerMode frontend/transactionsummary.txt testMode << EOF
`cat combined/inputs/2`
EOF)
cp frontend/transactionsummary.txt combined/outputs
mv combined/outputs/transactionsummary.txt combined/outputs/2
>frontend/transactionsummary.txt


output=$(python frontend/qbasic.py tests/withdraw/accounts/withdrawValidMachineMode frontend/transactionsummary.txt testMode << EOF
`cat combined/inputs/3`
EOF)
cp frontend/transactionsummary.txt combined/outputs
mv combined/outputs/transactionsummary.txt combined/outputs/3
>frontend/transactionsummary.txt

cat combined/outputs/1 >> combined/merged_transaction_summary.txt
cat combined/outputs/2 >> combined/merged_transaction_summary.txt
cat combined/outputs/3 >> combined/merged_transaction_summary.txt