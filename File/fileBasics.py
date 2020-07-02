#create a file and add lines
fd = open("abc.txt","w")
fd.write("This is a new file\n")
fd.write("This is the 2nd line\n")
fd.close()

#read content
with open("abc.txt","r") as fd:
    print(fd.read())

#append data, seek will set the pointer 
with open("abc.txt", "a+") as fd:
    fd.write("This is a 3rd line")
    fd.seek(20)
    print(fd.read())
    fd.close()