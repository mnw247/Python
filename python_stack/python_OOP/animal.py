class animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        print('walking')
        self.health -= 1
        return self

    def run(self):
        print('running')
        self.health -= 5
        return self

    def displayHealth(self):
        print(self.name,"Health: " + str(self.health))

class dog(animal):
    def __init__(self, name):
        super().__init__(name, 150)

    def pet(self):
        self.health += 5
        print("pet")
        return self

class dragon(animal):
    def __init__(self, name):
        super().__init__(name, 170)

    def fly(self):
        print("fly")
        self.health -= 10
        return self
    
    def displayHealth(self):
        super().displayHealth()
        print("I am a Dragon")

class bird(animal):
    def __init__(self, name, health):
        super().__init__(name, health)


animal1 = animal('squirrel', 50)
animal1.walk().walk().walk().run().run().displayHealth()

chihuahua = dog("whatsupdawg")
chihuahua.walk().walk().walk().run().run().pet().displayHealth()

puff = dragon("puffthemagic")
puff.walk().fly().displayHealth()

ostrich = bird("ostrich", 90)
ostrich.walk().run().displayHealth()