#its efficient to use arrays instaed of lists in places where the data is homogenous

from array import array
arr1 = array('i',[1,2,3,4,5,6,7])
print(arr1.typecode)

arr1.insert(0,0)
arr1.append(8)
arr1.extend([9,10,11])
print(arr1)

for i,elem in enumerate(arr1):
    arr1[i]=arr1[i]*2

print(arr1)

#convert array to list
list1 = arr1.tolist()
print(list1)