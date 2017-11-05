
array=("$@")

for i in "${array[@]}"
do
cd tests/$i
find . -path "tests/$i/accounts" -prune -o -type f -name "test_*" | while read line; do 
	echo "${line#*test_}"
done
cd ..
cd ..
done
