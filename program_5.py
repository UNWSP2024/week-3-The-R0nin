
Order = input(str("Enter hotdog: "))
#prices for the hotdogs variables \/
Hotdog = int(3.50)

Chilidog = int(4.50)
#I am trying to trun the answer into a variable \/
if Order == "hotdog" or "chilidog":
    "hotdog" == Hotdog
    "chilidog" ==  Chilidog
    toppings = print(input(str("Enter topping: ")))
#prices for the toppings variables\/
Cheese = int(0.50)

Peppers = int(0.75)

Grilled_Onions = int(1.00)

none = int(0.0)
#I am trying to trun the answer into a variable \/
if toppings == 'cheese' or 'peppers' or 'grilled onions':
    'cheese' == Cheese
    'peppers' == Peppers
    'grilled onions' == Grilled_Onions

total_price = float(input((int(Order) + int(toppings)) * 0.07))

print("Hotdog cost is: ", Order)
print("The taxt is: 7%")
print("Your total is: ", total_price)
