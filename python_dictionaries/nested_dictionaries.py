# csea = {
#   student1 : {
#     "name" : "neeraj",
#     "year" : 4
#   },
#   student2 : {
#     "name" : "prem",
#     "year" : 4
#   },
#   student3 : {
#     "name" : "rohit",
#     "year" : 3
#   }
# }
# print(csea)


# # student1 = {
#     "name" : "neeraj",
#     "year" : 4
#   }
# student2 = {
#     "name" : "prem",
#     "year" : 4
#   }
# student3 = {
#     "name" : "rohit",
#     "year" : 3
# }   

# csea = {
#     "student1":student1,
#     "student2":student2,
#     "student3":student3
# }
# print(csea)

# #accessing the items
# csea = {
#   "student1" : {
#     "name" : "neeraj",
#     "year" : 4
#   },
#   "student2" : {
#     "name" : "prem",
#     "year" : 4
#   },
#   "student3" : {
#     "name" : "rohit",
#     "year" : 3
#   }
# }
# print(csea["student3"]["name"])

#looping the dictionary using items()
csea = {
  "student1" : {
    "name" : "neeraj",
    "year" : 4
  },
  "student2" : {
    "name" : "prem",
    "year" : 4
  },
  "student3" : {
    "name" : "rohit",
    "year" : 3
  }
} 

for x , object in csea.items():
    print(x)
    for y in object:
        print(y +':',object[y])
