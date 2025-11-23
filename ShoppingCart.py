# Step 1: Empty cart
cart = []

while True:
    product = input("Enter product name (q to quit): ")

    # Quit condition
    if product.lower() == "q":
        break

    price = float(input("Enter price: "))

    # Step 2: Check if product already exists
    found = False

    for item in cart:
        if item[0].lower() == product.lower():
            item[2] = item[2] + 1  # increase quantity
            found = True
            break

    # Step 3: If not found, add as a new item
    if not found:
        cart.append([product, price, 1]) # [apple,10,1]

# Step 4: Print cart
print("\nCart:")
total = 0

for item in cart:
    name = item[0]
    price = item[1]
    quantity = item[2]

    print(name, quantity,"x",price,"=", quantity * price)

    total += quantity * price

print("Total:", total)
