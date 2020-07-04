def remove_backspace(str1, str2):
    str1 = parse_strings(str1)
    str2 = parse_strings(str2)
    print(str1 == str2)

def parse_strings(string):
    stack = []
    for i in string:
        if i != '#':
            stack.append(i)
        else:
            stack.pop()
    return ''.join(stack)

def main():
    remove_backspace('xy#z', 'xzz#')
    remove_backspace('xy#z', 'xyz#')
    remove_backspace('xp#', 'xyz##')
    remove_backspace('xywrrmp', 'xywrrmu#p')

if __name__ == '__main__':
    main()
