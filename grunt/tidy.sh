# @Author: Kristinita
# @Date:   2018-03-03 13:47:42
# @Last Modified by:   Kristinita
# @Last Modified time: 2018-03-03 18:52:13
# Recursive glob:
# https://unix.stackexchange.com/a/49917/237999
shopt -s globstar
cd output
# Using variables in script:
# http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html
for i in **/*.html; do
	echo $i
	tidy -mq --wrap 0 $i
done