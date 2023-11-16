# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invlaid)
def validate( block_data ):
  # Check whether the centre block is a bomb, a number, or an invalid input
  # Skip bombs, send an error on invalid input, verify numbers

  return


grid = [
  [-1,1,0],
  [1,1,0],
  [0,0,0]
]
print (validate(grid))

mine_count = sum(row.count(-1) for row in grid)
if grid[1][1] != -1 or mine_count != 1:
        return False
for i in range(3):
      for j in range(3):
        if grid[i][j] != -1:
           count = 0
          for x in range(max(0, i - 1), min(3, i + 2)):
             for y in range(max(0, j - 1), min(3, j + 2)):
               if grid[x][y] == -1:
                count += 1
                if int(grid[i][j]) != count:
return False
return True

block = [
    [1, -1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

result = validate_minesweeper_block(block)
print(result)
