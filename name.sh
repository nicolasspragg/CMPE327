testType= "$1"


cd tests/testType

find . -name "accounts" -prune -o -type f -name "test_*" | while read line; do 
	echo "${line#*test_}"
done


