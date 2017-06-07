# import random module
import random

# import urlopen() function from urlib module
from urllib2 import urlopen

# import sys module
import sys

# variable receives URL with list of words
WORD_URL = open("palavra")

# create an empty list
WORDS = []

# create a dictionary with phrases related to Object Oriented Programming
PHRASES = {
	"class %%%(%%%):":
	"Make a classe named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
	"class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	"class %%% has-a function named *** that takes self and @@@ parameters.",	
	"*** = %%%()":
	"set *** to an instance of class %%%.",
	"***.***(@@@)":
	"from *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
	"from *** get the *** attribute and set it to '***'."
}

# test if the first argument is 'english'
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False

# append the words from the URL into the empty list WORDS
for word in WORD_URL.readlines():
	WORDS.append(word.strip()) # strip() remove leading and trailing spaces from string

# function convert takes two parameters, snippet and phrase
def convert(snippet, phrase):
	class_names = [w.capitalize() for w in # capitalize() makes the first letter of a string UPPER case
		random.sample(WORDS, snippet.count("%%%"))] # sample() get N random elements from WORDS list, where N is the integer returned by count()
	other_names = random.sample(WORDS, snippet.count("***")) # same as above regarding sample()
	results = [] # create an empty list
	param_names = [] # create an empty list

	for i in range (0, snippet.count("@@@")): # range from 0 to N, where N is how many times the string appears, kind of grep -c
		param_count = random.randint(1,3) # return an integer N, where a -ge  N -le  b
		param_names.append(', '.join(random.sample(WORDS, param_count))) # join the parameters, separated by ' , ' (comma)

	for sentence in snippet, phrase:
		result = sentence[:]

		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)
		
		# fake other names
		for word in other_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results

# keep going until they hit CTRL-D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print question

			raw_input("> ")
			print "Answer: %s\n\n" % answer

except EOFError:
	print "\nBye"
