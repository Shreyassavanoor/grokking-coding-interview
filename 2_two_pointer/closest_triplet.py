#wrong
def closet_triplet(arr, target):
    arr.sort()
    closet_sum = 0
    for i in range(len(arr)):
        x = arr[i]
        left = i + 1
        right = len(arr) - 1
        while(left < right):
            current_sum = arr[left] + arr[right]
            if current_sum < target - (x):
                closet_sum = max(closet_sum, current_sum + x)
                left += 1
            else:
                right -= 1
    print(closet_sum)


def main():
    closet_triplet([-2, 0, 1, 2], 2)
    closet_triplet([-3, -1, 1, 2], 1)
    closet_triplet([1, 0, 1, 1], 100)
    closet_triplet([-1,2,1,-4], 1)


if __name__ == '__main__':
    main()
