def CalibEner (count,n1,n2,E1,E2):
    A=(float(count)-n1)/(n2-n1)
    B=(E1)/(E2-E1)
    C=E2-E1
    E=(A+B)*C
    return float(E)
def ReadSpectra(f,word):
    F=[]
    flag=0
    for line in f:
        if word in line:flag=1
        if (flag == 1) and (not word in line):
            I=line.split()
            for i in I:F.append(int(i))
    return F
def BaCut(intrvl,B):#cutting with 3 sigma filter
    from math import sqrt as sqr
    count=0#point of spectrum counter
    x = 1
    CB=[]#cutted spectrum
    for i in range(len(B)):#for even point of spectrum step by step
        j=0
        summ=0.0
        while j<intrvl:
            if (count-j)<2048-intrvl:y=float(B[count-j])
            else:y=x
            summ=summ+y
            j=j+1
        x=round(summ/intrvl)
        CB.append(x)
        count=count+1
    return CB
def MovingAverage(intrvl,CB):#simple moving average
    SCB=[]
    count=0
    intrvl_s=15*intrvl
    for i in range(len(CB)):
        j=0
        summ=0.0
        while j<intrvl:
            if (count-j)<2048-intrvl_s:y=float(CB[count-j])
            else:y=float(CB[j])
            summ=summ+y
            j=j+1
        x=round(summ/intrvl)
        SCB.append(round(x))
        count=count+1
    return SCB
def difSp(F,CB):
    D=[]
    count=0
    for i in range(len(F)):
        D.append((F[count]-CB[count]))
        count=count+1
    return D
def SigmaFilter(A):
    count=0
    import math
    B=[]
    count=0
    sum=0
    for i in range(len(A)):
        B.append(A[count]-(min(A)))
        print(B[count])
        sum=sum+B[count]
        count=count+1
    sigma=3*math.sqrt(sum/len(A))
    count=0
    #print(sum,len(A))
    for i in range(len(A)):
        #print(B[count],sigma)
        if B[count]>sigma+(sum/len(A)):B[count]=(sum/len(A))
        B[count]=B[count]+min(A)
        count=count+1
    return B





