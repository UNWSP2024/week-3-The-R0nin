
Order = input(str("Enter hotdog: "))
Order_Price = 0.0
if Order == "hotdog":
    Order_Price = 3.50
    toppings = print(input(str("Enter topping: ")))

elif Order == "chilidog":
    Order_Price = 4.50

toppings = print(input(str("Enter topping: ")))
toppings_price = 0.0
if toppings == "cheese":
    toppings_price = int(0.50)

elif toppings == "peppers":
    toppings_price = int(0.75)

elif toppings == "grilled onions":
    toppings_price = int(1.00)

elif toppings == "none":
    toppings_price = int(0.0)


total_tax = float(input((int(Order_Price) + int(toppings_price)) * 0.07))
total_price = float(input(int(Order_Price) + int(toppings_price) + int(total_tax)))

print("Hotdog cost is: ", Order_Price)
print("The taxt is: ", total_tax)
print("Your total is: ", total_price)
