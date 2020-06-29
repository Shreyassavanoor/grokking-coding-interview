def no_repeat_substring(string):
    window_start = 0
    max_length = 0
    chars_count = {}

    for i in range(len(string)):

        if string[i] not in chars_count:
            chars_count[string[i]] = 0
        chars_count[string[i]] += 1

        #if count > 1 then shring the window unti it becomes 1
        while chars_count[string[i]] > 1:
            if string[window_start] == string[i]:
                chars_count[string[i]] -= 1
            window_start += 1

        max_length = max(max_length, i - window_start + 1)
    
    print(max_length)

def main():
    no_repeat_substring("aabccbb")

if __name__ == '__main__':
    main()