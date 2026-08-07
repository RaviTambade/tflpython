# 🧪 **PyTest – Building Confidence Before Building Software**

## *"Great Software Engineers Don't Just Write Code... They Prove It Works."*


> *The classroom is buzzing with excitement. Yesterday, students built their first Python projects. Today, they are eager to learn something new. The mentor walks into the classroom carrying two mobile phones.*

One phone looks brand new. The other has a cracked screen. The mentor places both on the table.


## 👨‍🏫 **Mentor:**

Imagine both companies launch their phones today. Company A spent **two years testing** every feature. Company B said,

> "Testing is wasting time. Let's release it!"

Which phone would you buy? The students immediately answered,

> "The tested one!"
 
The mentor smiled. Exactly. Then why do many programmers spend hours writing code...

...but only a few minutes testing it?


# 📖 A Story from the Software Factory

Imagine you have joined **Transflower Technologies** as a Python Developer. Your team is building **TFLStore**, an online shopping platform. Thousands of customers visit every day.

```text
                 TFLStore

      +--------------------------+
      |      Product Catalog     |
      +--------------------------+
                  |
      +--------------------------+
      |      Shopping Cart       |
      +--------------------------+
                  |
      +--------------------------+
      |       Checkout           |
      +--------------------------+
                  |
      +--------------------------+
      |       Payment            |
      +--------------------------+
                  |
      +--------------------------+
      |     Order Management     |
      +--------------------------+
```

Every module is connected. If one small calculation fails... The customer cannot purchase. The company loses money. Customer trust disappears.


# One Small Bug...

Suppose a customer buys

```text
Laptop
Price : ₹80,000
Discount : 10%
```

Expected price

```text
₹72,000
```

But due to a programming mistake, the website displays

```text
₹7,200
```

Imagine... One thousand customers purchase before anyone notices. How much money has the company lost? Sometimes,

a **single bug costs millions**.

That is why software testing is not optional. It is a professional responsibility.

# Why Testing Matters

Imagine building a bridge. Would engineers allow people to cross it without testing? No. Imagine manufacturing an aircraft. Would pilots fly it without testing? Never. Software is no different. Every professional application is tested before it reaches users.


# Meet PyTest

The mentor writes on the board

```text
PyTest
```
and asks,

> "Who checks whether our code is correct?"

Students answer, "We do." The mentor replies,

> "Only until your project grows."

Imagine your application contains

```text
50 Functions
↓
500 Functions
↓
5,000 Functions
↓
50,000 Functions
```

Can one programmer test everything manually? Impossible. So we hire another engineer. Not a human. A robot. That robot is called

# **PyTest**


# What is PyTest?

PyTest is one of the most popular testing frameworks in Python. Think of it as a

```text
Robot Quality Engineer
```

It checks your software

- ✔ automatically
- ✔ repeatedly
- ✔ consistently
- ✔ quickly

Whenever your code changes, PyTest verifies that everything still works.


# The Software Factory

Imagine a modern software company.

```text
            Software Factory

             Requirements
                    │
                    ▼
               Python Code
                    │
                    ▼
            +----------------+
            |    PyTest 🤖    |
            +----------------+
                    │
        ┌───────────┴───────────┐
        │                       │
     PASS ✅                 FAIL ❌
```

Every time developers write code, PyTest inspects it before customers use it.

# Installing PyTest

Open your terminal.

```bash
pip install pytest
```

Verify installation.

```bash
pytest --version
```

If you see the version, your testing robot is ready.


# First Example

Suppose we build a simple function.

### discount.py

```python
def apply_discount(price, discount_percent):
    return price - (price * discount_percent / 100)
```

Looks correct. But how do we know? We test it.

### test_discount.py

```python
from discount import apply_discount

def test_apply_discount():

    assert apply_discount(1000,10)==900

    assert apply_discount(500,20)==400

    assert apply_discount(0,50)==0
```

Notice something interesting.

There is no

```python
print()
```

Instead,

we use

```python
assert
```

# What is assert?

Think of assert as asking a question.

```text
Expected
↓
900

Actual
↓
900

Match?
↓
YES
PASS
```

If they don't match, PyTest reports a failure.

# Running Tests

Simply type

```bash
pytest
```

PyTest automatically searches for

```text
test_*.py
```

and executes every function beginning with

```text
test_
```

No manual work required.

# Understanding the Output

If everything succeeds

```text
=============================
3 PASSED
=============================
```

If something fails

```text
=============================
2 PASSED
1 FAILED
=============================
```

It even shows

* expected value
* actual value
* line number
* error details

making debugging much easier.

# PyTest Fixtures

Now imagine our e-commerce project. Every test needs

* sample customer
* sample product
* sample order

Without fixtures, every test repeats the same setup.

```python
customer={...}
product={...}
order={...}
```

again and again and again. Professional developers avoid repetition.


# Fixtures

Think of a fixture as preparing a laboratory before experiments begin.

```text
Laboratory
↓
Arrange Equipment
↓
Students Perform Experiment
↓
Clean Laboratory
```

PyTest works exactly like this.


Example

