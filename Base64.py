chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
inp=input()
l=len(inp)
encoded=""
ind=0
for i in range(0,l,3):
    val=0
    no=0
    c=0
    for j in range(i,i+3):
        if(j==l):
            break
        val=val<<8
        val=val|ord(inp[j])
        c+=1
    no=c*8
    padding=no%3
    while(no!=0):
        if(no>=6):
            temp=no-6
            ind=(val>>temp)&63
            no-=6
        else:
            temp=6-no
            ind=(val<<temp)&63
            no=0
        encoded=encoded+chars[ind]
for i in range(1,padding+1):
    encoded=encoded+"="
print("input:",inp)
print("Encoded:",encoded)