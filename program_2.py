age = float(input("Enter the person's age: "))
def categorize_age(age):
    ageCategory = "TBD"
    
    if age <= 1:
        print("infant")
    elif age < 13:
        print("child")
    elif age < 20:
        print("teenager")
    elif age >= 20:
        print("adult")

categorize_age(age)  
