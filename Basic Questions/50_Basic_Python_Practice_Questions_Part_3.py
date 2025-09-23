# ==============================================================
# 🔰 80 Basic Python Practice Questions with Solutions
# Author: Pankaj Yadav
# GitHub: https://github.com/JE-Pankaj-Yadav
# ==============================================================

# ==============================================================
# 1–10: Loops (for, while)
# ==============================================================

# 1. Print numbers from 1 to 20 using a for loop.
for i in range(1, 21):
    print(i, end=" ")
print("\n")

# 2. Print numbers from 20 to 1 using a while loop.
i = 20
while i >= 1:
    print(i, end=" ")
    i -= 1
print("\n")

# 3. Print all even numbers between 1 and 50.
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")

# 4. Print all odd numbers between 1 and 50.
for i in range(1, 51):
    if i % 2 != 0:
        print(i, end=" ")
print("\n")

# 5. Print the multiplication table of a number input by the user.
num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")

# 6. Calculate the sum of first n natural numbers using a loop.
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)

# 7. Find the factorial of a given number using a loop.
n = int(input("Enter a number for factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)

# 8. Print the Fibonacci series up to n terms.
n = int(input("Enter number of terms for Fibonacci series: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])
print("Fibonacci Series:", fib[:n])

# 9. Count the number of digits in a number using a while loop.
num = int(input("Enter a number: "))
count = 0
temp = num
while temp > 0:
    temp //= 10
    count += 1
print("Number of digits:", count)

# 10. Print all numbers divisible by 3 and 5 between 1 and 100.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
print("\n")


# ==============================================================
# 11–20: Conditionals (if, if-else, if-elif-else)
# ==============================================================

# 11. Check if a number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 12. Check if a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 13. Find the largest of three numbers.
a, b, c = map(int, input("Enter three numbers separated by space: ").split())
print("Largest =", max(a, b, c))

# 14. Check whether a year is a leap year.
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 15. Check if a character is a vowel or consonant.
char = input("Enter a character: ")
if char.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# 16. Check if a number is divisible by 2, 3, and 5.
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
    print("Yes! Divisible by 2, 3, and 5")
else:
    print("No!")

# 17. Print grade based on marks.
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Fail")

# 18. Check if a number is a prime number.
num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is Prime")
    else:
        print(num, "is Not Prime")

# 19. Check whether a string is empty or not.
s = input("Enter a string: ")
if not s.strip():
    print("Empty String")
else:
    print("Not Empty")

# 20. Determine whether a person is eligible to vote (age ≥ 18).
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")


# ==============================================================
# 21–30: Strings
# ==============================================================

# 21. Take a string input and print it in reverse.
s = input("Enter a string: ")
print("Reverse:", s[::-1])

# 22. Count the number of vowels in a string.
s = input("Enter a string: ")
count = sum(1 for ch in s if ch.lower() in "aeiou")
print("Number of vowels:", count)

# 23. Count the number of words in a string.
s = input("Enter a string: ")
print("Word count:", len(s.split()))

# 24. Convert a string to uppercase.
s = input("Enter a string: ")
print(s.upper())

# 25. Convert a string to lowercase.
s = input("Enter a string: ")
print(s.lower())

# 26. Check if a string is a palindrome.
s = input("Enter a string: ")
if s.lower() == s[::-1].lower():
    print("Palindrome")
else:
    print("Not Palindrome")

# 27. Find the length of a string without using len().
s = input("Enter a string: ")
count = 0
for _ in s:
    count += 1
print("Length =", count)

# 28. Remove spaces from a string.
s = input("Enter a string: ")
print("Without spaces:", s.replace(" ", ""))

# 29. Replace a word in a string with another word.
s = input("Enter a sentence: ")
print("Updated:", s.replace("pankaj", "Pankaj Ji"))

# 30. Check if a string starts with a given substring.
s = "Pankaj is a good boy"
if s.startswith("Pankaj"):
    print("Yes, starts with 'Pankaj'")
else:
    print("No!")


# ==============================================================
# 31–40: Lists
# ==============================================================

# 31. Create a list of numbers from 1 to 10.
lst = [i for i in range(1, 11)]
print(lst)

# 32. Print all elements of a list using a loop.
for i in lst:
    print(i, end=" ")
print("\n")

# 33. Find the sum of all elements in a list.
print("Sum =", sum(lst))

# 34. Find the largest element in a list.
print("Max =", max(lst))

# 35. Find the smallest element in a list.
print("Min =", min(lst))

# 36. Count how many times a number appears in a list.
lst = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 2, 2, 2, 10]
print("Count of 2 =", lst.count(2))

# 37. Remove duplicate elements from a list (keeping order).
lst = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 2, 2, 2, 10]
unique = []
for x in lst:
    if x not in unique:
        unique.append(x)
print("Without duplicates:", unique)

# 38. Reverse a list.
lst = [1, 2, 3, 4, 5]
print("Reversed:", lst[::-1])

# 39. Sort a list in ascending order.
lst = [6, 7, 3, 4, 5, 9, 8, 1, 2, 2, 10]
print("Ascending:", sorted(lst))

# 40. Sort a list in descending order.
print("Descending:", sorted(lst, reverse=True))


# ==============================================================
# 41–50: Sets
# ==============================================================

sets = {1, 2, 5, 5, 3, 8, 3, 4}  # duplicate removed automatically
print(sets)

# 42. Add a new element to a set.
sets.add(10)
print("After adding:", sets)

# 43. Remove an element from a set.
sets.remove(5)  # remove specific element
print("After removal:", sets)

# 44. Find the length of a set.
print("Length =", len(sets))

# 45. Union of two sets.
a = {1, 4, 8, 3, 5}
b = {1, 2, 34, 6, 7, 5, 4}
print("Union =", a.union(b))

# 46. Intersection of two sets.
print("Intersection =", a.intersection(b))

# 47. Difference between two sets.
print("A - B =", a.difference(b))
print("B - A =", b.difference(a))

# 48. Check if a set is a subset of another set.
print("A subset B?", a.issubset(b))
print("B subset A?", b.issubset(a))

# 49. Check if a set is a superset of another set.
print("A superset B?", a.issuperset(b))
print("B superset A?", b.issuperset(a))

# 50. Remove all elements from a set.
sets.clear()
print("Cleared set:", sets)


# ==============================================================
# 51–60: Tuples
# ==============================================================

# 51. Create a tuple with 5 numbers.
tup = (1, 2, 3, 4, 5)
print(tup)

# 52. Access the 3rd element of a tuple.
print("3rd element =", tup[2])

# 53. Find the length of a tuple.
print("Length =", len(tup))

# 54. Count how many times a value occurs in a tuple.
tup = (1, 2, 3, 4, 5, 2, 4, 3, 3, 3, 6, 7, 8, 9)
print("Count of 3 =", tup.count(3))

# 55. Find the largest element in a tuple.
print("Max =", max(tup))

# 56. Find the smallest element in a tuple.
print("Min =", min(tup))

# 57. Concatenate two tuples.
a = (1, 2, 3)
b = (4, 5, 6)
print("Concatenated =", a + b)

# 58. Repeat a tuple multiple times.
print("Repeated:", a * 4)

# 59. Convert a tuple into a list.
print("As list:", list(a))

# 60. Slice a tuple to get the first three elements.
print("First 3:", tup[:3])


# ==============================================================
# 61–70: Dictionaries
# ==============================================================

# 61. Create a dictionary with 5 key-value pairs.
info = {"Name": "Pankaj", "Study": "B.Tech", "City": "Gorakhpur", "State": "U.P", "PIN": 273409}
print(info)

# 62. Access a value using its key.
print("Name =", info["Name"])

# 63. Update the value of a key.
info["Name"] = "Pankaj Ji"
print("Updated:", info)

# 64. Add a new key-value pair.
info["Country"] = "India"
print(info)

# 65. Delete a key-value pair.
info.pop("Study")
print(info)

# 66. Print all keys of a dictionary.
print("Keys:", list(info.keys()))

# 67. Print all values of a dictionary.
print("Values:", list(info.values()))

# 68. Count character frequencies in a string using dictionary.
s = "hello world"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print("Frequencies:", freq)

# 69. Merge two dictionaries.
d1 = {"a": 1, "b": 2}
d2 = {"c": 3}
d1.update(d2)
print("Merged:", d1)

# 70. Check if a key exists in a dictionary.
if "City" in info:
    print("Key exists")
else:
    print("Key not found")


# ==============================================================
# 71–80: Functions
# ==============================================================

# 71. Square of a number.
def square(num):
    return num ** 2

print(square(5))

# 72. Factorial of a number.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))

# 73. Prime check.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))

# 74. Sum of elements in a list.
def sum_list(lst):
    return sum(lst)

print(sum_list([1, 2, 3, 4, 5]))

# 75. Reverse a string.
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))

# 76. Largest of three numbers.
def largest(a, b, c):
    return max(a, b, c)

print(largest(3, 7, 5))

# 77. Check even or odd.
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(even_odd(6))

# 78. Count vowels in a string.
def count_vowels(s):
    return sum(1 for ch in s if ch.lower() in "aeiou")

print(count_vowels("Hello World"))

# 79. Celsius to Fahrenheit.
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

print(celsius_to_fahrenheit(37))

# 80. Check if string is palindrome.
def palindrome(s):
    return s.lower() == s[::-1].lower()

print(palindrome("Madam"))
