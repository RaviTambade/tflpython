
''''
def square(x):
    return x*x

# Division
# divider, divident, divisor, quotionent

def divide(number, divisor):
    qutotient=number/divisor
    return qutotient

number1=4
result1=square(number1)
print (" sqaure result=" , result1)


number2=75
number3=5

resultDivision=divide(number2,number3)
print("Division result= ", resultDivision)

'''


#oneliner shortcut
square=lambda x: x*x
print(square(5))


# real use of lambda

marks=[34,76,45,87,98]
marksdoubled=list(map(lambda n: n*2,marks))
print( marksdoubled)


# Ecommerce Solution
products=[
    {"name":"Laptop", "price":60000,"rating":4.5},
    {"name": "Headphones", "price": 1500, "rating": 4.0},
    {"name": "Keyboard", "price": 700, "rating": 3.8},
    {"name": "Mouse", "price": 400, "rating": 4.2},
    {"name": "Monitor", "price": 12000, "rating": 4.7}
]
# Apply Discount 10% for each product available


discounted=list(map( lambda p: { **p, "price": p["price"]* 0.9,"rating":p["rating"]* 2},products))
print ( discounted)



=>