def find_pair_sum(array, target):
    if not array or not target:
        print('Either array or target is empty')
        return
    start_pointer = 0
    end_pointer = len(array) - 1

    while start_pointer <= end_pointer:
        current_sum = array[start_pointer] + array[end_pointer]
        if current_sum == target:
            print([start_pointer, end_pointer])
            return
    
        if current_sum > target:
            end_pointer -= 1
        else:
            start_pointer += 1

def main():
    find_pair_sum([1, 2, 3, 4, 6], 6)
    find_pair_sum([1, 2, 3, 4, 6], None)
    find_pair_sum([2, 5, 9, 11], 11)

if __name__ == '__main__':
    main()