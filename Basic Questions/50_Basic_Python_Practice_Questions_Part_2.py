# =====================================================
# 🔰 50 NEW Basic Python Practice Questions with Solutions
# =====================================================

# Author: [Pankaj Yadav]
# Description: This file contains 50 beginner-friendly
# Python coding practice questions with solutions.
# Each solution is explained step by step through comments.
# =====================================================


# =====================================================
# 🟢 Level 1 – Beginner (Syntax, Variables, Input/Output)
# =====================================================

# 1. Print your name 5 times using a loop.
name = input("Enter the name: ")
for i in range(1, 6):
    print(f"Time {i}: {name}")


# 2. Take two numbers as input and print their difference.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
diff = abs(num1 - num2)  # abs() handles positive difference
print("Difference is:", diff)


# 3. Convert a number from kilometers to miles.
km = float(input("Enter the kilometers: "))
print(f"Miles: {km * 0.621371}")


# 4. Convert seconds to minutes and hours.
seconds = int(input("Enter the seconds: "))
minutes = seconds / 60
hours = minutes / 60
print("Minutes:", minutes)
print("Hours:", hours)


# 5. Take a number and print its square root.
# ❌ Mistake fixed → earlier it printed num*num (square).
import math

num = int(input("Enter the number: "))
print(f"Square root of {num} is {math.sqrt(num)}")


# 6. Take two numbers and print which one is greater.
a, b = map(int, input("Enter two numbers separated by space: ").split())
print("Greater number is:", max(a, b))


# 7. Take marks of 5 subjects and find the average and percentage.
marks = []
for i in range(1, 6):
    score = int(input(f"Enter marks of subject {i}: "))
    marks.append(score)

average = sum(marks) / 5
percentage = (sum(marks) / (5 * 100)) * 100
print("Average:", average)
print("Percentage:", percentage, "%")


# 8. Take a number and check if it is divisible by 5 and 11.
num = int(input("Enter the number: "))
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by 5 and 11")
else:
    print(f"{num} is not divisible by 5 and 11")


# 9. Take a character as input and check if it is a vowel or consonant.
char = input("Enter a character: ").lower()
if char in "aeiou":
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")


# 10. Take three sides of a triangle and check if it is valid or not.
a, b, c = map(int, input("Enter three sides of a triangle: ").split())
if (a + b > c) and (a + c > b) and (b + c > a):
    print("It is a valid triangle.")
else:
    print("It is not a valid triangle.")


# =====================================================
# 🟡 Level 2 – Conditions & Loops
# =====================================================

# 11. Print numbers from 10 to 1 in reverse order.
for i in range(10, 0, -1):
    print(i)

# 12. Print all multiples of 3 between 1 and 50.
for i in range(1, 51):
    if i % 3 == 0:
        print(i)

# 13. Find the sum of all even numbers from 1 to 100.
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print("Sum of even numbers from 1 to 100:", total)

# 14. Find the sum of all odd numbers from 1 to 100.
total = 0
for i in range(1, 101):
    if i % 2 != 0:
        total += i
print("Sum of odd numbers from 1 to 100:", total)

# 15. Count how many digits are in a given number.
num = input("Enter the number: ")
print("Digits count:", len(num))

# 16. Find the largest digit in a number.
num = input("Enter the number: ")
print("Largest digit:", max(num))

# 17. Find the smallest digit in a number.
num = input("Enter the number: ")
print("Smallest digit:", min(num))

# 18. Check if a number is an Armstrong number.
num = int(input("Enter the number: "))
digits = str(num)
length = len(digits)
total = sum(int(d) ** length for d in digits)
if num == total:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

# 19. Check if a number is a Perfect number.
num = int(input("Enter the number: "))
div_sum = sum(i for i in range(1, num) if num % i == 0)
if div_sum == num:
    print(f"{num} is a Perfect number")
else:
    print(f"{num} is not a Perfect number")

