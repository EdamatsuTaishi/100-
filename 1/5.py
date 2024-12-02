#1-5
def generate_ngram_from_text(text, n, mode="word",):
    
    if mode == "word":
        # 単語単位のn-gramを生成
        sequence = text.split()
    elif mode == "char":
        # 文字単位のn-gramを生成
        sequence = text.replace(" ", "")
    else:
        raise ValueError("modeは 'word' または 'char' を指定してください。")

    # n-gram生成
    return [sequence[i:i + n] for i in range(len(sequence) - n + 1)]

# 使用例
sentence = "I am an NLPer"

# 単語 bi-gram
word_bigrams = generate_ngram_from_text(sentence, n=2, mode="word")
print("単語 bi-gram:", word_bigrams)


# 文字 bi-gram (空白を無視)
char_bigrams_without_space = generate_ngram_from_text(sentence, n=2, mode="char",)
print("文字 bi-gram (空白を無視):", char_bigrams_without_space)
