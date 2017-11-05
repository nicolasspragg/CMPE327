# from the top level directory, run "sh tests/run_tests.sh"

# this script orchestrates the running of each test
# test types are organized into folders so that is why
# there is repetition for each action

# empty the test results file
>tests/testResults

# get the names of each test, and for each test, run the singular test script
for testName in `sh tests/name.sh create`; do
	echo ""
	echo "----------$testName----------"
	sh tests/test.sh create $testName
done

for testName in `sh tests/name.sh delete`; do
	echo ""
	echo "----------$testName----------"
	sh tests/test.sh delete $testName
done

for testName in `sh tests/name.sh deposit`; do
	echo ""
	echo "----------$testName----------"
	sh tests/test.sh deposit $testName
done

for testName in `sh tests/name.sh login`; do
	echo ""
	echo "----------$testName----------"
	sh tests/test.sh login $testName
done

for testName in `sh tests/name.sh transfer`; do
	echo ""
	echo "----------$testName----------"
	sh tests/test.sh transfer $testName
done

for testName in `sh tests/name.sh withdraw`; do
	echo ""
	echo "----------$testName----------"
	sh tests/test.sh withdraw $testName
done

# read the test results file
# count up the 1s and 0s in the results file that got
# appended every test, depending on success or failure
# and summarize the information
echo ""
echo "----------Results----------"
echo "Passed: `(fgrep -o 1 tests/testResults | wc -l)`"
echo "Failed: `(fgrep -o 0 tests/testResults | wc -l)`"