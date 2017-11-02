# empty the test results file
>tests/testResults

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
echo ""
echo "----------Results----------"
echo "Passed: `(fgrep -o 1 tests/testResults | wc -l)`"
echo "Failed: `(fgrep -o 0 tests/testResults | wc -l)`"