# import argv
from sys import argv

# assign arguments to variables
script, input_file = argv

# print function
def print_all(f):
	print f.read()

# rewind, back to beginning of file
def rewind(f):
	f.seek(0)

# print line number and its content
def print_a_line(line_count, f):
	print "The 'line_count' variable is equal to %d." % line_count
	print line_count, f.readline(),

# open the file
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# assign line number
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
