def split_lst(length, order):
    new_lst = []
    for x in range(int(length)):
        new_lst.append(order[x])
    return new_lst

def stone_clr(new_lst):
    new_lst2 = []
    new_lst2.append(new_lst[0])
    counter = 0
    for x in range(len(new_lst)):
        if new_lst[x] != new_lst2[counter]:
            new_lst2.append(new_lst[x])
            counter += 1
    
    final = len(new_lst) - len(new_lst2)
    return final
    
    

a = split_lst(input(), input())
b = stone_clr(a)
print(b)