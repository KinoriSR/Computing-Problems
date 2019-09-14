#For Problem 16 just carry the 10s at the end

def double(Num,n):
    for i in range(n):
        Num[i]=Num[i]*2
        #Carry the 10
    for i in range(n):
        if Num[i]>=10:
            Num[i]-=10
            #No need to account for cases with 9+1 carrying over another 10 because multiplying by 2 cannot yeild 9 with integer digits
            #If not the last digit of the number
            if i<n-1:
                Num[i+1]+=1
            #If the last digit
            else:
                Num=resize(Num)
                Num[i+1]+=1
    return Num

def resize(Num):
    Num.append(0)
    return Num

x=eval(input("Number of doubling:"))
Num=[2]
for i in range(x-1):
    n=len(Num)
    Num=double(Num,n)
    #print (Num)
Sum=0
for i in range(len(Num)):
    Sum+=Num[i]
print (Sum)

