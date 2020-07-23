'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# U - we have an array where every element shows up twice except 1, return that 1 element. Loop through the array. Check to see if that element is in current array. If there is element that doesn't show up twice, return that element

def single_number(arr):
    # create array to store odd number
    list_1 = []
    # Loop through array
    for elem in arr:
        # check if elem is in list_1, if so remove it
        if elem in list_1:
            list_1.remove(elem)
        # if elem is not in list_1, add to list
        else:
            list_1.append(elem)
    # after full loop, pop number in list and return that value
    return list_1.pop()

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")