import collections
def find_substring(string, pattern):
    window_start = 0
    pattern_dict = collections.Counter(pattern)
    string_dict = {}

    for window_end in range(len(string)):

        if string[window_end] in pattern_dict:
            if string[window_end] not in string_dict:
                string_dict[string[window_end]] = 0
            string_dict[string[window_end]] += 1


        while  len(string_dict) == len(pattern_dict):
            if string_dict == pattern_dict:
                print(string[window_start : window_end + 1])
                return

            if string[window_start] in string_dict:
                string_dict[string[window_start]] -= 1
                if string_dict[string[window_start]] == 0:
                    string_dict[string[window_start]] += 1
            window_start += 1

    print("")

def main():
    find_substring('aabdec', 'abc')
    find_substring('abdabca', 'abc')
    find_substring('adcad', 'abc')

if __name__ == '__main__':
    main()