code = input()
col = "abcdefgh".find(code[0])
row = int(code[1]) - 1
max_num = 8
moves = ((2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))

answer = 0
for col_move, row_move in moves:
    new_col = col + col_move
    new_row = row + row_move
    if 0 <= new_col < max_num and 0 <= new_row < max_num:
        answer += 1
print(answer)
