# http://codeforces.com/problemset/problem/231/A

number = int(input())
dict = {}
counter = 1
while counter <= number:
    dict[counter] = input().split()
    counter += 1

solved = 0
for key in dict:
    round = 0
    for file in dict[key]:
        if file == '1':
            round += 1
    if round >= 2:
        solved += 1

print(solved)
