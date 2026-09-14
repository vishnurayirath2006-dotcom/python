string = input("Enter a string: ")

for ch in set(string):
    if ch != " ":
        print(ch, ":", string.count(ch))

words = string.split()

for word in set(words):
    print(word, ":", words.count(word))