#wrong not working in leetcode test for [1, 0, -1, 0, -2, 2] and target = 0
from collections import Counter
def find_quadraplet(arr, k):
    arr.sort()
    result = []
    arr_dict = Counter(arr)
    left = 0
    right = 0
    for i in range(len(arr)):
        if i > 0 and arr[i - 1] == arr[i]:
            continue
        left = i + 1
        right = len(arr) - 1
        while left < right:
            d = k - (arr[i] + arr[left] + arr[right])
            if d in arr_dict and arr_dict[d] > 0:
                arr_dict[arr[left]] -= 1
                arr_dict[arr[right]] -= 1
                arr_dict[arr[i]] -= 1
                result.append([arr[i], arr[left], arr[right], d])
                left += 1
                right -= 1
                while left < right and arr[left - 1] == arr[left]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            else:
                if d > k:
                    right -= 1
                else:
                    left += 1
    print(result)

def main():
    find_quadraplet([4, 1, 2, -1, 1, -3], 1)
    find_quadraplet([2, 0, -1, 1, -2, 2], 2)


if __name__ == '__main__':
    main()
