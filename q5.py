from collections import Counter
import re

# Input string
text = input("Enter a string: ")

# 1. Character replacement
old_char = input("Enter the character to replace: ")
new_char = input("Enter the replacement character: ")

replaced_text = text.replace(old_char, new_char)
print("\nAfter character replacement:", replaced_text)

# 2. String reversal
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

# 3. Palindrome checking
if text.lower() == reversed_text.lower():
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# 4. Character frequency
character_frequency = Counter(text)

print("\nCharacter frequencies:")
for char, count in character_frequency.items():
    if char == " ":
        print("'space':", count)
    else:
        print(f"'{char}':", count)

# 5. Word frequency
words = re.findall(r"\b[\w']+\b", text.lower())
word_frequency = Counter(words)

print("\nWord frequencies:")
for word, count in word_frequency.items():
    print(f"'{word}':", count)