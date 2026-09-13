Welcome to one more good session. Let’s turn this into a Transflower classroom learning session—not just explaining Singleton syntax, but helping learners understand why the pattern exists, what problem it solves, and when not to use it.

👨‍🏫 Transflower Mentor Classroom Session

Singleton Pattern — The Bank Manager and the One Vault

🌱 Welcome to One More Good Learning Session

Imagine I take you into a large bank.

There are:

- 🏦 20 branches
- 👨‍💼 500 employees
- 👥 100,000 customers
- 💰 Thousands of transactions every day

I ask a student:

«Ravi Sir: “How many vaults should contain the bank's central reserve?”»

The student thinks for a moment.

«Student: “Sir, one?”»

Exactly!

Why?

Because if every branch creates its own independent central vault, we have a serious problem.

                         BANK
                           │
             ┌─────────────┼─────────────┐
             │             │             │
          Branch A       Branch B      Branch C
             │             │             │
           Vault A       Vault B       Vault C
             │             │             │
          ₹10 Lakh      ₹20 Lakh      ₹15 Lakh

Now I ask:

«“Which vault contains the real central balance?”»

There is no single source of truth.

Instead, the bank wants:

                         BANK
                           │
             ┌─────────────┼─────────────┐
             │             │             │
          Branch A       Branch B      Branch C
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                    ┌─────────────┐
                    │  ONE VAULT  │
                    │  ₹45 Lakh   │
                    └─────────────┘

This is the basic idea behind the Singleton Design Pattern.

«Singleton means: one shared instance of a class.»

---

🧠 First Principle: What Is an Object?

Before understanding Singleton, understand something more fundamental:

«What happens when we create an object?»

Consider:

class BankVault:
    pass

vault1 = BankVault()
vault2 = BankVault()

Python normally creates two objects:

vault1 ───────► Object #1

vault2 ───────► Object #2

They are different objects.

print(vault1 == vault2)

Normally:

False

With Singleton, we want:

vault1 ───────┐
              │
              ▼
         ONE OBJECT
              ▲
              │
vault2 ───────┘

Therefore:

vault1 = BankVault()
vault2 = BankVault()

print(vault1 is vault2)

should produce:

True

---

👨‍🏫 Mentor–Student Conversation

I ask the classroom:

«Ravi Sir: “What does "BankVault()" normally do?”»

Student:

«“Sir, it creates an object.”»

Correct.

Then I ask:

«Ravi Sir: “What if I call it 100 times?”»

Student:

«“It creates 100 objects.”»

Exactly.

So our problem is:

BankVault()
BankVault()
BankVault()
BankVault()
    ...
BankVault()

       ↓

Many objects

Singleton changes the design:

BankVault()
BankVault()
BankVault()
BankVault()

       ↓

ONE shared object

---

🐍 Understanding "__new__()"

This is where Python becomes interesting.

A beginner usually learns:

__init__()

and thinks:

«""__init__()" creates the object."»

Not exactly.

Python separates object creation from object initialization.

Conceptually:

BankVault()
     │
     ▼
  __new__()
     │
     ▼
Object created
     │
     ▼
  __init__()
     │
     ▼
Object initialized

Therefore, if we want to control whether a new object should be created, "__new__()" is the important place.

---

🏦 Building Our Bank Vault

Let's build the Singleton step by step.

class BankVault:

    __instance = None

    def __new__(cls, *args, **kwargs):

        if cls.__instance is None:
            print("Creating the vault...")
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self):
        self.balance = 1000000

Now:

vault1 = BankVault()
vault2 = BankVault()

What happens?

---

1️⃣ First Call

vault1 = BankVault()

Python reaches:

__new__()

Initially:

__instance

is:

None

So Python creates the object:

        __instance
             │
             ▼
      ┌──────────────┐
      │  BankVault   │
      │              │
      │ ₹10,00,000   │
      └──────────────┘

The reference is stored in "__instance".

---

2️⃣ Second Call

Now:

vault2 = BankVault()

Python reaches "__new__()" again.

But this time:

cls.__instance

already exists.

Therefore:

if cls.__instance is None:

is "False".

Python simply returns the existing object.

So:

vault1 ───────┐
              │
              ▼
       ┌──────────────┐
       │  BankVault   │
       │  ₹10,00,000  │
       └──────────────┘
              ▲
              │
vault2 ───────┘

There are two references, but only one object.

---

🔍 "==" vs "is"

This is an excellent opportunity to teach an important Python concept.

print(vault1 == vault2)

checks equality.

But:

print(vault1 is vault2)

checks whether both variables refer to the exact same object.

For Singleton, "is" is the more meaningful test.

print(vault1 is vault2)

Output:

True

Remember

==  → Are the values equal?

is  → Are they the same object?

---

💰 Shared State

Now let's perform a banking transaction.

vault1.balance = 1000000

vault2.balance += 50000

print(vault1.balance)

Output:

1050000

Why?

Because there aren't two vaults.

There is only one:

vault1 ──────┐
             │
             ▼
       ┌─────────────┐
       │  ONE VAULT  │
       │ ₹10,50,000  │
       └─────────────┘
             ▲
             │
vault2 ──────┘

Changing the object through "vault2" changes the same object observed through "vault1".

This is the real power—and also the danger—of shared state.

---

⚠️ A Small but Important Python Problem

Now, as a mentor, I would not stop here.

Look carefully at:

