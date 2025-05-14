# arithmetic operators
a = 10
b = 20
print("a + b =", a + b)  # addition
print("a - b =", a - b)  # subtraction
print("a * b =", a * b)  # multiplication
print("a / b =", a / b)  # division

# assignment operators
a = 10
b = 20
a += b  # equivalent to a = a + b
print("a =", a)  # a is now 30

# comparison operators
a = 10
b = 20
print("a == b:", a == b)  # false
print("a != b:", a != b)  # true
print("a > b:", a > b)    # false
print("a < b:", a < b)    # true

# logical operators
a = True
b = False
print("a and b:", a and b)  # false
print("a or b:", a or b)    # true 
print("not a:", not a)      # false

# bitwise operators
a = 5  # 1010 in binary
b = 3   # 0100 in binary
print("a & b:", a & b)  # 1
print("a | b:", a | b)  # 7
print("a ^ b:", a ^ b)  # 6
print("~a:", ~a)        # -6
print("a << 1:", a << 1)  # 10