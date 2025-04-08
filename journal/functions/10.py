
#? Write a function INDEX_TUPLE(T), where T is the list of tuple elements passed as argument to the function.
#? The function returns another list named 'indexList' that stores the indices of all Non-Zero Elements of T.
#* For example, if L contains [12, 4, 0, 11, 0, 56], the indexList should contain [0, 1, 3, 5].

def INDEX_TUPLE(T):
    indexList = []
    
    for i in range(len(T)):
        if T[i] != 0:
            indexList.append(i)
        
    return indexList

L = (13, 14, 0, 17, 0, 0, 9)
print(INDEX_TUPLE(L))
