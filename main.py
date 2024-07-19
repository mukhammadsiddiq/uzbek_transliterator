from transliterate import to_cyrillic, to_latin

sentence = input("Matn Kiriting: ")
if sentence.isascii():
    print(to_cyrillic(sentence))
else:
    print(to_latin(sentence))