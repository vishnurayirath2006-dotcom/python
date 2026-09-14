# Create
numbers = [int(x) for x in input("Enter numbers: ").split()]

# Search
n = int(input("Search number: "))
print("Found" if n in numbers else "Not Found")

# Update (add)
numbers.append(int(input("Add number: ")))

# Filter (even numbers)
even = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even)

# Manipulate (sort)
numbers.sort()

# Remove
numbers.remove(int(input("Remove number: ")))

print("Final list:", numbers)