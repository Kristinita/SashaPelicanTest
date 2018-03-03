# @Author: Kristinita
# @Date:   2018-03-03 13:47:42
# @Last Modified by:   Kristinita
# @Last Modified time: 2018-03-03 19:38:48
# Recursive glob:
# https://unix.stackexchange.com/a/49917/237999
shopt -s globstar
# Using variables in script:
# http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html
for i in **/*.html; do
	tidy -mq --wrap 0 $i
	echo $i
done