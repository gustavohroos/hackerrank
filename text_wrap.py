def wrap(string, max_width):
    words = []
    for i in range(0, len(string), max_width):
        words.append(string[i:i+max_width])
    return "\n".join(str(p) for p in words)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)