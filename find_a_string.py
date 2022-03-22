def count_substring(string, sub_string):
    count = 0
    size = len(sub_string)

    for i in range(0, len(string)):
        if string.find(str(sub_string), i, i+size) != -1:
            count += 1
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)