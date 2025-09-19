# --------------------------------------------------------------
# 🔰 50 Basic Python Practice Questions with Solutions
# --------------------------------------------------------------
# 📌 Author: Pankaj Kumar
# 📌 Description: Beginner-friendly Python practice problems
#     covering syntax, conditions, loops, strings, lists, and functions.
# 📌 Each question is solved with comments for easy understanding.
# --------------------------------------------------------------

# ==============================================================
# 🟢 Level 1 – Very Basic (Syntax, Variables, Input/Output)
# ==============================================================

# 1. Print "Hello, World!"
print("Hello, World!")

# 2. Take your name as input and print it.
name = input("Enter your name: ")
print("Your name is:", name)

# 3. Take two numbers as input and print their sum.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

# 4. Swap two variables (without using a third variable).
x, y = 5, 10
x, y = y, x
print("After swap: x =", x, "y =", y)

# 5. Check if a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# 6. Convert Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C = {fahrenheit:.2f}°F")

# 7. Find the area of a circle.
radius = float(input("Enter circle radius: "))
area = 3.14159 * radius * radius
print("Area of circle =", area)

# 8. Find Simple Interest (SI = P × R × T / 100).
P = float(input("Enter Principal: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))
SI = (P * R * T) / 100
print("Simple Interest =", SI)

# 9. Print square and cube of a number.
n = int(input("Enter a number: "))
print("Square =", n ** 2, "Cube =", n ** 3)

# 10. Print the largest of three numbers.
a, b, c = map(int, input("Enter 3 numbers separated by space: ").split())
print("Largest =", max(a, b, c))

# ==============================================================
# 🟡 Level 2 – Conditions & Loops
# ==============================================================

# 11. Print numbers from 1 to 10.
for i in range(1, 11):
    print(i, end=" ")
print()

# 12. Print multiplication table of a number.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")

# 13. Sum of first N natural numbers.
N = int(input("Enter N: "))
print("Sum =", sum(range(1, N + 1)))

# 14. Check if number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 15. Print even numbers from 1 to 50.
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print()

# 16. Print odd numbers from 1 to 50.
for i in range(1, 51):
    if i % 2 != 0:
        print(i, end=" ")
print()

# 17. Factorial of a number.
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)

# 18. Check if number is prime.
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# 19. Find sum of digits of a number.
num = int(input("Enter a number: "))
sum_digits = sum(int(digit) for digit in str(num))
print("Sum of digits =", sum_digits)

# 20. Reverse a number (e.g., 123 → 321).
num = int(input("Enter a number: "))
rev = 0
temp = num
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reversed number =", rev)

# ==============================================================
# 🔵 Level 3 – Strings
# ==============================================================

# 21. Length of a string.
s = input("Enter a string: ")
print("Length =", len(s))

# 22. Count vowels in a string.
s = input("Enter a string: ")
count = sum(1 for ch in s if ch.lower() in "aeiou")
print("Vowels =", count)

# 23. Check if string is palindrome.
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 24. Convert string to uppercase and lowercase.
s = input("Enter a string: ")
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

# 25. Count occurrences of a character in a string.
s = input("Enter a string: ")
ch = input("Enter character to count: ")
print(f"'{ch}' occurs {s.count(ch)} times.")

# 26. Replace spaces with '-'.
s = input("Enter a string: ")
print(s.replace(" ", "-"))

# 27. Concatenate two strings.
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Concatenated:", s1 + s2)

# 28. Check if string contains a word.
s = input("Enter a sentence: ")
word = input("Enter word to search: ")
if word.lower() in s.lower():
    print("Yes, contains word.")
else:
    print("No, not found.")

# 29. Reverse string without slicing.
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed:", rev)

# 30. Print each character on a new line.
s = input("Enter a string: ")
for ch in s:
    print(ch)

# ==============================================================
# 🟣 Level 4 – Lists
# ==============================================================

# 31. Create a list of 5 numbers.
lst = [1, 2, 3, 4, 5]
print(lst)

# 32. Find maximum and minimum in list.
print("Max:", max(lst), "Min:", min(lst))

# 33. Find sum of list elements.
print("Sum =", sum(lst))

# 34. Remove duplicates from list.
a = [1, 2, 2, 3, 4, 5, 5]
print("Unique list:", list(set(a)))

# 35. Sort a list ascending & descending.
a = [5, 2, 9, 1, 5, 6]
print("Ascending:", sorted(a))
print("Descending:", sorted(a, reverse=True))

# 36. Count occurrences of element in list.
a = [1, 2, 3, 2, 2, 5, 6]
print("2 occurs", a.count(2), "times")

# 37. Find second largest number.
a = [1, 5, 7, 9, 7, 9]
unique = list(set(a))
unique.sort()
print("Second largest =", unique[-2])

# 38. Take 5 numbers as input and store in list.
nums = [int(input(f"Enter number {i+1}: ")) for i in range(5)]
print(nums)

# 39. Merge two lists.
a = [1, 2, 3]
b = [4, 5]
print("Merged:", a + b)

# 40. Print even numbers from list.
a = [1, 2, 3, 4, 5, 6]
print("Even numbers:", [x for x in a if x % 2 == 0])

# ==============================================================
# 🟤 Level 5 – Functions & Misc
# ==============================================================

# 41. Function to find square.
def square(n):
    return n * n

print("Square =", square(5))

# 42. Function to check prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Prime?", is_prime(7))

# 43. Function to find factorial.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("Factorial of 5 =", factorial(5))

# 44. Function to check Armstrong number.
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == n

print("Armstrong?", is_armstrong(153))

# 45. Function to count vowels in string.
def count_vowels(s):
    return sum(1 for ch in s if ch.lower() in "aeiou")

print("Vowels:", count_vowels("Hello"))

# 46. Largest number in list.
def largest(lst):
    return max(lst)

print("Largest =", largest([1, 5, 9, 2]))

# 47. Smallest number in list.
def smallest(lst):
    return min(lst)

print("Smallest =", smallest([1, 5, 9, 2]))

# 48. Palindrome string check.
def palindrome(s):
    return s == s[::-1]

print("Palindrome?", palindrome("madam"))

# 49. GCD of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("GCD =", gcd(48, 18))

# 50. LCM of two numbers.
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print("LCM =", lcm(4, 6))
