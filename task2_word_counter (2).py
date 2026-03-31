# Task 2: Word & Character Counter

text = input("Paste your paragraph here:\n")

# Character count (including spaces)
char_count = len(text)
print(f"\nTotal characters (including spaces): {char_count}")

# Word count
words = text.split()
word_count = len(words)
print(f"Total words: {word_count}")

# Search feature
letter = input("\nEnter a letter to search for: ")
letter_count = text.lower().count(letter.lower())
print(f"The letter '{letter}' appears {letter_count} time(s).")

# Uppercase conversion
print(f"\nYour text in UPPERCASE:\n{text.upper()}")
