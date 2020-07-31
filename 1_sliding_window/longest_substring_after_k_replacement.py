'''
    Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with
    any letter, find the length of the longest substring having the same letters after replacement.

    AND

    Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
    find the length of the longest contiguous subarray having all 1s.

    Input: String="aabccbb", k=2
    Output: 5
    Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
'''

def find_longest_substring(s, k):
    window_start = 0
    max_length = 0
    char_dic = {}
    max_repeat_char = 0

    for window_end in range(len(s)):
        char = s[window_end]
        if char not in char_dic:
            char_dic[char] = 0
        char_dic[char] += 1
        max_repeat_char = max(max_repeat_char, char_dic[char])

        if window_end - window_start + 1 - max_repeat_char > k:
            char_dic[s[window_start]] -= 1
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)

    print(f'Maximum length is {max_length}')

def main():
    find_longest_substring('aabccbb', 2)
    find_longest_substring('abbcb', 1)
    find_longest_substring('abccde', 1)


if __name__ == '__main__':
    main()