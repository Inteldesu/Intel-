a = 18
b = 9

print(f"a = {a}, b = {b}")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Floating-Point Division: {a / b}")
print(f"Integer Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ^ b}")

result1 = 5 + 3 * 2
result2 = (5 + 3) * 2
result3 = 10 % 3 + 5 * 2

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}")

inches = int(input("Enter the number of inches: "))
feet = inches // 12
remaining_inches = inches % 12

print(f"{inches} inches is equal to {feet} feet and {remaining_inches} inches.")
