#записываем новый файл в линию
f=open ('fons.dar')
fi=open('spe.txt', 'w')
fi.write('канал'+'\t')
fi.write ('энергия'+'\t')
fi.write('импульсы'+'\t')
fi.write('фон' +'\n')
fi.close

word='Data:'
flag=0
count=0
E=0

print('Bведите номер канала, в котором находится первый пик')
n1=int(input())
print ('Введите номер канала, в котором находится второй пик')
n2=int(input())
print ('Введите инервал усреднения')
interval=int(input())


E1=17.42
E2=19.61

ave=0
bg=0
j=0
summ=0
sum_st=0


for line in f:
    s=str(line)
    if word in line:
        flag=1
    if (flag == 1) and (not word in line):
        I=line.split()

        for i in I:
            count=count+1
            A=(count-n1)/(n2-n1)
            B=(E1)/(E2-E1)
            C=E2-E1
            E=(A+B)*C
            Imp=i
            summ=summ+int(Imp)
            #print(count,ave, ave)
            fi.write(str(count)+'\t')
            fi.write(str(round(E)) + '\t')
            fi.write(Imp+'\t')
            j=j+1
            #print(j)
            if j==interval:
                ave=round(summ/interval)
                bg=3*pow(ave,1/2)
                j=0
                summ=0
            if int(Imp)>ave: fi.write(str(round(ave))+'\n')
            else: fi.write(Imp+'\n')
        #print(ave,sigma)

          
f.close
fi.close
print('файл spe.txt записан и находится в том же каталоге, что и программа EnSpeCali')
#калибровка 
        
            
            
            
            
            
        
        
