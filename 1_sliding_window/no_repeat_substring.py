'''
    Given a string, find the length of the longest substring which has no repeating characters.

    Input: String="aabccbb"
    Output: 3
    Explanation: The longest substring without any repeating characters is "abc".
'''

def find_no_repeat_substring(s):
    window_start = 0
    max_length = 0
    char_dic = {}

    for window_end in range(len(s)):
        char = s[window_end]
        if char in char_dic:
            window_start = char_dic[char] + 1
        char_dic[char] = window_end
        max_length = max(max_length, window_end - window_start + 1)

    print(f'Maximum length is {max_length}')

def main():
    find_no_repeat_substring('aabccbb')
    find_no_repeat_substring('abbbb')
    find_no_repeat_substring('abccde')
    find_no_repeat_substring('abcdefghijklm')
    find_no_repeat_substring('aaaaaaaa')



if __name__ == '__main__':
    main()