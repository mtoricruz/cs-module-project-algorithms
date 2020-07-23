'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # loop through length of array-1 
    for elem in range(len(arr)-1):
        # for every index in the length of array
        for i in range(len(arr)-1):
            # check if the index value is 0:
            if arr[i] == 0:
                # if it is, swap the integers
                arr[i+1], arr[i] = arr[i], arr[i+1]
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")