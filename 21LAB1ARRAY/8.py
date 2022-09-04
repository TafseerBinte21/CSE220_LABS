def repeatarray (array):
    repeat = [None] * len(array)

    for i in range(0, len(array)-1):
        count = 1
        sameValue = False
        for k in range(i-1,-1,-1):
            if array[i] == array[k]:
                sameValue = True
                break
        if not sameValue:
            for j in range(i+1, len(array)):
                if(array[i] == array[j]):
                    count = count + 1
            if count != 1:
                repeat[i] = count
    for i in range(len(repeat)-1):
        if repeat[i] != None:
            for j in range(i+1,len(repeat)):
              if repeat[i] == repeat[j]:
                  return True
    return False
    



array= [2,4,2,2,1,6,6,6,6,5,4]
print(repeatarray(array))
