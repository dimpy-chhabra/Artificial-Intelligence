#Write a program that takes a sentence as input and outputs its reverse. Uppercase
#letters (if any) are converted to lowercase before reversing. Input sentence is taken
#as command line argument and output is printed on console.
#Question 03

import sys

def reverse_case(word):
	x = ""
	for i in range (len(word)):
		x = x + word[i].swapcase()
	return x		

arg1 = sys.argv[1]
list = []
list = arg1.split()
list.reverse()
for i in list:
	i = reverse_case(i)
print ' '.join(list)