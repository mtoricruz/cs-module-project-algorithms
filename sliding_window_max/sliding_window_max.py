'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# U - nums is an array of integers.
# k is the max number of integers we can interact with, 
# within that interaction, return the highest integer in that interaction
# will need a separate empty array to store the highest integer from each interaction
# will move k number of interaction array in increments of 1
# to mimic a sliding window increment, we need a data structure that can push # on one side
# and pop a number on the other side


def sliding_window_max(nums, k):
    window_arr = []
    output = []
    while 0 < len(nums) - (k-1):
        for n in nums[0:k]:
            window_arr.append(n)
        window_arr.sort()
        max_number = window_arr[k-1]
        output.append(max_number)
        nums.pop(0)
        window_arr = []
    return output

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
