a = ("Neeraj","sai","vamshi","teja")
b = list(a)
b[2] = "prem"
a = tuple(b)
print(a)

a = ("Neeraj","sai","vamshi","teja")
b = list(a)
b.append("nipun")
a = tuple(b)
print(a)
