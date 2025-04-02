
#? Write a function INDEX_TUPLE(T), where T is the list of tuple elements passed as argument to the function.
#? The function returns another list named 'index_list' that stores the indices of all Non-Zero Elements of T.
#* For example, if L contains [12, 4, 0, 11, 0, 56], the index_list should contain [0, 1, 3, 5].

def INDEX_TUPLE(T):
    index_list = []
    
    for i in range(len(T)):
        if T[i] != 0:
            index_list.append(i)
        
    return index_list

L = (13, 14, 0, 17, 0, 0, 9)
print(INDEX_TUPLE(L))
