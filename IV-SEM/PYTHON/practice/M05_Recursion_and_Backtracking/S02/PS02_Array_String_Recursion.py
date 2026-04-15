'''
#Sum of AArray in Traditional way
def Array_sum(nums):
    s=0 
    for i in range(len(nums)):
        s+=nums[i]
    return s    
print(Array_sum([1, 2, 3, 4, 5])) #15
'''
'''
#Sum of AArray using Recursion
def Array_sum(nums,index):
    if index==-1:
        return 0
    return nums[index]+Array_sum(nums,index-1)
n=list(map(int,input().split()))
print(Array_sum(n,len(n)-1))
'''
'''
#Recursive Approach-2
def Array_sum(nums):
    if len(nums)==0:
        return 0
    return nums[-1]+Array_sum(nums[:-1])
n=list(map(int,input().split()))
print(Array_sum(n))
'''
'''
#Reverse an Array using Recursion
def reverse_array(nums,i,j):
    if i>=j:
        return nums 
    nums[i],nums[j]=nums[j],nums[i]
    return reverse_array(nums,i+1,j-1)
n=list(map(int,input().split()))
print(reverse_array(n,0,len(n)-1))
''' 