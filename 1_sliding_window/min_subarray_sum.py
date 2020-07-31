'''
    Given an array of positive numbers and a positive number ‘S’,
    find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
    Return 0, if no such subarray exists.

    Ex:
    Input: [2, 1, 5, 2, 3, 2], S=7 
    Output: 2
    Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
'''
import math
def min_subarray_sum(arr, s):
    window_start = 0
    window_sum = 0
    min_length = math.inf

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            window_sum -= arr[window_start]
            min_length = min(min_length, window_end - window_start + 1)
            window_start += 1
    if min_length < math.inf:
        print(f'Minimum length is {min_length}')
    else:
        print('Minimum length is 0')
    

def main():
    min_subarray_sum([2, 1, 5, 2, 3, 2], 7)
    min_subarray_sum([2, 1, 5, 2, 8], 7)
    min_subarray_sum([3, 4, 1, 1, 6], 8)

if __name__ == '__main__':
    main()