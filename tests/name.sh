# output the name of every test in an action's folder
array=("$@")

for i in "${array[@]}"
do
cd tests/$i
find . -name "accounts" -prune -o -type f -name "test_*" | while read line; do
	if [ "${line#*test_}" != "./accounts" ]; then
		echo "${line#*test_}"
	fi
done
cd ..
cd ..
done
