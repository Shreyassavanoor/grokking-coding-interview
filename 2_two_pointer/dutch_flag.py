def dutch_flag(arr):
    left = 0
    right = len(arr) - 1
    i = 0 
    while i <= right:
        if arr[i] == 0:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
    print(arr)


def main():
    dutch_flag([1, 0, 2, 1, 0])

if __name__ == '__main__':
    main()