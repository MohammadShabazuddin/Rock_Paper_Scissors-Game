import random

def Play():
    User = input("Seclect 'R' is Rock, 'P' is Paper, 'S' is Scissor \n").upper()

    Computer = random.choice(['R','P','S'])
    

    if User == Computer:
        return 'Match is Draw'
    elif Game(User, Computer):
        return f'Congratulations!! You Won Computer choose {Computer} and you choose {User}'
    else:
        return f'You Lost Computer choose {Computer} and you choose {User}'

def Game(U, C):
    if ( U == 'R' and C == 'S' ) or ( U == 'S' and C == 'P') or ( U == 'P' and C == 'R'):
        return True

    
    

print(Play())



