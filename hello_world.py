#!/usr/bin/env python

import time

array=["H","e","l","l","o"," ","W","o","r","l","d"]
newarray=[]
print()
for c in array:
    newarray.append(" ")
    while newarray[-1]!=c :
        newarray[-1]=chr(ord(newarray[-1]) + 1)
        print(newarray[-1],end="\b",flush=True)
        time.sleep(0.010)         
    print(newarray[-1],end="")
print("\n")
