class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, fNum, *aNums):
        self.result += fNum
        for i in range(0,len(aNums)):
            self.result += aNums[i]
        return self
    def subtract(self, fNum, *aNums):
        self.result -= fNum
        for i in range(0,len(aNums)):
            self.result -= aNums[i]
        return self 

md = MathDojo()
print(md.add(2).add(2,5,1).subtract(3,2).result)