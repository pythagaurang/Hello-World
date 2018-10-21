import time
array=["H","e","l","l","o"," ","W","o","r","l","d"]
newarray=[]
for i in range(len(array)):
    newarray.insert(i," ")
    while newarray[i]!=array[i] :
        newarray[i]=chr(ord(newarray[i]) + 1)

        for j in range(i+1):
            print newarray[j],
            j=j+1
        
        time.sleep(0.015)
        print("\n\n\n")              
    i+=1
