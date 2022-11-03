
"""

You are given an array [-23, 12, -35, 45, 20, 36] then the two elements would be -35 & 36 as their pair sum is 1 which is closest to 0

"""

myArray=[-23, 12, -35, 45, 20, 36]

size=len(myArray)

for i in range(size):
    mySum=0
    for j in range(1,size):
            mySum=myArray[i] + myArray[j]
            if mySum > 0 and mySum < 2:
                print("pair {} and {}".format(myArray[i],myArray[j]))
        