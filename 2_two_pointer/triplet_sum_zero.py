def triplet_sum_zero(arr):
    arr[:] = list(set(arr))
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        current_no = arr[i]
        left = i + 1
        right = len(arr) - 1
        while(left < right):
            req_sum = arr[left] + arr[right]
            if req_sum == -current_no:
                triplets.append([current_no, arr[left], arr[right]])
                left += 1
                right -= 1
                continue
            if req_sum < -current_no:
                left += 1
            else:
                right -= 1
    print(triplets)


def main():
    triplet_sum_zero([-3, 0, 1, 2, -1, 1, -2])
    triplet_sum_zero([-5, 2, -1, -2, 3])


if __name__ == '__main__':
    main()
