'''
    Given a string, find the length of the longest substring in it with no more than K distinct characters.
    Fruits in basket problem

    Example:
    Input: String="araaci", K=2
    Output: 4
    Explanation: The longest substring with no more than '2' distinct characters is "araa".
'''

def longest_substring_k(string, k):
    window_start = 0
    max_length = 0
    char_dict = {}

    for window_end in range(len(string)):
        char = string[window_end]
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1

        while len(char_dict) > k:
            max_length = max(max_length, window_end - window_start)
            throw_char = string[window_start]
            char_dict[throw_char] -= 1
            if char_dict[throw_char] == 0:
                del char_dict[throw_char]
            window_start += 1

    print(f'Maximum length is {max_length}')


def main():
    longest_substring_k('araaci', 2)
    longest_substring_k('araaci', 1)
    longest_substring_k('cbbebi', 3)

if __name__ == '__main__':
    main()