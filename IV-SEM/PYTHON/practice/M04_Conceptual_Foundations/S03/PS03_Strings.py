#string:collection of characters enclosed '' or " "or ''' ''' or """ """
#string is immutable    
'''
s="python"
print(s[2])
print(s[1:])
print(s.capitalize())
print(s)
#s[0]='P'
s=s.replace('p','P')
'''
'''
#reversing a string without using built-in function and slice operator 
st=input()
res=""
stop=-1*(len(st)+1)
for i in range(-1,stop,-1):
    res+=st[i]
print(res)    
'''
def reverse_string(st):
    res1=""
    for ch in st:
        res1=ch+res1
    return res1
print(reverse_string("abc"))
def is_palindrome(st):
    return st==reverse_string(st)    
print(is_palindrome("aba"))
print(is_palindrome("abc"))
def fequency_count(st):
    d={}
    for ch in st:
        if ch not in d:
            d[ch]=1
        else:
            d[ch]+=1
    return d
print(fequency_count("abcabc"))
 def is_Anagram(st1,st2):
    return fequency_count(st1)==fequency_count(st2)
print(is_Anagram("space","paces"))
print(is_Anagram("abc","aabcabc"))