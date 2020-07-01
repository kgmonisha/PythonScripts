import string
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)

str1  = "Hi i am monisha"
str2 = "12345678"
#convert str1 to ascii letters
text = "".join([c for c in str1 if c in string.ascii_letters])
print(text)
print(all([c.isnumeric() for c in str2]))