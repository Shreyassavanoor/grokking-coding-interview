def remove_duplicates(arr):
    present = 0
    next = present + 1
    while (next <= len(arr) - 1):
        if arr[present] != arr[next]:
            arr[present + 1] = arr[next]
            present += 1
        next += 1
    print(f'Length of array is {present + 1}')
        

def main():
    remove_duplicates([2, 3, 3, 3, 6, 9, 9])
    remove_duplicates([2, 2, 2, 11])

if __name__ == '__main__':
    main()