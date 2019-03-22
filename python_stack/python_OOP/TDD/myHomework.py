def reverseList(x):
    for i in range (int(len(x)/2)):
       temp = x[i]
       x[i] = x[len(x)-1-i]
       x[len(x)-1-i] = temp
    return x
x = [1,3,5,7,8,9]
print(reverseList(x))

def isPalindrome(x):
    for i in range (int(len(x)/2)):
       temp = x[i]
       x[i] = x[len(x)-1-i]
       x[len(x)-1-i] = temp
    return x
x = [1,3,5,7,8,9]
print(reverseList(x))