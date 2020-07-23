'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # create empty array to store products of index values
    product_array = []
    # assign index variable to a starting point of 0
    index = 0
    # assign another index variable at the starting point of 0
    subindex = 0

    # while index position is less than length of array:
    while index < len(arr):
        # create product with a value of 1
        product = 1
        # while subindex is less than length of array:
        while subindex < len(arr):
            # check if subindex is not at the same position as index
            if subindex != index:
                # if it is, assign new value of product to equal product * value of subindex in the array
                product *= arr[subindex]
            # increment subindex
            subindex += 1
        # append new product to the final product_array list
        product_array.append(product)
        # then increment index
        index += 1
        # reset subindex to starting point 
        subindex = 0
    # return final product list
    return product_array




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
