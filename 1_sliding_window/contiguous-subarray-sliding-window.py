def max_subarray_sum(arr, k):
    #sliding window approach
    start = 0
    window_sum = 0
    max_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start]
            start += 1
    return(max_sum)


def main():
    print(max_subarray_sum([2, 1, 5, 1, 3, 2], 3))
    print(max_subarray_sum([2, 3, 4, 1, 5], 2))

if __name__ == '__main__':
    main()

