a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))

temp = a
a = c
c = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)
print("c =", c)