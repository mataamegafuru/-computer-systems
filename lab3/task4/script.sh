#!/bin/bash
ml icc
if [[ $(pwd) != "/home/grid/testbed/tb435/lab3/task4" ]]
then
	cd /home/grid/testbed/tb435/lab3/task4
fi
echo "WORKING!"
for oshka in O{1,2,3}
do
        echo "Current O: -"$oshka" i bez iXsov!" >> res
	icc -$oshka pi.cpp -o pi
	/usr/bin/time -p ./pi 2>>res
done


for oshka2 in O{1,2,3}
do
        echo "Current O: -"$oshka2 >> res
	for iX in SSE2 SSSE3 SSE4.1 SSE4.2 AVX
	do
		icc -$oshka2 -x$iX pi.cpp -o pi
		echo "Current X: -x"$iX >> res
		/usr/bin/time -p ./pi 2>>res
	done
done
