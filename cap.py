a=raw_input()
n=len(a)
for i in range(0,n):
   if(i==0):
     a[i]=a[0].upper()
   if(a[i]==" "):
     a[i+1]=a[i+1].upper()
print a     
