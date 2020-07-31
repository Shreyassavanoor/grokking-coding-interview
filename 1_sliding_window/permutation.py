'''
    Given a string and a pattern, find out if the string contains any permutation of the pattern.

    AND

    Given a string and a pattern, find all anagrams of the pattern in the given string.
    Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

    Input: String="oidbcaf", Pattern="abc"
    Output: true
    Explanation: The string contains "bca" which is a permutation of the given pattern.
'''
import collections
def find_permutation(s, pattern):
    window_start = 0
    char_dic = collections.Counter(pattern)
    matched = 0

    for window_end in range(len(s)):
        char = s[window_end]

        if char in char_dic:
            char_dic[char] -= 1
            if char_dic[char] == 0:
                matched += 1
        
        if matched == len(char_dic):
            print(f'Permutation found')
            return

        if window_end  >= len(pattern) - 1:
            start_char = s[window_start]
            if start_char in char_dic:
                if char_dic[start_char] == 0:
                    matched -= 1
                char_dic[start_char] += 1
            window_start += 1
    
    print('Permutation not found')

def main():
    find_permutation('oidbcaf', 'abc')
    find_permutation('odicf', 'dc')
    find_permutation('bcdxabcdy', 'bcdxabcdy')


if __name__ == '__main__':
    main()