
while True:
    month_to_search = input("Birthday Month number: ")

    # Create condition for look for only months
    months = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

    if month_to_search in months:
        break
    else:
        print("Invalid value!")


print("ok")