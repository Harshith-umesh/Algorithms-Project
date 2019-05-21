en=input()
l=len(en)
de=""
no=0
c=0
for i in range(0,l,4):
    no=0
    c=0
    for j in range(0,4):
        if(en[i+j]!='='):
            no=no<<6
            c+=6
        if(en[i+j]>='A' and en[i+j]<='Z'):
            no=no|(ord(en[i+j])-ord('A'))
        elif(en[i+j]>='a' and en[i+j]<='z'):
            no=no|(ord(en[i+j])-ord('a')+26)
        elif(en[i+j]>='0' and en[i+j]<='9'):
            no=no|(ord(en[i+j])-ord('0')+52)
        elif(en[i+j]=='+'):
            no=no|62
        elif(en[i+j]=='/'):
            no=no|63
        else:
            no=no>>2
            c-=2
    while(c!=0):
        c-=8
        de=de+chr((no>>c)&255)
print(de)
