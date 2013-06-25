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

for line in txt: #creates the our_dict from the file txt
	#takes in string, lowercases it, then strips new lines and punctuation
	for word in line.lower().strip('\n').replace(".", "").replace(",", "").replace("?","").split():
		#sets word that doesn't exist to zero
		our_dict[word]=our_dict.get(word,0) + 1
	


# sorts by values, starting with the largest
#for key, value in sorted(our_dict.iteritems(), key=lambda (k,v): (v,ord(chr(k))), reverse=True):
for key, value in sorted(our_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
#for key, value in sorted(our_dict.iteritems()):
  print "%s: %s" % (key, value)

