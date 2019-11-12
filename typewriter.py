#! /usr/bin/env python3
import time


def typewriter(array="Hello There!",interval=0.005):
    newarray=[]
    time.sleep(interval*50)         
    for c in array:
        newarray.append(" ")
        while newarray[-1]!=c :
            newarray[-1]=chr(ord(newarray[-1]) + 1)
            print(newarray[-1],end="\b",flush=True)
            time.sleep(interval)         
        print(newarray[-1],end="")

def print_writer(string="Welcome to",typew="TypeWriter!",interval=0.005):
    print()
    print(string,end=' ',flush=True)
    typewriter(typew,interval)
    print("\n")

if __name__=="__main__":
    print_writer()
