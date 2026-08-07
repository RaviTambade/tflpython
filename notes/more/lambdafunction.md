 

## 👨‍🏫 Lambda Function 

Normally, in Python, when you want to perform a task, you write a function with `def`. It’s like building a **full machine** — big, structured, and permanent.

But sometimes, you just want a **quick calculation**, like “square this number” or “add 10 to a value.” You don’t want to build a full machine, just a **small tool**.

That’s where a **lambda function** comes in.
 

### 📌 Definition

A **lambda function** in Python is a **small, anonymous function** (no name).

* It can have **any number of arguments**.
* But it can only have **one expression**.
* It **automatically returns** the result of that expression.

 

### 🐍 Syntax

```python
lambda arguments: expression
```

 

### 💡 Simple Example

Normal function:

```python
def square(x):
    return x * x

print(square(5))  # 25
```

Lambda version:

```python
square = lambda x: x * x
print(square(5))  # 25
```

Both do the same thing! ✅
But the lambda is just a **one-liner shortcut**.

 

### 🔧 Where do we use it?

Lambdas are **very common** in quick operations, especially with functions like:

* `map()` → Apply something to every item in a list
* `filter()` → Pick items from a list
* `sorted()` → Custom sort rules

Example:

```python
numbers = [1, 2, 3, 4, 5]

# Double every number
doubled = list(map(lambda n: n * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]
```
✨ **Mentor’s Note:**

* Use **lambda** for short, temporary logic.
* Use **def** when the logic is bigger or reused multiple times.


👨‍🏫 **Scene: E-Commerce Discount System**

Imagine you’re coding for **Amazon’s sale day** 🎉.
Your manager says:

* “Apply **10% discount** on all products today.”
* “Filter out only products that cost more than ₹500.”
* “Sort products by customer ratings.”

You could write big, heavy `def` functions for each,
but that’s like bringing a **truck to carry one shopping bag** 🛒.
Instead, use **lambda — a quick, light helper**.

 

### 🛒 Example: Products List

```python
products = [
    {"name": "Laptop", "price": 60000, "rating": 4.5},
    {"name": "Headphones", "price": 1500, "rating": 4.0},
    {"name": "Keyboard", "price": 700, "rating": 3.8},
    {"name": "Mouse", "price": 400, "rating": 4.2},
    {"name": "Monitor", "price": 12000, "rating": 4.7}
]
```
 

### ✅ 1. Apply **10% discount** (using `map`)

```python
discounted = list(map(lambda p: {**p, "price": p["price"] * 0.9}, products))
print(discounted)
```

🎯 Every product now has a new price after discount.
 

### ✅ 2. Filter **premium products** (using `filter`)

```python
premium = list(filter(lambda p: p["price"] > 5000, products))
print(premium)
```

🎯 Only Laptop & Monitor stay in the list.
 

### ✅ 3. Sort by **ratings** (using `sorted`)

```python
sorted_by_rating = sorted(products, key=lambda p: p["rating"], reverse=True)
print(sorted_by_rating)
```

🎯 Products appear with **best rating first**.

 
⚡ **Mentor’s Wisdom:**

* `def` = **big machine** (permanent, reusable)
* `lambda` = **pocket calculator** (quick, temporary, one-shot task)

That’s why in **real commercial apps** like e-commerce, finance, or even AI data filtering, lambdas make your code **short, powerful, and readable**.

👨‍🏫 **Scene: Amazon Product Dataset**

Imagine you’re a **data analyst at Amazon**.
You’ve got a **CSV file** of thousands of products with details like *name, price, rating, category*.

Your boss asks:

* “Show me only the products above ₹10,000.”
* “Find average rating per category.”
* “Create a special column with discount prices.”

This is where **lambda + Pandas** shine 🌟.
 

### 🐼 Example: Using Pandas with Lambda

```python
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
```
 

### ✅ 1. Filter premium products (price > 10,000)

```python
premium = df[df["price"].apply(lambda p: p > 10000)]
print(premium)
```

🎯 Shows only Laptop & Monitor.

---

### ✅ 2. Add a **discounted price column**

```python
df["discounted_price"] = df["price"].apply(lambda p: p * 0.9)
print(df)
```

🎯 Every product now has a new price after discount.
 

### ✅ 3. Sort by rating

```python
sorted_df = df.sort_values(by="rating", key=lambda col: col)
print(sorted_df)
```

🎯 Products ordered by rating.
 

### ✅ 4. Group by category & find average rating

```python
avg_rating = df.groupby("category")["rating"].apply(lambda x: x.mean())
print(avg_rating)
```

🎯 Quickly calculates **average rating for each category**.
 

✨ **Mentor’s Wisdom:**

* In **small scripts**, lambdas save you lines of code.
* In **big datasets (Pandas)**, lambdas let you write **custom, one-line operations** without full functions.
* In **real companies**, this means **faster data filtering, cleaning, and transformation**.
 

## 📝 Mini Hands-On Exercise: E-Commerce Product Analysis

### **Scenario (Storytelling Style)**

You are a **data analyst at a small e-commerce company**. The company has a **CSV file of products** with columns like:

* `ProductID` → Unique identifier
* `Name` → Product name
* `Category` → Electronics, Accessories, Clothing, etc.
* `Price` → Price of the product in ₹
* `Rating` → Customer rating (1–5)
* `Stock` → Quantity available

Your task is to **analyze the data** to support the marketing and sales teams. You will practice **filtering, mapping, sorting, and grouping using lambda functions**.
 

### **Step 0: Sample CSV (`products.csv`)**

