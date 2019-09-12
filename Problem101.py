#Problem 101

import numpy as np
import scipy.linalg


def main():
    #1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
    n=1                  #input into function
    nextGuess=0          #next guess
    FIT=[]               #first incorrect terms
    SumFIT=0
    knownElements=[]
    NextUn=-1
    while(np.int(nextGuess)!=np.int(NextUn)):
        #1.-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
        CurrentUn=1.-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10

        knownElements.append(CurrentUn)
        nextGuess=OP(knownElements,n)
        
        n+=1
        
        NextUn=1.-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
        #print nextGuess,NextUn,nextGuess==NextUn,type(nextGuess),type(np.float64(NextUn))
        
        #if the next guess is wrong then add the wrong guess to FIT (first incorrect term)
        if nextGuess!=NextUn:
            print"ADD"
            FIT.append(nextGuess)
            #sum the FITs
            SumFIT+=nextGuess
        if(nextGuess==NextUn):
            print "TRUE"
        #print n,NextUn
    print"--------------"
    print FIT
    print SumFIT


def createMatrix(n):
    #make empty matrix
    U=np.empty([n,n])
    #make matrix of coefficients
    for y in range(n):
        for x in range(n):
            U[y][x]=(y+1)**x

    return U

def OP(knownElements,n):
    #solving Ax=B
    A=createMatrix(n)
    B=knownElements
    X=scipy.linalg.solve(A,B)
    #create guess
    nextGuess=0
    for i in range(n):
        nextGuess+=X[i]*((n+1)**i)
    print X
    return nextGuess
    
main()