# 20. Check if a number is a Strong number.
# Strong number = sum of factorial of digits == number
import math

num = int(input("Enter the number: "))
digits = str(num)
fact_sum = sum(math.factorial(int(d)) for d in digits)
if num == fact_sum:
    print(f"{num} is a Strong number")
else:
    print(f"{num} is not a Strong number")


# =====================================================
# 🔵 Level 3 – Strings
# =====================================================

# 21. Count how many words are in a string.
string = input("Enter a sentence: ")
print("Number of words:", len(string.split()))

# 22. Check if a string starts with a vowel.
string = input("Enter a string: ")
if string[0].lower() in "aeiou":
    print("The string starts with a vowel.")
else:
    print("The string does not start with a vowel.")

# 23. Count uppercase and lowercase letters in a string.
string = input("Enter a sentence: ")
upper, lower = 0, 0
for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase letters:", upper, "Lowercase letters:", lower)

# 24. Count digits and special characters in a string.
string = input("Enter a sentence: ")
digits, special = 0, 0
for ch in string:
    if ch.isdigit():
        digits += 1
    elif not ch.isalpha() and not ch.isspace():
        special += 1
print("Digits:", digits, "Special characters:", special)

# 25. Remove all vowels from a string.
string = input("Enter a sentence: ")
result = "".join(ch for ch in string if ch.lower() not in "aeiou")
print("After removing vowels:", result)

# 26. Find the frequency of each character in a string.
string = input("Enter a sentence: ")
freq = {}
for ch in string:
    if ch != " ":
        freq[ch] = freq.get(ch, 0) + 1
print("Character frequencies:")
for key, val in freq.items():
    print(key, ":", val)

# 27. Check if two strings are anagrams.
str1, str2 = input("Enter two words separated by space: ").split()
if sorted(str1.lower()) == sorted(str2.lower()):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# 28. Find the longest word in a string.
words = input("Enter a sentence: ").split()
longest = max(words, key=len)
print("Longest word is:", longest)

# 29. Print the first and last character of a string.
string = input("Enter a string: ")
print("First character:", string[0], "Last character:", string[-1])

# 30. Convert the first letter of every word in a string to uppercase.
string = input("Enter a sentence: ")
print("Capitalized string:", string.title())


# =====================================================
# 🟣 Level 4 – Lists
# =====================================================

# 31. Create a list of numbers from 1 to 10 using a loop.
nums = []
for i in range(1, 11):
    nums.append(i)
print(nums)

# 32. Calculate the product of all elements in a list.
my_list = [1, 2, 3, 4, 5]
product = 1
for num in my_list:
    product *= num
print("Product of list elements:", product)

# 33. Find all unique elements in a list.
my_list = [1, 1, 12, 4, 5, 5, 3, 4, 5]
print("Unique elements:", list(set(my_list)))

# 34. Find common elements between two lists.
list1 = [1, 1, 12, 4, 5, 5, 3, 4, 5]
list2 = [2, 6, 12, 9, 5, 3, 3, 4, 5]
common = sorted(set(list1) & set(list2))
print("Common elements:", common)

# 35. Remove all even numbers from a list.
list1 = [1, 1, 12, 4, 5, 5, 3, 4, 5]
odds = [num for num in list1 if num % 2 != 0]
print("List without even numbers:", odds)

# 36. Remove all odd numbers from a list.
list1 = [1, 1, 12, 4, 5, 5, 3, 4, 5]
evens = [num for num in list1 if num % 2 == 0]
print("List without odd numbers:", evens)

# 37. Find the average of numbers in a list.
list1 = [1, 1, 12, 4, 5, 5, 3, 4, 5]
average = sum(list1) / len(list1)
print("Average:", average)

# 38. Check if a number exists in a list.
list1 = [1, 1, 12, 4, 5, 5, 3, 4, 5]
num = 5
if num in list1:
    print(num, "exists in the list")
else:
    print(num, "does not exist in the list")

