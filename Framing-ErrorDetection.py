# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 12:32:39 2020
101010000101010111111110001010100101110001111110
1010100001010100001010100101110001111110
10101000 01010101 01111010 00101010 01011100 00000010
['0b10101000', '0b1010101', '0b1111010', '0b101010', '0b1011100', '0b0', '0b10']
@author: iNaz

 10101000    0 10101010     11110100010101001011100
[10101000', '0b1010101', '0b1111010', '0b101010', '0b1011100']
chand daste 5


"""
import textwrap
import random


#Sender:
#1.get data 
#2.devide to 8 bit chunks
#3.sum
#4.complement
#5.add edc
#6.add flag and escape

####################################Sender#####################################
#1.get data 
# 1010100001010101111111100010101001011100
# 1010100001010101011110100010101001011100
n = input("Input your data: ")

#2.devide to 8 bit chunks
x = list( textwrap.wrap(n, 8))
print( "\nParts:",  x )

#3.sum
summ = 0
for i in range( 0 , len(x)):
     summ = summ + int(x[i] , 2)
     #print( summ )
    
binary_sum = bin(summ)
edcn = (binary_sum)[-8:]
print("Binary sum:",edcn)

#4.complement
edc = edcn.replace('1', '2').replace('0', '1').replace('2', '0')
print("EDC =",edc,"\n")

#5.add edc
z=n+edc



#6.add flag and escape

if(z.find('00000000')!= -1):
    zn = z.replace("00000000","0000000000000000")
if(z.find('11111111')!= -1):
    zn = z.replace("11111111","0000000011111111")
    
fzf = '11111111'+zn+'11111111'

#Frame:
print("Frame:\n",fzf)
print("________________________\n")

###############################Create error####################################
items = ['0', '1']

x = random.sample(items,  1)  
print("Change the 9th bit to :", x[0])
fzfl = [str(i) for i in str(fzf)]
fzfl[9]=x[0] #random kon
fzfs = ''.join([str(elem) for elem in fzfl])
print("Sent:",fzf) 
print("Received:",fzfs)
print("Sent = Received : ",fzf is fzfs)

#Receiver
#1.Remove flags and escape bits(what was the main data?)
#2.calculate edc'
#3.check if data was correct
#################################Receiver#######################################

#1.Remove flags and escape bits(what was the main data?)
esc = False
count1 = 0
count0 = 0
gum = 0

temp=[]
fzfn=fzfs
for i in fzfs:
       
    #print(gum ,":",i)
    if (i == '1'):
        count0 = 0
        count1 +=1
       
        if (count1 == 8 and esc == False):  
            
            count1 = 0
            
            print("eight 1's , esc F ")
            print("delete: ",gum-7," - ", gum+1)
            temp.append(gum-7)
            temp.append(gum+1)
            #print(fzfn)
            
        elif ( count1 == 8 and esc == True):
            
            esc = False
            print("eight 1's , esc T bud")
            count1 = 0
            
    elif (i == '0'):
        count1 = 0
        count0 +=1
        
        if (count0 == 8 and esc == False):
            
            esc = True
            print("eight 0's , esc F ")
            print("delete: ",gum-7," - ", gum+1)
            temp.append(gum-7)
            temp.append(gum+1)
            
            #print(fzfn)
            count0 = 0
            
        elif(count0 == 8 and esc == True):
            print("eight 0's , esc T ")
            esc = False
            count0 = 0
            
    gum +=1      

bar=0
print(temp)
for i in range(0, len(temp), 2):
  

    print ("temp",i)
    print("delete:",temp[i],"-",temp[i+1])
    fzfs = fzfs[:temp[i]-bar] +  fzfs[temp[i+1]-bar:]
    bar+=8
    print(fzfs)
    
print("Main data" , fzfs)


#2.calculate edc'
xn = list( textwrap.wrap(fzfs, 8))

summn = 0

print ("xn",xn)

for i in range(0, len(xn)):
     summn = summn + int(xn[i],2)   

binary_sumn = bin(summn)
#print(binary_sumn)
edcnn = (binary_sumn)[-8:]
print(edcnn)

#3.check if data was correct
if (edcnn =='11111111'):
    print("Correct")
else:
    print("Error")