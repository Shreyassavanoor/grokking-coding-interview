import math
def find_subarray_product(arr, target):
    count = 0
    for i in range(len(arr)):
        left = i
        right = i
        while left < len(arr) and right < len(arr):
            subarray = arr[left : right + 1]
            subarray_prod =  math.prod(subarray)
            if subarray_prod < target:
                right += 1
                count += 1
                #print(f'Subaary {subarray}')
            else:
                break
    print(count)


def main():
    find_subarray_product([2, 5, 3, 10], 30)
    find_subarray_product([8, 2, 6, 5], 50)

if __name__ == '__main__':
    main()