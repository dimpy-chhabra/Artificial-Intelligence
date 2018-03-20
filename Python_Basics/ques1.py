#Write a program that takes three numbers as input from command line and outputs
#the largest among them.
#Question 02

import sys

s = 0
list = []
for arg in sys.argv[1:]:
	list.append(int(arg))
	#arg1 = sys.argv[1]

list.sort()
print list[len(list)-1]
