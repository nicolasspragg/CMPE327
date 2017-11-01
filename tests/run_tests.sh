for testName in `sh tests/name.sh create`; do
	sh tests/test.sh create $testName
done

for testName in `sh tests/name.sh delete`; do
	sh tests/test.sh delete $testName
done

for testName in `sh tests/name.sh deposit`; do
	sh tests/test.sh deposit $testName
done

for testName in `sh tests/name.sh login`; do
	sh tests/test.sh login $testName
done

for testName in `sh tests/name.sh transfer`; do
	sh tests/test.sh transfer $testName
done

for testName in `sh tests/name.sh withdraw`; do
	sh tests/test.sh withdraw $testName
done