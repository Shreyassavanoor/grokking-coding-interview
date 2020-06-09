import math

def max_subarray_given_sum(arr, s):
    #sliding window approach
    start = 0
    window_sum = 0
    min_length = math.inf
    for i in range(len(arr)):
        window_sum += arr[i]

        #if window sum >= s try to shring the window
        while window_sum >= s:
            min_length = min(min_length, i - start + 1)
            window_sum -= arr[start]
            start += 1

    if min_length == math.inf:
        return 0
        
    return min_length 


def main():
    print(max_subarray_given_sum([2, 1, 5, 1, 3, 2], 3))
    print(max_subarray_given_sum([2, 3, 4, 1, 5], 2))
    print(max_subarray_given_sum([2, 1, 5, 2, 3, 2], 7))
    print(max_subarray_given_sum([2, 1, 5, 2, 8], 7 ))
    print(max_subarray_given_sum([3, 4, 1, 1, 6], 8 ))

if __name__ == '__main__':
    main()