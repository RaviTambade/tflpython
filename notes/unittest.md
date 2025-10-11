

👨‍🏫 **Scene: The Software Factory**

Imagine a **software factory** 🏭 building a huge e-commerce platform:

* There are **modules for products, orders, payments, and user accounts**.
* Every module has **multiple functions**, and they interact with each other.
* One small bug in the **checkout process** can ruin a customer’s experience.

Now, imagine you are the **quality engineer**. Your manager says:

> “We need to **test everything automatically**, repeatedly, and reliably. Manual testing will take too long!”

Here comes **PyTest** — your **smart robot assistant** 🤖.

---

### 🐍 Python Essentials — PyTest

**PyTest** is a **powerful Python testing framework** that allows you to:

1. Write **simple tests quickly**.
2. Organize **complex test suites**.
3. Reuse **fixtures** for setup and teardown.
4. Scale testing as your application grows.

---

### 🔹 Simple Example: Testing a Function

Suppose we have a function that calculates **discounted price**:

```python
# discount.py
def apply_discount(price, discount_percent):
    return price - (price * discount_percent / 100)
```

Now we want to **test it**:

```python
# test_discount.py
from discount import apply_discount

def test_apply_discount():
    assert apply_discount(1000, 10) == 900
    assert apply_discount(500, 20) == 400
    assert apply_discount(0, 50) == 0
```

✅ Run the test in terminal:

```bash
pytest test_discount.py
```

PyTest will **automatically detect functions starting with `test_`** and run them.

---

### 🔹 Advanced PyTest: Using Fixtures

In a large system, some **setup is common** (e.g., database connection, test data). PyTest **fixtures** help reuse setup code:

```python
# test_orders.py
import pytest

@pytest.fixture
def sample_order():
    return {"product": "Laptop", "price": 60000, "quantity": 2}

def test_order_total(sample_order):
    total = sample_order["price"] * sample_order["quantity"]
    assert total == 120000
```

✨ **Mentor Wisdom:**

* Fixtures = **mini-labs** to prepare your test environment.
* Avoid repeating the same setup code in every test.

---

### 🔹 Parametrized Tests

Sometimes you want to **run the same test with multiple inputs**:

```python
import pytest
from discount import apply_discount

@pytest.mark.parametrize("price,discount,expected", [
    (1000, 10, 900),
    (500, 20, 400),
    (2000, 50, 1000)
])
def test_apply_discount(price, discount, expected):
    assert apply_discount(price, discount) == expected
```

✅ This makes your **tests scalable and maintainable**.

---

### 🔹 Mentor Analogy:

* **Small functions** → Single machines in the factory
* **Complex workflows** → Entire assembly lines
* **PyTest** → Your **robot supervisor** that checks every machine and assembly line automatically, repeatedly, and reliably.

Without PyTest:

* Manual checks = slow, error-prone, inconsistent

With PyTest:

* Automated checks = fast, consistent, repeatable
* Works even as your codebase **grows to thousands of functions**

---

### 🔹 Real-World Applications of PyTest

* E-commerce: test checkout, payment, cart calculations
* Banking: test transactions, interest calculations
* SaaS: test user authentication, API endpoints, data integrity
* Data pipelines: test ETL jobs, transformations, and aggregation logic



If you want, I can **design a mini hands-on PyTest exercise** for your students where they:

1. Test **multiple e-commerce functions** (discount, tax, shipping).
2. Use **fixtures** for common test data.
3. Use **parametrized tests** to handle multiple scenarios.

This way, they **experience building a scalable, professional test suite**.

Do you want me to create that exercise?
