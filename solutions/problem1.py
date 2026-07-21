# Palindrome Checker
word = input("Enter a word: ").strip().lower()

if word == word[::-1]:
    print(f"Yes, '{word}' is a palindrome.")
else:
    print(f"No, '{word}' is not a palindrome.")