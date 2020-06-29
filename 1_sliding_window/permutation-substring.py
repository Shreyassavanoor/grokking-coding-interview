def find_permutation_substring(string, pattern):
    window_start = 0
    pattern_length = len(pattern)
    pattern_dict = {}
    string_dict = {}
    chars_processed = 0

    for p in range(pattern_length):
        if pattern[p] not in pattern_dict:
            pattern_dict[pattern[p]] = 0
        pattern_dict[pattern[p]] += 1

    for i in range(len(string)):
        if string[i] not in string_dict:
            string_dict[string[i]] = 0
        string_dict[string[i]] += 1

        chars_processed += 1
        if chars_processed >= pattern_length:
            if string_dict == pattern_dict:
                print('Hurray!! Perms found')
                return
            string_dict[string[window_start]] -= 1
            if string_dict[string[window_start]] == 0:
                del string_dict[string[window_start]]
            window_start += 1
            chars_processed -= 1
    
    print('Not found')

def main():
    find_permutation_substring('oidbcaf','abc')
    find_permutation_substring('bcdxabcdy','bcdxabcdy')
    find_permutation_substring('aaacb','abc')
    find_permutation_substring('odicf','dc')

if __name__ == '__main__':
    main()