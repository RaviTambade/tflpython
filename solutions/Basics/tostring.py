# In Java, we use toString() method. 
# In python this can be achieved by using __repr__ or __str__ methods.

# Class for Product
class Product:
    #Class variable
    title= "Gerbera"

    #The Init or constructor
    def __init__(self, title,description,unitPrice,quantity):
        # Instnace Variable
        self.title=title
        self.description=description
        self.unitPrice=unitPrice
        self.quantity=  quantity
     
    def __repr__(self):
        return "Product title:%s description:%s" % (self.title, self.description)

  
    def __str__(self): 
        return "From str method of Product: Title is %s, Description is %s" % (self.title, self.description) 
  

# Driver Code
flower=Product("Lily", "Smelling flower", 10,4000)
print(flower) # This calls __str__()
print([flower]) # This calls __repr__()