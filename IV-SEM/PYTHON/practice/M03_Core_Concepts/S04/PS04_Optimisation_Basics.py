'''
check for duplicates in a list 
input:[1,2,3,4,5,1]
output:true 

input:[1,2,3,4,5]
output:False
''' 
'''
def check_duplicates(li):
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if li[i]==li[j]:
                return True 
    return False
li=list(map(int,input().split()))
print(check_duplicates(li))
#Time_Complexity:O(n^2)
'''
#reduced_time_complexity
''' 
def check_duplicates(li):
    s=set()
    for ele in li:
        if ele in s:
            return True 
        s.add(ele)
    return False 
li=list(map(int,input().split()))
print(check_duplicates(li))    

#Time_Complexity:O(n)
'''