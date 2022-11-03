"""
Given an integer array numbers and return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

"""

nums = [-1,0,1,2,-1,-4]
triplets = []
finalTriplets=[]
n=len(nums)
mySum = 0
for i in  range(n):
    for j in range(1,n):
        for k in range(2,n):
            if i!= j and i != k and j!= k:
                mySum = nums[i] + nums[j] + nums[k]
                if mySum == 0:
                    sumTripplet = [nums[i],nums[j],nums[k]]
                    print("triplets are {}+{}+{}=0".format(nums[i],nums[j],nums[k]))
                    triplets.append(sumTripplet)
                    
                
print(triplets)
m=len(triplets)

for i in range(m):
   for j in range(1,m):
       if triplets[i]  not in finalTriplets:
           finalTriplets.append(triplets[i])
           

print("final triplets ",finalTriplets)
                

