def longest_substring_k_distinct_chars(string, k):
    distinct_chars = {}
    window_start = 0
    longest_substring_len = 0
    for i in range(len(string)):
        if string[i] not in distinct_chars:
            distinct_chars[string[i]] = 0
        distinct_chars[string[i]] += 1

        while len(distinct_chars) > k:
            distinct_chars[string[window_start]] -= 1
            if distinct_chars[string[window_start]] == 0:
                del distinct_chars[string[window_start]]
            window_start += 1

        longest_substring_len = max(longest_substring_len, i - window_start + 1)

    print(longest_substring_len)

def main():
    longest_substring_k_distinct_chars('araaci', 2)
    longest_substring_k_distinct_chars('araaci', 1)
    longest_substring_k_distinct_chars('cbbebi', 3)


if __name__ == '__main__':
    main()