# 39. Print index of all occurrences of a given element in a list.
list1 = [1, 1, 12, 4, 5, 5, 3, 4, 5]
element = 5
print("Indexes of", element, ":", [i for i in range(len(list1)) if list1[i] == element])

# 40. Reverse a list without using reverse() or slicing.
list1 = [1, 1, 12, 4, 5, 5, 3, 4, 5]
reversed_list = []
for i in range(len(list1) - 1, -1, -1):
    reversed_list.append(list1[i])
print("Reversed list:", reversed_list)


# =====================================================
# 🟤 Level 5 – Functions & Misc
# =====================================================


# 41. Write a function to calculate compound interest.
def compound_interest(P, R, T):
    """
    P = Principal amount
    R = Rate of Interest (% per year)
    T = Time in years
    Formula: CI = P * (1 + R/100)^T - P
    """
    CI = P * (1 + R / 100) ** T - P
    return CI


print(
    "Compound Interest:",
    compound_interest(
        int(input("Principal: ")),
        float(input("Rate of Interest: ")),
        int(input("Time (years): ")),
    ),
)


# 42. Write a function to print Fibonacci series up to N terms.
def fibonacci(n):
    """
    Fibonacci sequence:
    F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)
    """
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq[:n]  # return only n terms


print("Fibonacci series:", fibonacci(int(input("Enter number of terms: "))))


# 43. Write a function to check if a number is palindrome.
def is_palindrome(num):
    """
    A number is palindrome if it reads the same
    forward and backward.
    """
    return str(num) == str(num)[::-1]


n = int(input("Enter a number: "))
print(n, "is palindrome?", is_palindrome(n))


# 44. Write a function to convert decimal to binary.
def decimal_to_binary(num):
    """
    Convert decimal to binary by repeated division by 2.
    """
    if num == 0:
        return "0"
    bits = []
    while num > 0:
        bits.append(str(num % 2))
        num //= 2
    return "".join(reversed(bits))


n = int(input("Enter decimal number: "))
print("Binary:", decimal_to_binary(n))


# 45. Write a function to convert binary to decimal.
def binary_to_decimal(binary_str):
    """
    Convert binary string → decimal number.
    """
    decimal = 0
    power = 0
    for digit in binary_str[::-1]:  # process from rightmost bit
        if digit == "1":
            decimal += 2**power
        power += 1
    return decimal


binary = input("Enter binary number: ")
print("Decimal:", binary_to_decimal(binary))


# 46. Write a function to find sum of digits of a number.
def sum_of_digits(num):
    return sum(int(d) for d in str(num))


n = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(n))


# 47. Write a function to calculate power of a number (x^y).
def power(x, y):
    """
    Raise x to power y (x^y).
    """
    result = 1
    for _ in range(y):
        result *= x
    return result


x = int(input("Enter base: "))
y = int(input("Enter exponent: "))
print(f"{x}^{y} =", power(x, y))


# 48. Write a function to count words in a string.
def word_count(sentence):
    """
    Count number of words in a string
    by splitting using whitespace.
    """
    return len(sentence.split())


sentence = input("Enter a sentence: ")
print("Word count:", word_count(sentence))


# 49. Write a function to merge two lists and remove duplicates.
def merge_lists(a, b):
    """
    Merge two lists and remove duplicates using set().
    """
    return list(set(a + b))


a = [1, 2, 4, 6, 8, 9, 1, 4]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Merged list without duplicates:", merge_lists(a, b))


# 50. Write a function to find the mode (most repeated element) in a list.
def find_mode(lst):
    """
    Mode = element that occurs most frequently.
    """
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    # find element with max frequency
    max_count = max(freq.values())
    mode = [k for k, v in freq.items() if v == max_count]
    return mode, max_count


lst = [1, 3, 5, 7, 9, 3]
mode, count = find_mode(lst)
print("Mode:", mode, "appears", count, "times")
