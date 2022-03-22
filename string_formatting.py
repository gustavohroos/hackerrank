def print_formatted(number):
    # your code goes here
    values = []
    width = 0
    for i in range(1, number+1):
        s1 = str(i)
        s2 = str(oct(i))[2:]
        s3 = (str(hex(i))[2:]).upper()
        s4 = str(bin(i))[2:]
        a = [s1, s2, s3, s4]
        values.append(a)
        width = max(width, len(a[3]))
    
    for i in range(number):
        for j in range(4):
            print(values[i][j].rjust(width, " "), end = ' ')
        print()
    
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)