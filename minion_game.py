def minion_game(string):
    scores = [['Stuart', 0], ['Kevin', 0]]
    vowels = 'A', 'E', 'I', 'O', 'U'
    
    for i in range(len(string)):
        if string[i] in vowels:
            scores[1][1] += (len(string)-i)
        else:
            scores[0][1] += (len(string)-i)

    if scores[0][1] > scores[1][1]:
        print(scores[0][0] + ' ' + str(scores[0][1]))
    elif scores[1][1] > scores[0][1]:
        print(scores[1][0] + ' ' + str(scores[1][1]))
    else:
        print("Draw")
        
    
            

if __name__ == '__main__':
    s = input()
    minion_game(s)