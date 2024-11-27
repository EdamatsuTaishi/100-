#1-2
a="パトカー"
b="タクシー"
c="".join(a+b for a,b in zip(a,b))
print(c)
