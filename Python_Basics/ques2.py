#Write a program that reads numbers from a given input text file (filename passed as
#command line argument). Each number is on a separate line in this input text file.
#After reading numbers, program finds the average of these numbers.
#Question 2

import sys


input = sys.argv[1]
output = sys.argv[2]
#input = "para.txt"
data = open( input , 'rb')
para = data.read()
#print para

list = []
list = para.split()
x = 0.00
x = sum(list) / float(len(list))
print x 


fh = open(output, "w")
fh.write(str(x))
fh.close()