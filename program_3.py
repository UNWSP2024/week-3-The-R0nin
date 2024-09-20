weight = float(input('Enter the weight of the package: '))
def weight_conversion(weight):
    # Calculate the shipping charge.
    
    if weight <= 2:
         shippingCost = 1.50
    elif weight > 2 and weight < 6:
         shippingCost = 3.00
    elif weight >= 6 and weight < 10:
         shippingCost = 4.00
    elif weight >= 10:
         shippingCost = 4.75
    else:
         shippingCost = 0.0

    
         return shippingCost
shippingCost = weight_conversion(float(weight))
print ('Shipping charge: $', shippingCost)
