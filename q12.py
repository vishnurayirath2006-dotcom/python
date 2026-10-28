
# Electricity Bill Calculation using Exception Handling

try:
    units = float(input("Enter electricity units consumed: "))

    if units < 0:
        raise ValueError("Units cannot be negative.")

    if units <= 100:
        bill = units * 1.50

    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)

    else:
        bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)

except ValueError as e:
    print("Invalid input:", e)

else:
    print("Units consumed:", units)
    print("Electricity bill: Rs.", round(bill, 2))

finally:
    print("Electricity bill calculation completed.")
