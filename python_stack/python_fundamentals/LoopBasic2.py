#1)Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
arr=[-1,3,5,-5]
def makeItBig():
    for i in range(0,len(arr),1):
        if(arr[i]>0):
            arr[i] = "big"
    return arr
print(makeItBig())


#2)Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to b a positive number).
arr=[-1,1,1,1]
def countPositives():
    sum = 0
    for i in range(0,len(arr),1):
        if(arr[i]>0):
            sum += 1
    arr [len(arr)-1] = sum
    return arr
print(countPositives())


#3)SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10
def sumTotal(arr):
    x = 0    
    for i in arr:
        x = x + i
    return x
print(sumTotal([1,2,3,4]))


#4)Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5
def average(arr):
    sum = 0
    for i in range (0,len(arr),1):
        sum = sum + arr[i]
    sum = sum/len(arr)
    print (sum)
average([1,2,3,4])

#5)Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4
def Length(arr):
    print(len(arr))
    return arr
Length ([1,2,3,4])


#6)Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(arr):
    if (len(arr)<1):
        return false
    else:
        temp = arr[0]
        for i in range (0, len(arr),1):
            if(arr[i]<temp):
                temp = arr[i]
        print (temp)
minimum([-1,-2,-3])

#7)Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -3.

def maximum(arr):
    if (len(arr)<1):
        return false
    else:
        temp = arr[0]
        for i in range (0, len(arr),1):
            if(arr[i]>temp):
                temp = arr[i]
        print (temp)
maximum([1,2,3,4])

#8)UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
def ultimate(arr):
    min = arr[0]
    max = arr[0]
    sumTotal = 0
    for i in range (0, len(arr),1):
        sumTotal = sumTotal + arr[i]
        if(arr[i] < min):
            min = arr[i]
        if(arr[i] > max):
            max = arr[i]

    average = sumTotal/len(arr)
    length = len(arr)

    L = {
        "total" : sumTotal,
        "average" : average,
        "minimum" : min,
        "maximum" : max,
        "lenth" : length
    }

    return L

x = ultimate([1,2,3,4,5,6,7,8,9])
print(x)

#9)ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.

def ReverseList (arr):
    for i in range (0,len(arr)/2,1):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr
x = ReverseList([1,2,3,4,5,6])
print(x)