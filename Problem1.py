
def encode(s, n):
    newS = ""
     
    for i in range(len(s)):
        val = ord(s[i])
        dup = n
        if val + n>122:
            n -= (122-val)
            n = n % 26
            newS += chr(96 + n)
             
        else:
            newS += chr(val + n)
         
        n = dup
    print (newS)
    
str = 'ZAB'
n = 1
 
encode(str, n)
