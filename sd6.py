# variables
# assigning string values to variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# print the variables
print x
print y

# print both string and variable
print "I said: %r." % x
print "I also said: '%s'." % y

# using boolean variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# print variable
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# concatenate variables
print w + e
