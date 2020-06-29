def square_array(arr):
    left = 0
    right = len(arr) - 1
    squared_array = [ 0 ] * len(arr)
    index = len(arr) - 1
    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square > right_square:
            squared_array[index] = left_square
            left += 1
        else:
            squared_array[index] = right_square
            right -= 1
        index -= 1
    print(f'Squared array is {squared_array}')


def main():
    square_array([-3,-2,-1,0,1,2])

if __name__ == '__main__':
    main()