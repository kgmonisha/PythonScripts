import string

#moving to upper and lower
str1 = "hi hello how are u"
print(str1.upper())
print(str1.lower())

#split and join
list1 = str1.split(" ")
print(list1)
print(" ".join(list1))

#justification
length = max(len(name) for name in list1)
for elem in list1:
    print(elem.ljust(length+2,"-")+":")
for elem in list1:
    print(elem.center(length+2,"-")+":")
for elem in list1:
    print(elem.rjust(length+2,"-")+":")

#Translation table
trans_table = str1.maketrans("hoau","1234")
print(str1.translate(trans_table))