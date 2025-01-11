x = 5
y = 7
print(f"Before swapping: x = {x}, y = {y}")
# Swapping using XOR
x = x ^ y
y = x ^ y
x = x ^ y
print(f"After swapping: x = {x}, y = {y}")