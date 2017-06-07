numbers = []

def contar(limite):
	"""
	Essa funcao conta ate o limite
	"""
	i = 0
	for i in range(i, limite):
		print "At the top i is %d" % i
		numbers.append(i)

		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

contar(int(raw_input("Qual o limite? ")))

print "The numbers: "

for num in numbers:
	print num
