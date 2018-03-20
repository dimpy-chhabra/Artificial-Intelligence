#Write a program that reads a paragraph in English language from an input text file
#(filename passed as command line argument). After reading the paragraph, program
#finds unique words (separated by space, uppercase & lowercase is ignored, all words
#are converted to lowercase) and finds frequency of occurrence of each word. Unique
#work and its frequency is to be written on separate line in output file.
#Question 05

import sys


input = sys.argv[1]
output = sys.argv[2]
#input = "para.txt"
data = open( input , 'rb')
para = data.read()
#print para

list = []
list = para.split()
#print "Number of Words: ",len(list)

dict = {}
count = 0
for word in list:
	#print word
	if word in dict.keys():
		count = dict.get(word)
		count +=1
		(key, val) = (word, count)
		dict[(key)] = val
	else:
		(key, val) = (word, 1)
		dict[(key)] = val
print dict

fh = open(output, "w")
fh.write(str(dict))
fh.close()