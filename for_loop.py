






number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]


print("Remember rows/columns also begin at 0")
print(number_grid[1][2])


# =======================
print("\n\n--------------------------")

for row in number_grid:
    for column in row:
        print(column)