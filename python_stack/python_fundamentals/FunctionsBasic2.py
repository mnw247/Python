#1) Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].
def countDown(num):
    newarr = []
    for newarr in range (num, -1, -1):
        print(newarr)
countDown(5)

#2) Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.
def par (arr):
    print(arr[0])
    return(arr[1])
par ([2,3])

#3) First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.
def fpl (arr):
    sum = arr[0]+len(arr)
    print(sum)
    return sum
fpl([20,2,3,4,5])

#4) Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only one element long, have the function return False
def greater(arr):
    second = arr[1]
    newarr = []
    count = 0
    if (len(arr) == 1 ):
        return False
    for i in range (0, (len(arr)), 1):
        if (arr[i]>second):
            count += 1
            newarr.append(arr[i])
    print (newarr)
    print (count)
greater([12,34,50,22,28,40])

#5) This Length, That Value - Given two numbers, return array of length num1 with each value num2.  Print "Jinx!" if they are same.
num1 = 3
num2 = 3
arr = []
if (num1 == num2):
    print("Jinx!")
else:
    for i in range (0,num1,1):
        arr.append(num2)
    print (arr)