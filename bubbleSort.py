"""
Write a program or algorithm to implement bubble sort. 


"""


myArray = [5,3,2,1,7,10]



size = len(myArray)
print(size)
for i in range(size):
    for j in range(i+1,size):
        if myArray[i] < myArray[j]:
            temp=myArray[j]
            myArray[j]=myArray[i]
            myArray[i]=temp



print("sort descending {}".format(myArray))

for i in range(size):
    for j in range(i+1,size):
        if myArray[i] > myArray[j]:
            temp=myArray[j]
            myArray[j]=myArray[i]
            myArray[i]=temp

print("sort ascending {}".format(myArray))
