# variables
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0# inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Metric system please
kg = weight / 2
meters = height / 25.4

print "Let's talk about %r." % name
print "He's %r inches tall." % meters
print "He's %d pounds heavy." % kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "He's teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, meters, kg, age + meters + kg)
