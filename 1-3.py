#1-3
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."


cleaned_words = [word.strip(",.") for word in sentence.split()]

word_lengths = [len(word) for word in cleaned_words]

print(word_lengths)

