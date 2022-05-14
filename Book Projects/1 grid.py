grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(len(grid)):
    # grid[i] so python doesn't include the rows since we make it anonymous using i
    print(grid[i][0], end='')
print()
for i in range(len(grid)):
    # end='': To remove spacing in the for loop print output
    print(grid[i][1], end='')
# To allow the next print statement be on a new line due the end='' keyword
print()
for i in range(len(grid)):
    print(grid[i][2], end='')
print()
for i in range(len(grid)):
    print(grid[i][3], end='')
print()
for i in range(len(grid)):
    print(grid[i][4], end='')
print()
for i in range(len(grid)):
    print(grid[i][5], end='')
print()
# OR
'''print('\n'.join(map(''.join, zip(*grid))))
The zip(*grid) effectively transposes the matrix (flip it on the main diagonal), then each row is joined into 
one string, then the rows are joined with newlines so the whole thing can be printed at once.'''
# OR
'''rows = len(grid) # len(grid)Number of elements in the list
cols = len(grid[0]) # we indexed only the columns so python prints that only

for j in range(cols):
    for i in range(rows):
        print(grid[i][j], end='')
    print()'''  # so everything is not printed on one line due to the end='' keyword
