
# Option 1.
a = [1, 2, 3, 4, 10, 11]  # input array
b = 0                     # variable to store sum
for i in range(0, len(a), 1):   # loop through all indices of array
    b = b + a[i]                # add each element to b
print(b)                        # print total sum


# Option 2.
a = [1, 2, 3, 4, 10, 11]
print(sum(a))

# Option 3.
n = int(input())                         # first line: number of elements
a = list(map(int, input().split()))      # second line: n space-separated integers
print(sum(a))

