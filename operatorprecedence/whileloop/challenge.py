num = int(input("Enter a number: "))

num_str = str(num)         
power = len(num_str)        

print("Number of digits =", power)

sum = 0

for digit in num_str:
    sum += int(digit) ** power

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")