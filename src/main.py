b_set = set()
w_set = set()
wordle_set = set()

with open("blacklist.txt", "r") as b_file:
	for line in b_file.readlines():
		b_set.add(line.strip("\n"))


with open("words.txt", "r") as w_file:
	for line in w_file.readlines():
		w_set.add(line.strip("\n"))

wordle_set = w_set.difference(b_set)


print(len(wordle_set))
five_set = set()
for word in wordle_set:
	if len(word) == 5:
		five_set.add(word)

print(len(five_set))
print(len(wordle_set.difference(five_set)))

for word in five_set:
	print(word)