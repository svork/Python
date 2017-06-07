# create a mappinf of state to abbreviation
states = {
	'Sao Paulo': 'SP',
	'Minas Gerais': 'MG',
	'Rio de Janeiro': 'RJ',
	'Espirito Santo': 'ES',
	'Bahia': 'BA' 
}

# create a basic set of states and some cities in them
cities = {
	'SP': 'Campinas',
	'MG': 'Uberlandia',
	'RJ': 'Seropedica',
}

# add some cities
cities['ES'] = 'Vila Velha'
cities['BA'] = 'Ilheus'

# print out some cities
print '-' * 10
print "SP State has: ", cities['SP']
print "RJ State has: ", cities['RJ']

# print some states
print '-' * 10
print "Bahia's abbreviation is: ", states['Bahia']
print "Espirito Santo's abbreviation is: ", states['Espirito Santo']

# do it by using the state then cities dict
print '-' * 10
print "Minas Gerais has: ", cities[states['Minas Gerais']]
print "Sao Paulo has: ", cities[states['Sao Paulo']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city
