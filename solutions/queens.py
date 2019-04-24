input = open("../sample_data/queens.txt", "r")
lines = input.readlines()
row_nums = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}
queens = [l.strip() for l in lines[1:]]
found = False

for i in range(len(queens)):
    for j in range(i+1, len(queens)):
        row_i = row_nums[queens[i][0]]
        row_j = row_nums[queens[j][0]]
        col_i = int(queens[i][1])
        col_j = int(queens[j][1])
        if row_i == row_j or col_i == col_j or abs(row_i - row_j) == abs(col_i - col_j):
            found = True

print(found)


