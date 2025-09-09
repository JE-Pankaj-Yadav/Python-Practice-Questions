# Function to calculate the sum of very large numbers in a list
def aVeryBigSum(ar):
    a_sum = 0   # Start with sum = 0
    # Go through each element of the list
    for i in range(len(ar)):
        a_sum += ar[i]   # Add each number to the total sum
    return a_sum         # Return the final sum


# Main program starts here
if __name__ == "__main__":
    num = int(input())   # Read how many numbers the user will enter

    # Keep asking for input until user enters exactly 'num' numbers
    while True:
        arr = list(map(int, input().split()))  # Read numbers as a list
        if len(arr) == num:   # If count matches 'num', exit the loop
            break
        # If not correct length, show a message
        print(f"Please enter exactly {num} numbers!")

    # Call the function to calculate the sum of the array
    result = aVeryBigSum(arr)

    # Print the result
    print(result)