```python
import pytest

@pytest.fixture
def sample_order():

    return {
        "product":"Laptop",
        "price":60000,
        "quantity":2
    }

def test_order_total(sample_order):
    total=sample_order["price"]*sample_order["quantity"]
    assert total==120000
```

One setup. Many tests.


# Mentor Wisdom

Fixtures help us

* avoid duplicate code
* prepare common data
* improve readability
* simplify maintenance

Professional projects contain hundreds of fixtures.

# Parameterized Tests

Suppose marketing changes discounts every week. Should we write

```python
def test1():
def test2():
def test3():
def test4():
```

No. PyTest allows one test with many inputs.

```python
import pytest

from discount import apply_discount
@pytest.mark.parametrize(
"price,discount,expected",
[
(1000,10,900),
(500,20,400),
(2000,50,1000),
(8000,25,6000)
]
)

def test_apply_discount(price,discount,expected):
    assert apply_discount(price,discount)==expected
```

One test.Multiple scenarios. Elegant. Professional. Scalable.

# Testing TFLStore

Imagine the modules inside **TFLStore**.

```text
               TFLStore

     Product Module
           │
           ▼
     Shopping Cart
           │
           ▼
      Discount Engine
           │
           ▼
      Payment Module
           │
           ▼
      Order Module
```

Every module has its own tests.

```text
test_products.py
test_cart.py
test_discount.py
test_payment.py
test_orders.py
```

When developers modify one module, PyTest automatically verifies that the rest of the application still works. This gives teams confidence to improve software without breaking existing features.

# Industry Applications

PyTest is used across industries.

| Domain                | What Gets Tested?                                         |
| --------------------- | --------------------------------------------------------- |
| 🛒 E-Commerce         | Cart, discounts, checkout, payment, inventory             |
| 🏦 Banking            | Interest calculations, fund transfers, account validation |
| 🏥 Healthcare         | Patient registration, billing, prescriptions              |
| ✈️ Travel             | Ticket booking, seat allocation, fare calculations        |
| 🎓 Learning Platforms | Login, assessments, grading, certificates                 |
| 🤖 AI Applications    | Data preprocessing, prediction APIs, model integration    |


# Mini Hands-On Exercise

## Project: Test the TFLStore Pricing Engine
### Step 1 – Create `pricing.py`

```python
def calculate_discount(price, discount):
    return price - (price * discount / 100)

def calculate_tax(price, tax):
    return price + (price * tax / 100)

def shipping_charge(amount):
    if amount >= 5000:
        return 0
    return 250
```

### Step 2 – Create `test_pricing.py`

```python
import pytest
from pricing import calculate_discount, calculate_tax, shipping_charge

@pytest.fixture
def sample_price():
    return 1000

@pytest.mark.parametrize(
    "discount,expected",
    [
        (10, 900),
        (20, 800),
        (50, 500)
    ]
)
def test_discount(sample_price, discount, expected):
    assert calculate_discount(sample_price, discount) == expected

def test_tax():
    assert calculate_tax(1000, 18) == 1180

def test_free_shipping():
    assert shipping_charge(6000) == 0

def test_paid_shipping():
    assert shipping_charge(2000) == 250
```

### Step 3 – Run the Tests

```bash
pytest -v
```

Observe the output and identify which tests pass or fail. If a test fails, inspect the function, fix the logic, and run the suite again. This rapid feedback loop is how professional teams maintain quality.

# Best Practices
* Write tests as soon as you write the corresponding function.
* Keep each test focused on one behavior.
* Use descriptive test names such as `test_free_shipping_for_large_orders()`.
* Reuse fixtures for common setup.
* Use parameterized tests to cover multiple scenarios efficiently.
* Run your test suite before every commit or deployment.

# Mentor's Challenge

Build a complete **PyTest Test Suite for TFLStore**. Create tests for:

* Product Price Calculation
* Shopping Cart
* Discount Engine
* GST Calculation
* Shipping Charges
* Coupon Validation
* Order Placement
* Payment Gateway
* Customer Login

**Advanced Challenge**

* Use fixtures to create sample customers, products, and orders.
* Use parameterized tests for discounts and tax calculations.
* Generate an HTML test report using the `pytest-html` plugin.
* Integrate the test suite into a GitHub Actions workflow so tests run automatically on every push.


# Key Takeaways

* **PyTest** is a powerful and widely used Python testing framework.
* Tests verify that your code behaves as expected and help prevent regressions.
* `assert` compares expected and actual results.
* **Fixtures** prepare reusable test data and setup.
* **Parameterized tests** let you validate multiple inputs with minimal code.
* Automated testing improves confidence, speeds up development, and supports continuous integration.

# 🌟 Mentor's Closing Words

> **"Anyone can write code that works today. A professional software engineer writes code that still works tomorrow, after hundreds of changes."**

> **"Testing is not about finding mistakes after they happen. It is about preventing mistakes before your customer experiences them."**

> **"At Transflower, we don't celebrate code that merely compiles—we celebrate software that is reliable, maintainable, and trusted. PyTest is not just a testing tool; it is your quality partner on the journey from a classroom assignment to enterprise-grade software."**
