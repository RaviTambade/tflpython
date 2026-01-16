import pandas as pd

# Sample product dataset
data = {
    "name": ["Laptop", "Headphones", "Keyboard", "Mouse", "Monitor"],
    "price": [60000, 1500, 700, 400, 12000],
    "rating": [4.5, 4.0, 3.8, 4.2, 4.7],
    "category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"]
}

df = pd.DataFrame(data)
print(df)