# copying all itens from ine to another dictionary using copy()
# x = {
#     "name"    : "neeraj",
#     "roll no" :  6618,
#     "branch"  : "cse"
# }
# y = x.copy()
# print(y)   

#another method using dict()
x = {
    "name"    : "neeraj",
    "roll no" :  6618,
    "branch"  : "cse"
}
y = dict(x)
print(y)   