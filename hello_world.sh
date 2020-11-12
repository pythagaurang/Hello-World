#!/bin/sh
hello(){
	if [ -z "$1" ];then
		echo "Hello world"
	else
		echo "$1) Hello world"
	fi
}
echo "Concurrent hello worlds:"
for i in $(seq 1 10); do
	hello $i &
done
echo "End of script"
