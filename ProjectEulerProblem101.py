#Project Euler: Problem 101
#Problem URL: https://projecteuler.net/problem=101
#Problem Summary: Given a series of numbers produced by a polynomial, guess the the polynomial. If given the right number of terms, I
#should be able to produce the actual polynomial. The Project Euler problem asks for us to guess a polynomial with only 1 term in the
#series, then 2 then iterate until it is correct. Then we take each incorrect polynomial guesses and have it guess the next term beyond 
#the series it was guessed from. So if the polynomial was guessed after 3 terms we need to use that polynomial to guess the 4th. Then we
#sum all of those incorrectly guessed terms and plug them into the Project Eueler site. This problem is done for a series produced by:
#F(n)=1.-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10

#Thoughts: I am getting an incorrect sum of fits despite getting the correct polynomial. I think there might be a typing issue since my 
#function works with floats and Project Euler is asking for int. Since the coefficients of the polynomial get large at some point I think
#there the numbers are skewed due to the nature of large floats. If the scipy.linalg.solve() did row reduction then it would be capable 
#of maintaining integers. It seems that this program solves the linear equations using the inverse matrix which has a coefficient that
#is calculated as a float.

import numpy as np
import scipy.linalg


def main():
    n=1                  #input into function
    nextGuess=0          #next guess
    FIT=[]               #First Incorrect Terms list
    SumFIT=0             #sum of the FITs
    knownElements=[]     #list of known elements of the series
    NextUn=-1            #initializing Next
    
    while(np.int(nextGuess)!=np.int(NextUn)):
        #The "given" new term is generated with this polynomial.
        CurrentUn=1.-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
        
        #Add the new "given" term to the knownElements list.
        knownElements.append(CurrentUn)
        
        nextGuess=OP(knownElements,n)
        
        #Check to see if we guess the next term correctly.
        n+=1
        NextUn=1.-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
        
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

#Create a matrix where rows are inputted values of n and columns are a term in the polynomial.
#Treat the variable n as a known. We know it will be 1,2,3,... when producing the series terms. I am treating n as the known portion of 
#the functions and the coefficients of the polynomials as the unknowns.
def createMatrix(n):
    #make empty matrix
    U=np.empty([n,n])
    #make matrix of coefficients
    for y in range(n):
        for x in range(n):
            U[y][x]=(y+1)**x

    return U

#Solve the matrix and produce a guess for the next "unknown" term.
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
