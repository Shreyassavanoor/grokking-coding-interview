def remove_targets(arr, key):
    j = 0
    for i in  range(len(arr)):
        if arr[i] != key:
            arr[j] = arr[i]
            j += 1
    print(j)

def main():
    remove_targets([3, 2, 3, 6, 3, 10, 9, 3], 3)
    remove_targets([2, 11, 2, 2, 1], 2)
    remove_targets([], 2)
    remove_targets([1,1,1,1,1,1], 1)
    remove_targets([1,1,1,1,1,2], 1)


if __name__ == '__main__':
    main()
