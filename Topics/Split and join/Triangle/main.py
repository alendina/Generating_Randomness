triangle_rows = int(input())
triangle_row = ""
for i in range(triangle_rows):
    triangle_row = "#" * (i * 2 + 1)
    print(triangle_row.center(triangle_rows * 2 - 1))
