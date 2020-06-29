import collections
def find_anagrams_index(string, pattern):
    window_start = 0
    chars_processed = 0
    pattern_dic = collections.Counter(pattern)
    chars_count = {}
    result = []

    for window_end in range(len(string)):

        if string[window_end] not in chars_count:
            chars_count[string[window_end]] = 0
        chars_count[string[window_end]] += 1

        chars_processed += 1

        if chars_processed >= len(pattern):
            if chars_count == pattern_dic:
                result.append(window_start)
            chars_count[string[window_start]] -= 1
            if chars_count[string[window_start]] == 0:
                del chars_count[string[window_start]]
            window_start += 1
            chars_processed -= 1

    print(result)

def main():
    find_anagrams_index('ppqp', 'pq')
    find_anagrams_index('abbcabc', 'abc')

if __name__ == '__main__':
    main()

