rows = int(input(" Enter the number of rows and columns:"))
num = 1 
for j in range(1, rows+1):
    for i in range(j):
        print(num, end = " ") 
        num= num + 1
    print()