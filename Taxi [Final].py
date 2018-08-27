""" def taxi(groups, students):
    int_lst = []
    for val in students:
        int_lst.append(int(val))
        
    sum_std = sum(int_lst)
    modulo_std = sum_std // 4
    if modulo_std == sum_std / 4:
        return modulo_std
    else:
        return modulo_std + 1
    
        

a = taxi(input(),input().split())
print(a)
    """
def numerate_lst(groups, students):
    int_lst = []
    for val in students:
        int_lst.append(int(val))
    return int_lst

def count_ones(lst):
    lst_one = []
    lst_two = []

    lst_length = len(lst)
    for x in range(lst_length):
        if lst[x] == 1:
            lst_one.append(lst[x])
        elif lst[x] == 2:
            lst_two.append(lst[x])
    return lst_one, lst_two

def solve_cab(int_lst, lst_uno, lst_dos):
    lst_one = lst_uno
    lst_two = lst_dos
    
    counter = 0
    lst_length = len(int_lst)
    for x in range(lst_length):
        if int_lst[x] == 4:
            counter += 1
        elif int_lst[x] == 3:
            if len(lst_one) >= 1:
                lst_one.pop()
                counter += 1
            else:
                counter +=1
    for y in int_lst:
        if y == 2:
            if len(lst_two) >= 2:
                lst_two.pop()
                lst_two.pop()
                counter += 1
            elif len(lst_two) == 1:
                if len(lst_one) >= 2:
                    lst_one.pop()
                    lst_one.pop()
                    lst_two.pop()
                    counter += 1
                elif len(lst_one) == 1:
                    lst_one.pop()
                    lst_two.pop()
                    counter += 1
                else:
                    lst_two.pop()
                    counter += 1
    if len(lst_one) != 0:
        mod_one = len(lst_one) // 4
        if mod_one == len(lst_one) / 4:
            counter += mod_one
        else:
            counter += mod_one + 1
    
    return counter






a = numerate_lst(input(), input().split())
b = count_ones(a)
c = solve_cab(a, b[0], b[1])
print(c)