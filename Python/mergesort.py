#merge sort IN PYTHON 
def merge(a):
 if(len(a)>1):    
    mid=len(a)//2
    l=a[:mid]
    r=a[mid:]
    merge(l)
    merge(r)
    i=j=k=0
    while(i<len(l)  and j<len(r)):
        if(l[i]<r[j]):
            a[k]=l[i]
            i=i+1 
        else:
            a[k]=r[j]
            j=j+1
        k=k+1 
    while(i<len(l)):
        a[k]=l[i]
        i=i+1 
        k=k+1 
    while(j<len(r)):
        a[k]=r[j]
        j=j+1 
        k=k+1 
        
n=int(input("enter the no of elements"))
a=[]
for j in range(0,n):
    k=int(input())
    a.append(k)
merge(a)
print(a)
