# http://codeforces.com/problemset/problem/50/A

game_board = input().split()

X = int(game_board[0])
Y = int(game_board[1])

board_size = X * Y

if board_size % 2 == 0:
    ans1 = board_size / 2
    print(int(ans1))
else:
    ans2 = (board_size - 1) / 2
    print(int(ans2))

