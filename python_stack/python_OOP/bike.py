class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print (self.price, self.max_speed, self.miles)
        return self #only return self unnecessary since it is the last function that is run on all 3, but will crash if you have a function after because it would not have passed it back again.

    def ride(self):
        print ('Riding')
        self.miles += 10
        return self

    def reverse(self):
        print ('Reversing')
        if(self.miles>5):
            self.miles -= 5
        if(self.miles<=5 and self.miles>=0):
            self.miles = 0
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(300, "35mph")
bike3 = Bike(100, "15mph")

bike1.ride().ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()