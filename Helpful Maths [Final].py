usr_in = input()
a = usr_in.replace('+', '')

lst = []
for x in range(len(a)):
    lst.append(a[x])

new_lst = sorted(lst)
b = '+'.join(new_lst)

print(b)

