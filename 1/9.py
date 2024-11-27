import random

def shuffled_words(text):
    words = text.split()
    scrambled = []
    for word in words:
        if len(word) > 4:

            head, middle, tail = word[0], word[1:-1], word[-1]
            middle_list = list(middle)
            random.shuffle(middle_list)
            shuffled_word = head + ''.join(middle_list) + tail
            scrambled.append(shuffled_word)
        else:
            scrambled.append(word)
    return ' '.join(scrambled)

# Example sentence
input_sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
scrambled_sentence = shuffled_words(input_sentence)
scrambled_sentence
