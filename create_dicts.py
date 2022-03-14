# Preprocessing

files = ["words-all.txt", "words-guess.txt"]
word_list = []
for file in files:
    with open(file, "r", encoding="UTF-8") as in_file:
        for line in in_file:
            word_list.append(line.strip())

contains = {}

not_contains = {}

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for char in alphabets:
    contains[char] = {}
    for i in range(5):
        contains[char][i] = set()
    not_contains[char] = set()

# make the contains dictionary
for word in word_list:
    for i in range(5):
        contains[word[i]][i].add(word)

# make the not contains dictionary
for word in word_list:
    for letter in alphabets:
        if letter not in word:
            # add to not_contains[letter]
            not_contains[letter].add(word)

#print(contains)
print(not_contains)
