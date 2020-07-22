'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    for elem in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i]== 0:
                arr[i+1], arr[i] = arr[i], arr[i+1]
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")