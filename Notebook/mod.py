def isPalindrome(word):
    if (word == word[::-1]):
        return "Palindrome"
    else:
        return "Not Plaindrome"
    
def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n-1))