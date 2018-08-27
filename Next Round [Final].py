# http://codeforces.com/problemset/problem/158/A

first_i = input().split()
second_i = input().split()

adv_pos = int(first_i[1])  # advancee position
list_pos = adv_pos - 1  # list position index

score_pos = int(second_i[list_pos])  # score of position index

counter = 0

while counter == 0:
    if score_pos >= 1:
        counter += adv_pos
    else:
        index_val = second_i.index('0')
        counter += index_val
        break

for i in second_i[list_pos + 1:]:
    if int(i) >= 1:
        if i == second_i[list_pos]:
            counter += 1

print(counter)