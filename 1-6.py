from sre_constants import SRE_INFO_PREFIX
#1-6
str1 ='paraparaparadise'
str2 ='paragraph'
X = generate_ngram_from_text(str1, n=2, mode="char",)
print("文字 bi-gram (空白を無視):", X)

Y = generate_ngram_from_text(str2, n=2, mode="char",)
print("文字 bi-gram (空白を無視):", Y)



X = set(X)
Y = set(Y)

print(X)
print(Y)

union = X.union(Y)
intersection = X.intersection(Y)
difference = X.difference(Y)


print('和集合' ,union)
print('積集合',intersection)
print('差集合', difference)


se_in_X = 'se' in X
se_in_Y=  'se' in Y

print(se_in_X)
print(se_in_Y)
