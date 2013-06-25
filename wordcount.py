#Exercise 6 in hackbright GIT curriculum
# week two, day one


#write a program that opens a file and counts how many times each space -separated wod
# occurs in that file.  

# dictionary with word, counter pairs
# if word in dictionary -> increment counter
# else add word, 1 to dictionary


from sys import argv
import string
script, filename = argv

txt = open(filename)

our_dict = {}

for line in txt:
	new_line = line.strip('\n')
	for word in new_line.split(" "):
		our_dict[word]=our_dict.get(word,0)
		our_dict[word] +=1



for key, value in our_dict.iteritems():
	print key, value
