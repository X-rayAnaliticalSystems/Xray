# spectra maker for origin
#created by Dr. Valeriy M. Raznomazov
# Rostov-on-Don, 2016
#=======================================================
import xray
import matplotlib.pyplot as plt
import numpy
import math
#=======================================================
word='Data:'
count=0
E=0
E1=5.41 # Crome
E2=17.42 #Molibdenium
n1=305
n2=972
A1=[]
A2=[]
A3=[]
A4=[]
S=[]
#========================================================
f=open ('1.spc')
f2=open ('2.spc')
f3=open ('3.spc')
f4=open ('4.spc')
fs=open ('substrate.spc')
#=======================================================
fo=open('spe.txt', 'w')
#========================================================
fo.write('Chanel'+'\t')
fo.write('Energy'+'\t')
fo.write('Substrate'+'\t')
fo.write('~1~'+'\t')
fo.write('~2~'+'\t')
fo.write('~3~'+'\t')
fo.write('~4~'+'\t')
fo.write('\n')
fo.write('=======================================================')
fo.write('\n')
#========================================================
A1=xray.ReadSpectra(f,word)
A2=xray.ReadSpectra(f2,word)
A3=xray.ReadSpectra(f3,word)
A4=xray.ReadSpectra(f4,word)
S=xray.ReadSpectra(fs,word)
for i in range(len(S)):
    E=xray.CalibEner(count,n1,n2,E1,E2)
    fo.write(str(count)+'\t')
    fo.write(str(E)+'\t')
    fo.write(str(S[count])+'\t')
    fo.write(str(A1[count])+'\t')
    fo.write(str(A2[count])+'\t')
    fo.write(str(A3[count])+'\t')
    fo.write(str(A4[count])+'\t')
    fo.write('\n')
    count=count+1
#=========================================================
f.close
f2.close
f3.close
f4.close
fs.close
fo.close
#========================================================
k=0
B=S
I=[]
count=0
B=numpy.fft.fft(S,n=800)
B[85:750]=0
B[0:5]=0
I=numpy.fft.ifft(B,n=800).real
#Bkgrnd=xray.MovingAverage(20,I)
Bkgrnd=xray.BaCut(10,I)
Bkgrnd2=xray.SigmaFilter(Bkgrnd)
Bkgrnd3=xray.BaCut(80,Bkgrnd2)
Bkgrnd4=xray.SigmaFilter(Bkgrnd3)
Bkgrnd5=xray.BaCut(100,Bkgrnd4)
#========================================================
plt.plot(S)
plt.plot(I, color='red', linewidth=2)
plt.plot(Bkgrnd5,color='green',linewidth=2)
#plt.plot(B)h
#plt.plot(A3)
plt.grid(True)
plt.show()







