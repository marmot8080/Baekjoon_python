def is_invalid(p):
    if p=='0' or p=='2' or p=='5': 
        return False
    else:
        return True

def play_RSP(p1, p2):
    is_p1_invalid = is_invalid(p1)
    is_p2_invalid = is_invalid(p2)

    if p1 == p2:
        return '='

    if is_p1_invalid and is_p2_invalid:
        return '='
    elif is_p1_invalid:
        return '<'
    elif is_p2_invalid:
        return '>'

    if p1 == '0':
        if p2 == '2':
            return '>'
        else:
            return '<'
    elif p1 == '2':
        if p2 == '5':
            return '>'
        else:
            return '<'
    else:
        if p2 == '0':
            return '>'
        else:
            return '<'

if __name__ == '__main__':
    player1, player2 = input().split()
    print(play_RSP(player1, player2))