#binary search that also finds where a number would go in an array if it is not there.

def binary_search(n,L):
    if len(L)==1 and L[0]==n:
        return 0
    elif len(L)==1 and L[0]<n:
        return 1
    elif len(L)==1 and L[0]>n:
        return 0
    half=len(L)//2
    if n<L[half]:
        return binary_search(n,L[:half])
    else:
        return half+binary_search(n,L[half:])


L=[1,2,3,5,6]
print(binary_search(3,L))
