phone_number = input("Cellphone number: ")

# Verifica se o número inserido tem 10 dígitos
if len(phone_number) == 11 and phone_number.isdigit():
    formatted_number = f"({phone_number[:2]}) {phone_number[2:7]}-{phone_number[7:]}"
    print("Formatted phone number:", formatted_number)
else:
    print("Invalid phone number. Please enter a 10-digit numeric phone number.")
