
import re

while True:
    print("\n--- INPUT VALIDATION SYSTEM ---")
    print("1. Validate Email")
    print("2. Validate Phone Number")
    print("3. Extract Transaction IDs")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        email = input("Enter email address: ")

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        if re.fullmatch(pattern, email):
            print("Valid email address")
        else:
            print("Invalid email address")

    elif choice == "2":
        phone = input("Enter 10-digit mobile number: ")

        pattern = r"[6-9]\d{9}"

        if re.fullmatch(pattern, phone):
            print("Valid phone number")
        else:
            print("Invalid phone number")

    elif choice == "3":
        log = input("Enter log message: ")

        pattern = r"\bTXN\d+\b"
        ids = re.findall(pattern, log)

        if ids:
            print("Transaction IDs found:")
            for txn in ids:
                print(txn)
        else:
            print("No transaction IDs found")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
