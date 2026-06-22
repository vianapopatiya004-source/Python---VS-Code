rows = int(input(" Enter the number of rows and columns:"))
for j in range(1, rows+1):
    for i in range(j):
        print("*", end = " ") 
    print()