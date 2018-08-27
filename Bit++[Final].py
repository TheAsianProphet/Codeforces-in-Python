a = int(input())
Dictionary = {}
counter = 0
while counter <= a - 1:
    Dictionary[counter] = input()
    counter += 1

fin_val = 0

for x in Dictionary:
    if Dictionary[x] == "X++" or Dictionary[x] == "++X":
        fin_val += 1
    elif Dictionary[x] == "X--" or Dictionary[x] == "--X":
        fin_val -= 1
        
print(fin_val)