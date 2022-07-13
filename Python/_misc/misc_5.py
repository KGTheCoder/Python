from textblob import Word

str = Word("Happy")
str2 = Word("Chair")

print(str.spellcheck())
print(str2.spellcheck())

