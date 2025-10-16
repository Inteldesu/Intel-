
age = int(input("Enter age: "))
is_student = input("Is student? (True/False): ").lower() == "true"

base_price = 12
discount = 0

if age <= 12:
    discount = 3
elif age >= 65:
    discount = 4
elif is_student:
    discount = 2

final_price = base_price - discount
print(f"Your ticket price is ${final_price}.")

correct_username = "intel"
correct_password = "intel"
is_2fa_enabled = True
correct_2fa_code = "123456"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if is_2fa_enabled:
    input_2fa_code = input("Enter 2FA code: ")
    if (input_username == correct_username and
            input_password == correct_password and
            input_2fa_code == correct_2fa_code):
        print("Login successful!")
    else:
        print("Login failed!")
else:
    if (input_username == correct_username and
            input_password == correct_password):
        print("Login successful!")
    else:
        print("Login failed!")