```csv
ProductID,Name,Category,Price,Rating,Stock
101,Laptop,Electronics,60000,4.5,25
102,Headphones,Electronics,1500,4.0,50
103,Keyboard,Accessories,700,3.8,100
104,Mouse,Accessories,400,4.2,200
105,Monitor,Electronics,12000,4.7,30
106,T-Shirt,Clothing,800,4.1,150
107,Jeans,Clothing,1500,4.3,80
108,Smartphone,Electronics,35000,4.6,40
```

 

### **Step 1: Load CSV into Pandas**

```python
import pandas as pd

df = pd.read_csv("products.csv")
print(df.head())
```

### **Step 2: Filter Products**

**Task:** Show products with **Price > 10,000**

```python
premium_products = df[df["Price"].apply(lambda p: p > 10000)]
print(premium_products)
```

### **Step 3: Map / Transform Data**

**Task:** Apply a **10% festive discount** on all products and create a new column `DiscountedPrice`.

```python
df["DiscountedPrice"] = df["Price"].apply(lambda p: p * 0.9)
print(df)
```

### **Step 4: Sort Products**

**Task:** Sort products by **Rating in descending order**.

```python
sorted_products = df.sort_values(by="Rating", key=lambda col: col, ascending=False)
print(sorted_products)
```

### **Step 5: Group & Aggregate**

**Task:** Find **average price per Category**.

```python
avg_price = df.groupby("Category")["Price"].apply(lambda x: x.mean())
print(avg_price)
```

**Task:** Find **average rating per Category**.

```python
avg_rating = df.groupby("Category")["Rating"].apply(lambda x: x.mean())
print(avg_rating)
```

### **Step 6: Bonus Challenge (Optional)**

* Filter products **in stock < 50** and **price > 10,000**.
* Sort by **DiscountedPrice** in ascending order.
* Identify **top 3 products by rating in each category**.

### **Learning Outcomes**

After completing this exercise, students will be able to:

1. Load and explore a **real-world dataset**.
2. Use **lambda functions** to **filter, transform, sort, and aggregate data**.
3. Experience a **mini industry workflow**: filtering premium products, applying discounts, and analyzing product ratings.
4. Understand how **small anonymous functions** can simplify data processing tasks.


### Set Steps for products.csv

### **Step 0: Generate `products.csv`**

Here’s an example dataset content (50+ products). You can save this as `products.csv`:

```csv
ProductID,Name,Category,Price,Rating,Stock
101,Laptop,Electronics,60000,4.5,25
102,Headphones,Electronics,1500,4.0,50
103,Keyboard,Accessories,700,3.8,100
104,Mouse,Accessories,400,4.2,200
105,Monitor,Electronics,12000,4.7,30
106,T-Shirt,Clothing,800,4.1,150
107,Jeans,Clothing,1500,4.3,80
108,Smartphone,Electronics,35000,4.6,40
109,Sneakers,Footwear,2500,4.4,60
110,Socks,Clothing,200,4.0,300
111,Tablet,Electronics,25000,4.3,35
112,Charger,Accessories,500,4.1,150
113,Backpack,Accessories,1200,4.2,70
114,Smartwatch,Electronics,15000,4.5,45
115,Jacket,Clothing,2500,4.3,60
116,Cap,Clothing,500,3.9,120
117,Belt,Accessories,400,4.0,80
118,Desk,Home,8000,4.4,20
119,Chair,Home,5000,4.2,30
120,Table Lamp,Home,1500,4.1,50
121,Notebook,Stationery,50,4.5,500
122,Pen,Stationery,20,4.2,1000
123,Printer,Electronics,12000,4.3,15
124,Router,Electronics,3000,4.1,40
125,External HDD,Electronics,5000,4.2,25
126,Coffee Maker,Home,7000,4.4,18
127,Blender,Home,3500,4.1,25
128,Air Fryer,Home,9000,4.5,12
129,Vacuum Cleaner,Home,15000,4.6,10
130,Water Bottle,Accessories,300,4.0,200
131,Running Shoes,Footwear,3500,4.3,55
132,Sandals,Footwear,1200,4.0,80
133,Sports Watch,Accessories,3500,4.4,40
134,Hair Dryer,Home,2500,4.2,30
135,Earbuds,Electronics,2000,4.1,100
136,Camera,Electronics,45000,4.7,12
137,Tripod,Accessories,1500,4.2,45
138,Microphone,Electronics,8000,4.5,20
139,Speaker,Electronics,5000,4.3,35
140,Notebook Stand,Accessories,1200,4.1,50
141,Office Chair,Home,12000,4.5,15
142,Sofa,Home,45000,4.6,5
143,Dining Table,Home,35000,4.4,8
144,Bed,Home,40000,4.7,6
145,Pillow,Home,800,4.2,150
146,Curtains,Home,2500,4.1,40
147,Mattress,Home,20000,4.5,10
148,Scarf,Clothing,700,4.0,60
149,Gloves,Clothing,400,4.1,80
150,Sunglasses,Accessories,1500,4.3,50
```
### **Step 1: Save CSV**

1. Copy the content above into a file named `products.csv`.
2. Place it in the same folder as your Python script.


### **Step 2: Sample Student Tasks**

1. Filter products **Price > 10,000**
2. Apply **15% discount** using lambda → new column `DiscountedPrice`
3. Sort products by **Rating descending**
4. Group by `Category` → calculate **average price** and **average rating**
5. Bonus: Filter **Stock < 50** and **Price > 10,000**

This dataset is realistic enough for **50+ products**, covering multiple categories like **Electronics, Accessories, Clothing, Home, Footwear, Stationery**. Students can see **how lambda + Pandas** are used in **real industry workflows**.
