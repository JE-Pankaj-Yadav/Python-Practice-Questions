# Option 1.
print("Enter the size of the matrix:")
num = int(input())   # Read the size of the matrix (matrix will be num x num)

matrix = []          # Empty list to store the matrix
L2R_Digonal = 0      # Variable to store sum of Left-to-Right diagonal
R2L_Digonal = 0      # Variable to store sum of Right-to-Left diagonal

# Taking input for the matrix
for i in range(num):
    row = []   # Empty row
    for j in range(num):
        # Ask user to enter element at position (i, j)
        value = int(input(f"Enter element at position [{i}][{j}]: "))
        row.append(value)   # Add the element to the row
    matrix.append(row)      # Add the row to the matrix

# Printing the matrix in a proper way
for i in range(num):
    for j in range(num):
        print(matrix[i][j], end=" ")   # Print elements of each row in one line
    print()   # Move to next line after printing one row

# Calculating diagonal sums
for i in range(num):
    L2R_Digonal += matrix[i][i]               # Main diagonal (↘ top-left to bottom-right)
    R2L_Digonal += matrix[i][num - i - 1]     # Other diagonal (↙ top-right to bottom-left)

# Printing diagonal sums
print("\nSum of left-to-right diagonal:", L2R_Digonal)
print("Sum of right-to-left diagonal:", R2L_Digonal)

# Calculating the absolute difference between the two diagonals
diff = 0
if L2R_Digonal > R2L_Digonal:
    diff = L2R_Digonal - R2L_Digonal
elif R2L_Digonal > L2R_Digonal:
    diff = R2L_Digonal - L2R_Digonal
else:
    diff = 0   # Both are equal, so difference is 0

# Print the difference
print("The absolute difference between diagonals is:", diff)

# Option 2. 
