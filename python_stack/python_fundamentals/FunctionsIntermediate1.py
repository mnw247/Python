# randInt() returns a random integer between 0 to 100
import random
def randInt():
    x = 0
    x = int(random.random()*101)
    return x
y = randInt()
print (y)

# randInt(max=50) returns a random integer between 0 to 50
import random
def randInt(max=51):
    x = 0
    x = int(random.random()*max)
    return x
y = randInt()
print (y)

# randInt(min=50) returns a random integer between 50 to 100
import random
def randInt(max=51):
    x = 0
    x = int(random.random()*max)+50
    return x
y = randInt()
print (y)

# randInt(min=50, max=500) returns a random integer between 50 and 500
import random
def randInt(min=50,max=500):
    x = 0
    max = max-49
    x = int(random.random()*(max+1-min))+min
    return x
y = randInt()
print (y)