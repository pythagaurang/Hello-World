import time
import os
array=["H","e","l","l","o"," ","W","o","r","l","d"]
newarray=[]
for i in range(len(array)):
    newarray.insert(i," ")
    while newarray[i]!=array[i] :
        os.system('clear')
        newarray[i]=chr(ord(newarray[i]) + 1)
        for j in range(i+1):
            print (newarray[j],end='')
            j=j+1
        print()
        time.sleep(0.015)              
    i+=1
