sentence = input("Enter a sentence: ")

words = sentence.split()
words.reverse()

print("Reversed sentence:", " ".join(words))
# output:
# Enter a sentence: i am nikhil
# Reversed sentence: nikhil am i