#1-4
str="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

word = [word.strip(",.") for word in str.split()]
print(word)

num =[1,5,6,77,8,9,15,16,18]


word_dict={}
for i, word in enumerate(word,1):
  if i in num:
    word_dict[i]=word[:1]

  else:
    word_dict[i] =word[:2]


print(word_dict)
