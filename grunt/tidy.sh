# @Author: Kristinita
# @Date:   2018-03-03 13:47:42
# @Last Modified by:   Kristinita
# @Last Modified time: 2018-03-03 15:11:01
shopt -s globstar
for i in **/*.html; do
	tidy -mq -config "../tidy-config.txt" $i
	echo $i
done