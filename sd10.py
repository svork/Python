# variables using escape characters
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# using the triple quotes technique
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# compare %r and %s
a = "This is a raw string"
b = "This is a regular string"

print "%r" % a
print "%s" % b
