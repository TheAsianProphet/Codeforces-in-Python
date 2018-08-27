# http://codeforces.com/problemset/problem/118/A

case = list(input().lower())
vowels = ["a", "e", "i", "o", "u", "y"]

result = []
for i in case:
    if i not in vowels:
        result += i

final = []
for x in result:
    final.append('.')
    final.append(x)

string = ''.join(final)
print(string)
