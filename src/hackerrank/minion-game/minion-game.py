def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']

    p1 = 0
    p2 = 0

    # gets the string length
    string_length = len(string)

    # for each i in the length of the string
    for i in range(string_length):
        # if the string char is a vowel, then count to p1
        if s[i] in vowels:
            p1 += (string_length) - i
        # if not, count to p2
        else:
            p2 += (string_length) - i

    if (p1 > p2):
        print(f'Kevin {p1}')
    elif (p2 > p1):
        print(f'Stuart {p2}')
    elif (p2 == p1):
        print("Draw")


s = input("Input the word.")
minion_game(s)
