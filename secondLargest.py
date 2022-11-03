#Write a program to find the second largest number in an array. [2.5 marks]


myArray = [5,4,3,1,6,8]

firstLargest = myArray[0]
secondLargest = myArray[0]
n=len(myArray)

for i in range(1,n):
    if myArray[i] > firstLargest:
        firstLargest = myArray[i]
        
for j in range(1,n):
    if myArray[j] > secondLargest and myArray[j] < firstLargest:
        secondLargest = myArray[j]

print("firstLargest {}".format(firstLargest))
print("secondLargest {}".format(secondLargest))