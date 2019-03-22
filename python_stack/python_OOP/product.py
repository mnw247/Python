class product:
    def __init__(self, price, itemname, weight, brand):
        self.price = price
        self.itemname = itemname
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    
    def sell(self):
        self.status = "sold"
        return self
    
    def add_tax(self, tax):
        self.price = self.price * tax
        return self

    def returnitem(self, reason_for_return):
        if (reason_for_return == "defective"):
            self.status = "defective"
            self.price = 0
        if (reason_for_return == "like new"):
            self.status = "for sale"
        if (reason_for_return == "opened"):
            self.status = "used"
            self.price *= .8
        return self
        
    def displayAll(self):
        print("Price: $" + str(self.price))
        print("Weight: " + str(self.weight))
        print("Brand: " + str(self.brand))
        print("Status: " + str(self.status))

p1 = product(5, "apple", "1lb", "a")
p2 = product(2, "orange", "2 lb", "b")
p3 = product(1, "grapes", "1 lb", "c")
p4 = product(2, "lettuce", "3 lb", "d")
p5 = product(3, "brocolli", "2 lb", "e")
p6 = product(8, "soup", "1 lb", "a")

p1.sell().add_tax(.15).returnitem("opened").displayAll()
