# Define a function named comparetriples that takes two lists (a for Alice, b for Bob)
def comparetriples(a, b):
    alice = 0   # variable to count Alice's score
    bob = 0     # variable to count Bob's score

    # Loop through the indices of list a (both lists are of same length: 3 elements each)
    for i in range(len(a)):
        # If Alice's score is greater in this category, Alice gets 1 point
        if a[i] > b[i]:
            alice += 1
        # If Bob's score is greater in this category, Bob gets 1 point
        elif a[i] < b[i]:
            bob += 1
        # If both scores are equal, no points are awarded (do nothing)

    # Return the results as a list [Alice's score, Bob's score]
    return [alice, bob]


# Main program starts here
if __name__ == "__main__":
    # Read Alice's triplet from input, split into integers, and store as a list
    a = list(map(int, input().split()))

    # Read Bob's triplet from input, split into integers, and store as a list
    b = list(map(int, input().split()))

    # Call the function to compare both triplets and store the result
    result = comparetriples(a, b)

    # Print Alice's score and Bob's score separated by a space
    print(result[0], result[1])
