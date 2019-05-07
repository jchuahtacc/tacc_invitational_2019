#!/usr/bin/env python

input = open("../sample_data/smithwaterman.dat", "r")
lines = input.readlines()

while len(lines) > 0:
    tokens = lines[0].split()
    row_count = int(tokens[0])
    column_count = int(tokens[2])
    col_sequence = [ acid.strip() for acid in lines[1].split()[1:] ]
    rows = [ line for line in lines[2:row_count + 2]]
    row_sequence = [ line[0] for line in rows ]
    matrix = [ [ int(cell.strip()) for cell in row.split()[1:] ] for row in rows ]
    max_value = max( [ max(row) for row in matrix ] )
    row_i = 0
    col_j = 0
    for row in matrix:
        if max_value in row:
            row_i = matrix.index(row)
            col_j = row.index(max_value)
    row_sequence_match = row_sequence[row_i]
    col_sequence_match = col_sequence[col_j]
    while row_i != 0 and col_j != 0:
        if matrix[row_i - 1][col_j - 1] > max([ matrix[row_i - 1][col_j], matrix[row_i][col_j - 1] ]):
            row_i -= 1
            col_j -= 1
            row_sequence_match = row_sequence[row_i] + row_sequence_match
            col_sequence_match = col_sequence[col_j] + col_sequence_match
        elif matrix[row_i - 1][col_j] > matrix[row_i][col_j - 1]:
            row_i -= 1
            row_sequence_match = row_sequence[row_i] + row_sequence_match
            col_sequence_match = "-" + col_sequence_match
        else:
            col_j -= 1
            row_sequence_match = "-" + row_sequence_match
            col_sequence_match = col_sequence[col_j] + col_sequence_match
    print("ROW " + row_sequence_match)
    print("COLUMN " + col_sequence_match)
    lines = lines[row_count + 2:]

