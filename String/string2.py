import string
str1 = "hi this is monisha"

#startswith/endswith
print(str1.startswith("hi"))
print(str1.endswith("sha"))
print(str1.startswith("Hi"))

#find(left) and rfind(right side) functions first occurence
print(str1.find("is"))
print(str1.rfind("is"))

#count and replace
print(str1.count("is"))
print(str1.replace("is","end"))