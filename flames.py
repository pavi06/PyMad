print("--Flames--")
def check(s1,s2):
    i=0
    while(i<len(s1)):
        if s1[i] in s2:
            if i+1<len(s1):
                s1=s1[:i]+s1[i+1:]
            else:
                s1=s1[:i]
            if i+1<len(s2):
                s2=s2[:i]+s2[i+1:]
            else:
                s2=s2[:i]
        i+=1
    return len(s1)+len(s2)
    
s1=input().strip().lower().replace(" ","")
s2=input().strip().lower().replace(" ","")
if(len(s1)<=len(s2)):
    a=check(s1,s2)
else:
    a=check(s2,s1)
l=["Friends","Lovers","Affectionate","Marriage","Enemies","Sisters"]
while(len(l)>1):
    i=(a%len(l))-1
    if i>=0:
        left=l[:i]
        right=l[i+1:]
        l.remove(l[i])
        l=right+left
    else:
        l=l[:i]
print(l[0])
