import csv
#use zipfile for working with zipfiles
import zipfile

def readersample():
    with open("test.csv") as fd:
        data = csv.reader(fd)
        for line in data:
            print(line)

def writersample():
    with open("test1.csv","a") as fd:
        csvwriter = csv.writer(fd)
        csvwriter.writerow(["name","age","sex"])
        csvwriter.writerow(["A", 10, "M"])
        csvwriter.writerow(["B", 20, "F"])
        fd.close()
readersample()
writersample()