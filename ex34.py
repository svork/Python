animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

ordinal = ['first (1st)', 'second (2nd)', 'third (3rd)', 'fourth (4th)', 'fifth (5th)', 'sixth (6th)']

i = 0

while i < len(animals):
	print "The %s animal is at %d is a %s" % (ordinal[i], i, animals[i])
	i += 1
