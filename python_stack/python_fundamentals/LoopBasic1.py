#1) Basic - Print all the numbers/integers from 0 to 150.
for count in range(0,151):
    print(count)

#2) Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
for count in range (0,1000001,5):
    print(count)

#3) Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for count in range (1,101):
    x = ''
    if count % 5 == 0:
        x = "Coding"
        if count % 10 == 0:
            x = x + " Dojo"
        print (x)
    else:
        print (count)

#4) Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range (0,500000,1):
    if (x%2!=0):
        sum = sum + x
print (sum)


#5) Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
for count in range (2018,0,-4):
    print (count)


#6) Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for count in range (lowNum,highNum+1,1):
    if (count % mult == 0):
        print(count)


# list = [3,5,1,2]
# for i in list:
#     print(i)
3,5,1,2

# list = [3,5,1,2]
# for i in range(list):
#     print(i)
error because list is a list and not a integer value

# list = [3,5,1,2]
# for i in range(len(list)):
#     print(i)
0,1,2,3