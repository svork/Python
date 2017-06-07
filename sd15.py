# import argv from sys module(library)
from sys import argv

# saving the arguments to two variables
script, filename = argv

# Using the open() to receive the file name and store in into a variable
txt = open(filename)

# print the file name
print "Here's your file %r:" % filename

# using read() to print out the file's content
print txt.read()

# closing the file
txt.close()

# reading the file name using raw_input()
print "Type the filename again:"
file_again = raw_input("> ")

# using open() to receive the file
txt_again = open(file_again)

# using read() to show the file's content
print txt_again.read()

# closing the file
txt_again.close()
