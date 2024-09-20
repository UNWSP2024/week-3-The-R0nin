hotdogs = input(str("Enter hotdog: "))
Hotdog = 3.50
Chilidog = 4.50
if hotdogs == "hotdog" or "chilidog":
    "hotdog" = Hotdog
    "chilidog" ==  Chilidog
    toppings = print(input(str("Enter topping: ")))

Cheese = 0.50
Peppers = 0.75
Grilled_Onions = 1.00
none = 0.00
if toppings == 'cheese' or 'peppers' or 'grilled onions':
    'cheese' == Cheese
    'peppers' == Peppers
    'grilled onions' == Grilled_Onions

total_price = float(input((hotdogs + toppings) * 0.07))

print("Hotdog cost is: ", hotdogs)
print("The taxt is: 7%")
print("Your total is: ", total_price)
