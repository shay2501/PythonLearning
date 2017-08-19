import math
import string
#compute the volume of sphere given the radians

def vol(rad):
    volume = (4/3)*(math.pi)*(math.pow(rad, 3))
    return volume

#print(vol(9))

#check to see if a number is in a range
def ran_check(num, low, high):
    result = "Number " + str(num) + " is NOT in the range of ( " + str(low) + " , " + str(high) + " )"
    if num >= low:
        if num<= high:
            result = "Number " + str(num) + " is in the range of ( " + str(low) + " , " + str(high) + " )"
    print(result)


def ran_bool(num, low, high):
    result = False
    if num >= low and num<=high:
        result = True
    print(result)

#ran_check(10, 9, 10)
#ran_bool(11, 1, 10)

#count how many uppercase and lowercase letters are in a string
def up_low(s):
    lower = 0
    upper = 0
    for l in s:
        if string.ascii_lowercase.find(l) >= 0:
            lower+= 1
        elif string.ascii_uppercase.find(l) >=0:
            upper+= 1
    print ("The number of lowercase characters: " + str(lower))
    print ("The number of uppercase characters: " + str(upper))

#up_low("The Quick Brown Fox Jumped Over The Lazy Brown Dog")

#return a list of unique values
def unique_list(l):
    retlist = []

    for i in l:
        if i not in retlist:
            retlist.append(i)

    return retlist

#print(unique_list([1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,4,4,5]))

#multiply all numbers in a list
def multiply(numbers):
    val=1
    for n in numbers:
        val = val * n
    return val

#print(multiply([1,2,3,-4]))

#check whether string is a palindrome
def palindrome(s):
    test = "".join(s.lower().split())
    print(test[::-1])

palindrome("Hello")
