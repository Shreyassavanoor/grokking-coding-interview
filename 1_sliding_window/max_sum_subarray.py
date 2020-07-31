'''Given an array of positive numbers and a positive number ‘k’, 
   find the maximum sum of any contiguous subarray of size ‘k’.

   Ex:1
   Input: [2, 1, 5, 1, 3, 2], k=3 
   Output: 9
   Explanation: Subarray with maximum sum is [5, 1, 3].
'''

def find_max_sum_subaarray(arr, k):
    window_start = 0
    max_sum = 0
    window_sum = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    
    print(f'Maximum sum is {max_sum}')

def main():
    find_max_sum_subaarray([2, 1, 5, 1, 3, 2], 3)
    find_max_sum_subaarray([2, 3, 4, 1, 5], 2)

if __name__ == '__main__':
    main()