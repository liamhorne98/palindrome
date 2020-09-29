def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
num1=str(input("Enter string:"))
if(is_palindrome(num1) == True):
    print("String is a palindrome")
else:
    print("String is not a palindrome")
#Task2
def isEven(num):
    if (num < 2):
        return (num % 2 == 0)
    return (isEven(num - 2))
num = int(input("Enter the number for check odd or even: "))
if (isEven(num) == True):
    print(num, "is an even number")
else:
    print(num, "is an odd number")