def __init__(self):
    self.balance = 1000000

There is an interesting issue.

"__init__()" can run every time we call:

BankVault()

even though "__new__()" returns the same object.

For example:

vault1 = BankVault()

vault1.balance += 50000

vault2 = BankVault()

print(vault2.balance)

The result may be:

1000000

Why?

Because the second call can initialize the same object again:

First call
    ↓
balance = ₹10,00,000
    ↓
+ ₹50,000
    ↓
balance = ₹10,50,000

Second BankVault()
    ↓
__init__()
    ↓
balance = ₹10,00,000

This teaches us an important lesson:

«Singleton is not merely about returning the same object. Initialization also needs to be designed carefully.»

---

✅ Safer Implementation

One simple approach is to initialize the state only when the Singleton object is first created.

class BankVault:

    __instance = None

    def __new__(cls):

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.balance = 1000000

        return cls.__instance

Now initialization happens when the Singleton object is first created.

---

🎯 Singleton Pattern in One Diagram

                    APPLICATION
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       Module A       Module B       Module C
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                ┌────────────────┐
                │   SINGLETON    │
                │     OBJECT     │
                └────────────────┘
                         │
                    Shared State

The important idea is:

«Many references, one object.»

Not:

«Many objects with the same data.»

---

📝 Hands-On Exercise 1 — Logger

Now forget the bank.

Imagine your application has:

Login
Payment
Order
Database
API

Every module wants to write logs.

You don't want:

LoginLogger
PaymentLogger
OrderLogger
DatabaseLogger
APILogger

Instead:

                    APPLICATION
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
           Login       Payment      Order
             │           │           │
             └───────────┼───────────┘
                         ▼
                    ONE LOGGER

Task

Create:

class Logger:
    pass

Make it Singleton.

Then test:

logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)

Expected:

True

Then add:

logger1.logs.append("Application started")

and verify:

print(logger2.logs)

Expected:

["Application started"]

💡 Think Like a Developer

Don't immediately search for a Singleton implementation.

First ask:

«“Why should there be only one Logger?”»

That question is more important than the syntax.

---

🧑‍💻 Hands-On Exercise 2 — Configuration Manager

Imagine an application has configuration such as:

- Database connection
- API URL
- Application name
- Environment

Create:

class Configuration:
    pass

The application should have only one configuration object.

Try:

config1 = Configuration()
config2 = Configuration()

print(config1 is config2)

Expected:

True

Then:

config1.environment = "Production"

print(config2.environment)

Expected:

Production

Again, ask yourself:

«Why does the application need one shared configuration object?»

---

🤔 “But Ravi Sir, Should Everything Be Singleton?”

No!

This is one of the most important lessons.

Suppose we have:

class Customer:
    pass

We need:

Customer 1
Customer 2
Customer 3
Customer 4
...

Should "Customer" be Singleton?

Obviously not.

We need independent objects:

customer1 ───► Customer Object 1

customer2 ───► Customer Object 2

customer3 ───► Customer Object 3

If we accidentally make "Customer" a Singleton:

customer1 ──┐
customer2 ──┼──► SAME CUSTOMER
customer3 ──┘

Now changing one customer's name could affect everybody.

Disaster!

---

🌱 Mentor Wisdom

Remember this simple rule:

«Singleton is not about making an object special. It is about controlling object lifetime and ensuring one shared instance where one instance is actually required.»

Possible candidates include:

- Application-wide configuration
- Certain logging infrastructure
- Shared cache managers
- Resource managers
- Some infrastructure services

But don't blindly make everything Singleton.

---

🚨 Singleton Has a Cost

I would ask my students:

«Student: “Sir, if Singleton is so useful, why don't we make every class Singleton?”»

Because global shared state can create problems.

For example:

             Module A
                 │
                 ▼
             Singleton
                 ▲
                 │
             Module B

Module A changes something.

Module B unexpectedly sees the changed state.

This can make:

- 🧪 Testing harder
- 🔗 Dependencies less obvious
- 🧩 Code more tightly coupled
- ⚡ Concurrency more complicated
- 🐛 Debugging harder

So remember:

«Use Singleton because the business/design requirement demands one shared instance—not simply because you know how to implement it.»

---

🧠 Final Classroom Summary

I would end the class with this on the whiteboard:

                  Singleton Pattern
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
    One Instance    Shared Access    Controlled
                                    Object Creation
          │
          ▼
      Shared State
          │
          ▼
      Use Carefully

And one final question:

«“What is the real purpose of Singleton?”»

The answer is not:

«""__new__()" is used."»

The better answer is:

«“When the system logically requires exactly one shared instance of a resource, Singleton provides controlled creation and shared access to that instance.”»

---

🌸 Transflower Mentor Mantra

Don't memorize the Singleton code.

First ask:

«“Do I really need only one object?”»

Then ask:

«“Who should own it?”»

Then ask:

«“Who should be allowed to access it?”»

Only after answering those design questions should you write:

class Something:
    ...

The learning journey should always be:

Problem
   ↓
Requirement
   ↓
Design
   ↓
Pattern
   ↓
Implementation
   ↓
Testing
   ↓
Refactoring

«First understand the problem → then understand the design → then write the code.»

That is the developer mindset.

🌸 Tap your potential. Enjoy learning experiences.If you want, I can also convert this into a **Transflower-style “Singleton Pattern in Python — classroom notes + 5 progressive hands-on exercises + interview questions”** format.
