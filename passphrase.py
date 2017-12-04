def isValidPassphrase(pp):
	words = pp.split(" ")
	# counts = [words.count(word) for word in words]
	# if max(counts)>1:
	# 	return False
	# else:
	# 	return True
	##################
	# Allow no anagrams
	for i, word in enumerate(words):
		for j, other in enumerate(words):
			if i!=j and len(word)==len(other):
				common = [c for c in word if word.count(c)==other.count(c)]
				if len(common)==len(word):
					return False
	return True 


assert(isValidPassphrase("aa bb cc dd")==True)
assert(isValidPassphrase("aa aa bb cc")==False)
assert(isValidPassphrase("abc bcd edf")==True)
assert(isValidPassphrase("pir dafgsah dafgsah kndjbml estcz yjeoijp kkcws ebq puwno")==False)
assert(isValidPassphrase("yvwykx uhto ten wkvxyy wdbw")==False)

with open("passphrases.txt", 'r') as fi:
	lines = fi.readlines()

for i, line in enumerate(lines):
	if i!=len(lines)-1:
		lines[i] = line[:-1]

true_passes = [isValidPassphrase(line) for line in lines]
c = true_passes.count(True)
print("Input length = " + str(len(lines)))
print("Passes = " + str(c))