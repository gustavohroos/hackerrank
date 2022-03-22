# Enter your code here. Read input from STDIN. Print output to STDOUT

def print_door(height: int, width: int) -> str:
    
    '''
    Pythonic code:
    '''
    for i in range (1, height, 2):
        print((i*".|.").center(width, "-"))
    print(("WELCOME").center(width, "-"))
    for i in range (height-2, -1, -2):
        print((i*".|.").center(width, "-"))

    '''
    My code:
        for i in range (0, int((height/2))):
            print("---"*int(height/2 - i) + ".|."*(i) + ".|." + ".|."*(i) + "---"*int(height/2 - i))
            
        print("-"*int((width-7)/2) + "WELCOME" + "-"*int((width-7)/2))
        
        for i in range (int((height/2)), 0, -1):
            print("---"*int(height/2 - (i-1)) + ".|."*(i-1) + ".|." + ".|."*(i-1) + "---"*int(height/2 - (i-1)))
    '''        
    
        
if __name__ == '__main__':
    height, width = map(int, input().split(' '))
    
    print_door(height, width)