n = int(input())

if n % 2 != 0:               # if n is odd
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:   # even and in range 2 to 5
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:  # even and in range 6 to 20
    print("Weird")
elif n % 2 == 0 and n > 20:        # even and greater than 20
    print("Not Weird")
