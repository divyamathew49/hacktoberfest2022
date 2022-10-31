# quick sort IN PYTHON 
def quick(a):
    if len(a)<=1:
        return a
    else:
        p=a.pop()
    
    l=[]
    r=[]
    
    for i in a:
        if i>p:
            r.append(i)
        else:
            l.append(i)
    return quick(l)+[p]+quick(r)
n=int(input("enter the no of elements"))
a=[]
for j in range(0,n):
    k=int(input())
    a.append(k)
a=quick(a)
print(a)
