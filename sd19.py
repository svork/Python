# defining the function with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# print the values
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


# print the values
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# assign values to the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# assigne values to the function
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# assign valiues to the function
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# my own function
def ppk(a,b):
	print "%s + %s = %f" % (a, b, a + b)
	print "%s - %s = %f" % (a, b, a - b)
	print "%s * %s = %f" % (a, b, a * b)
	print "%s / %s = %r" % (a, b, a / b)
	print "===========================================\n"

ppk(11,23)
ppk(234,92387)
	
