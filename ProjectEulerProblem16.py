#For Problem 16 from projecteuler.com
#The problem asks for the sum all of the digits 2**n where n is an input from the user. This problem asks for n to be 1000.
#Normal 32-bit and 64bit integers are limited in size to 2**32 and 2**64 scales respectively. Although they can get a bit larger by using 
#their remaining bits, it still was sufficient. I handled the doubling operation within an array that could grow. This allows me to 
#create arbitrarily large powers of 2. I have considered implementing this in C to have more control over bit operations and use of 
#memory. I have yet to explore this.
#This can be used for ala Carte multiplication.

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

