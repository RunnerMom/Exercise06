sentence = "The quick brown fox jumped over the lazy dog."
characters = {"T":0, "h":1}

for character in sentence:
    characters[character] = characters.get(characters,0) + 1 

print(characters)