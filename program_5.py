Order = input(str("Enter hotdog: "))
Order_Price = 0.0
if Order == "hotdog":
    Order_Price = 3.50
    toppings = print(input(str("Enter topping: ")))

elif Order == "chilidog":
    Order_Price = 4.50
    toppings = print(input(str("Enter topping: ")))

    if toppings == "cheese":
        toppings_price = int(0.50)

    elif toppings == "peppers":
        toppings_price = int(0.75)

    elif toppings == "grilled onions":
        toppings_price = int(1.00)

    elif toppings == "none":
        toppings_price = int(0.0)


total_price = float(input((int(Order_Price) + int(toppings_price)) * 0.07))

print("Hotdog cost is: ", Order)
print("The taxt is: 7%")
print("Your total is: ", total_price)
