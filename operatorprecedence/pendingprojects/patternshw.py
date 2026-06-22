rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):

    # Left triangle
    for j in range(i):
        print("*", end=" ")

    # Gap between triangles
    for j in range(2 * (rows - i)):
        print(" ", end=" ")

    # Right triangle
    for j in range(i):
        print("*", end=" ")

    print()

    