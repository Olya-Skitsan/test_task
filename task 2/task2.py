# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 21:45:27 2020

@author: Sam
"""


Fin = open ("C:\\Users\\Sam\\Desktop\\task 2\\input.txt") #path to input file
Fout = open ("C:\\Users\\Sam\\Desktop\\task 2\\output.txt", "w") #path to output file,
#w -opening for writing, the contents of the file are deleted,
#if the file does not exist, a new one is created.
list = Fin.readline().split() #read input
N, x, y = int(list[0]),int(list[1]),int(list[2]) #reading a file in parts
t = 0 #initial number of possible time
t += min(x,y) #define a fast xerox and make the first copy
slower = max(x,y) #start a slow xerox
i = 0 #initial condition for i
for i in range(0, i >= N): #simulated flow of time, t goes in steps of min (x, y)
    slower -= min(x,y) #slow xerox already printed some part of the document
    if(slower <= 0): #if a slow copy machine has already printed a document
        i += 1 #then count it
slower = max(x,y) #send another print
t += max(x,y)
with open("C:\\Users\\Sam\\Desktop\\task 2\\output.txt", "w") as file: #open file output.txt for writting
             Fout.write(str(t+1)) #write response to file output.txt, taking into account the original document
Fout.close() #file output.txt closing
Fin.close() #file input.txt closing          