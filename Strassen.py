
def add(A,B):
    n=len(A)
    C=[[0 for j in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j]=A[i][j]+B[i][j]
    return C

def sub(A,B):
    n=len(A)
    C=[[0 for j in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j]=A[i][j]-B[i][j]
    return C

def nextPowerOf2(n):
    count = 0;
    if (n and not(n&(n-1))):
        return n
    while( n != 0):
        n >>= 1
        count += 1
    return 1 << count;

def strassen(A,B):
    n=len(A)
    C=[[0]]
    if n==1:
        C[0][0]=A[0][0]*B[0][0]
        return C
    else:
        newsize=int(n//2)
        C=[[0 for j in range(n)]for i in range(n)]
        a11=[[0 for j in range(newsize)]for i in range(newsize)]
        a12=[[0 for j in range(newsize)]for i in range(newsize)]
        a21=[[0 for j in range(newsize)]for i in range(newsize)]
        a22=[[0 for j in range(newsize)]for i in range(newsize)]

        b11=[[0 for j in range(newsize)]for i in range(newsize)]
        b12=[[0 for j in range(newsize)]for i in range(newsize)]
        b21=[[0 for j in range(newsize)]for i in range(newsize)]
        b22=[[0 for j in range(newsize)]for i in range(newsize)]

        for i in range(newsize):
            for j in range(newsize):
                a11[i][j]=A[i][j]
                a12[i][j]=A[i][j+newsize]
                a21[i][j]=A[i+newsize][j]
                a22[i][j]=A[i+newsize][j+newsize]

                b11[i][j]=B[i][j]
                b12[i][j]=B[i][j+newsize]
                b21[i][j]=B[i+newsize][j]
                b22[i][j]=B[i+newsize][j+newsize]

        s1=sub(b12,b22)
        s2=add(a11,a12)
        s3=add(a21,a22)
        s4=sub(b21,b11)
        s5=add(a11,a22)
        s6=add(b11,b22)
        s7=sub(a12,a22)
        s8=add(b21,b22)
        s9=sub(a11,a21)
        s10=add(b11,b12)

        p1=strassen(a11,s1)
        p2=strassen(s2,b22)
        p3=strassen(s3,b11)
        p4=strassen(a22,s4)
        p5=strassen(s5,s6)
        p6=strassen(s7,s8)
        p7=strassen(s9,s10)

        c11=sub(add(add(p5,p4),p6),p2)
        c12=add(p1,p2)
        c21=add(p3,p4)
        c22=sub(sub(add(p1,p5),p3),p7)

        for i in range(newsize):
            for j in range(newsize):
                C[i][j]=c11[i][j]
                C[i][j+newsize]=c12[i][j]
                C[i+newsize][j]=c21[i][j]
                C[i+newsize][j+newsize]=c22[i][j]

        return C
        
def printMatrix(C):
    for line in C:
        print ("\t".join(map(str,line)))
    

def Multiply():
    l1=int(input("Number of rows of first matrix:"))
    l2=int(input("Number of columns of first matrix:"))
    l3=int(input("Number of columns of second matrix:"))
    n=max(l1,l2,l3)
    n=nextPowerOf2(n)

    A=[]
    B=[]

    d2=n-l2
    d3=n-l3

    print("First Matrix:")
    for i in range(n):
        if i<l1:
            y=input()
            l=[int(x) for x in y.split()]
            if d2>0:
                for k in range(d2):
                    l.append(0)
            A.append(l)
        else:
            l=[0 for j in range(n)]
            A.append(l)
        
    
    print("Second Matrix:")
    for i in range(n):
        if i<l2:
            y=input()
            l=[int(x) for x in y.split()]
            if d3>0:
                for k in range(d3):
                    l.append(0)
            B.append(l)
        else:
            l=[0 for j in range(n)]
            B.append(l)


    T=strassen(A,B)
    C=[[0 for j in range(l3)]for i in range(l1)]
    for i in range(l1):
        for j in range(l3):
            C[i][j]=T[i][j]
    print("Multiplication Matrix of the given 2 Matrices is:")
    printMatrix(C)

def Population():
    n=int(input("Enter number of Age Categories:"))
    print ("Enter details in the format:")
    print ("No. of Lizards Alive\tNo. Dying during interval\tMean no. of offsprings per female")
    P=[]
    for i in range(n):
        #print("Age Category ",i+1)
        a=input()
        l=[float(x) for x in a.split()]
        P.append(l)
    M1=[[0 for j in range(n)]for i in range(n)]
    M2=[[0 for j in range(n)]for i in range(n)]
    for i in range(n):
        M2[i][0]=P[i][0]
    S=[]
    for i in range(n-1):
        k=(P[i][0]-P[i][1])/P[i][0]
        k=round(k,3)
        S.append(k)
    for i in range(n):
        M1[0][i]=P[i][2]
    for i in range(n-1):
        M1[i+1][i]=S[i]
    print("Leslie Matrix:")
    printMatrix(M1)
    Final=strassen(M1,M2)
    print("Population Matrix in the next Time Period:")
    for i in range(n):
        print(int(Final[i][0]))

g=int(input("For Multiplication of Matrix, Press 0\nFor Population Growth Analysis, Press 1\n"))
if (g==0):
    Multiply()
elif (g==1):
    Population()

