# %r stands for RAW, kind of set -x, useful for debug
formatter = "%r %r %r %r"

# integers
print formatter % (1, 2, 3, 4)

# string
print formatter % ("one", "two", "three", "four")

# boolean
print formatter % (True, False, False, True)

# recursive variable
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
