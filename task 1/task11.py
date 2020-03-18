# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:25:13 2020
"""

Fin = open ("C:\\Users\\Sam\\Desktop\\input.txt") #path to input file
Fout = open ("C:\\Users\\Sam\\Desktop\\output.txt", "w") #path to output file,
#w -opening for writing, the contents of the file are deleted,
#if the file does not exist, a new one is created.
list = Fin.readline().split() #read input
sum = 0 #initial number of possible gifts
X, Y, Z, W = int(list[0]),int(list[1]),int(list[2]),int(list[3]) #reading a file in parts
for i in range(0, W // X + 1): #we find the quotient of the total weight for X
   for j in range(0 , (W - (X * i)) // Y + 1): #from the remaining W we find the quotient integer for Y
        if (W - (X * i + Y * j)) % Z == 0: #enumeration of possible options
            sum += 1 #number of possible gifts
with open("C:\\Users\\Sam\\Desktop\\output.txt", "w") as file: #open file output.txt for writting
             Fout.write(str(sum)) #write response to file output.txt
Fout.close() #file output.txt closing
Fin.close() #file input.txt closing
