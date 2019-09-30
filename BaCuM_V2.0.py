# Background calculator for origin
#created by Dr. Valeriy M. Raznomazov
# Rostov-on-Don, 2017
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
def BaCut(intrvl,B):
    import math
    count=0
    x=1
    CB=[]
    for i in range(len(B)):
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
def MovingAverage(intrvl,CB):
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

    
    

#=======================================================
import xray
#=======================================================
f=open ('1.spc')
#=======================================================
fo=open('spectrum.txt','w')
#=======================================================
fo.write('Chanel'+'\t')
fo.write('Energy'+'\t')
fo.write('~Impulse~'+'\t')
fo.write('Cutted Impulse'+'t')
fo.write('Background1'+'\t')
fo.write('Background2'+'\t')
#fo.write('Spectrum'+'t')
fo.write('\n')
fo.write('=======================================================')
fo.write('\n')
#=======================================================
count=0
word='Data'
intrvl=30
point=3
b_lvl=5
b_lvl_c=30
intrvl_s=25
A1=[]
B=[]
CB=[]
CB1=[]
D=[]
E=0
E1=5.41 # Crome
E2=17.42 #Molibdenium
n1=305
n2=972
#=======================================================
A1=xray.ReadSpectra(f,word)
B=xray.BaCut(intrvl,A1)
CB=xray.BaCut(intrvl,B)
CB1=xray.BaCut(intrvl,CB)
#CB1=xray.MovingAverage(intrvl,point,CB)
#print(range(CB1))
#D=xray.difSp(A1,CB)
if not(A1[61]==B[61]): print('All right!')

#=======================================================
count=0
for i in range(len(A1)):
    E=xray.CalibEner(count,n1,n2,E1,E2)
    fo.write(str(count)+'\t')
    fo.write(str(E)+'\t')
    fo.write(str(A1[count])+'\t')
    fo.write(str(B[count])+'\t')
    fo.write(str(CB[count])+'\t')
    fo.write(str(CB1[count])+'\t')
    #fo.write(str(D[count])+'\t')
    fo.write('\n')
    count=count+1
#========================================================
f.close
fo.close
