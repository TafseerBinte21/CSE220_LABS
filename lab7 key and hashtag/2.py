def hashTable(a):
    hashtable=[0]*len(a)

   
    for i in a:
        consCount=0
        sum=0
        v=['A','E','I','O','U']
        number=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        for x in i:
            if ord(x)>=65 and ord(x)<=99:
                if x not in v:
                    consCount+=1
            elif x in number:
                sum+=int(x)
        idx= ((consCount*24)+sum)%9
        
        
        while (hashtable[idx%len(a)])!=0:
            idx+=1
        hashtable[idx%len(a)] = i 
    
    return hashtable
            

a=["T2T","PP9","SS3","E10","UV1","12P","EE2","TT4","PO9"]
print(hashTable(a))

