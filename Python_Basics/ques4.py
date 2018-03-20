#Write a program that reads a paragraph in English language from an input text 
#file (filename passed as command line argument). After reading the paragraph, 
#programfinds the number of sentences (separated by full stop), number of words 
#(separated by space) and number of characters (full stop and spaces are ignored, paragraph
#won't contain any other punctuations), each on separate line in output file.
#Question 04

import sys


input = sys.argv[1]
output = sys.argv[2]

data = open( input , 'rb')
para = data.read()
#print para

list = []
list = para.split()
print "Number of Words: ",len(list)

count_of_sentences = 0
count_of_alphabets = 0 

for i in range ((len(para))):
	if para[i]==".":
		count_of_sentences+=1
	if para[i].isalpha():
		count_of_alphabets+=1

print "Number of Sentences: ",count_of_sentences
print "Number of Characters: ",count_of_alphabets

key = []
key.append(count_of_sentences)
key.append(len(list))
key.append(count_of_alphabets)

fh = open(output, "w")
fh.write(str(key))
fh.close()
