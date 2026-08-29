import random
import time
symbols = ['🍒', '🍋', '🍇']
game = 1
ans = 0
balance = 100
story = []
ans = 0
print('Welcome to slot machine!🎰')
while balance > 0:
    story.append(f'Game {game}')
    print(f'Your balance is {balance} dollars')
    sym1 = symbols[random.randint(0, len(symbols)-1)]
    sym2 = symbols[random.randint(0, len(symbols)-1)]
    sym3 = symbols[random.randint(0, len(symbols)-1)]
    story.append(f'your balance is {balance}')
    bet = input('Your bet? ')
    story.append(f'your bet is {bet}')
    if int(bet) > balance:
        print('You don\'t have that much money💵')
        print('--------------------------')
        continue
    if bet == '67':
        print('SIX SEVEN!!!')
        time.sleep(0.5)
    if str(bet).isdigit():
        print(sym1, end = ' ')
        time.sleep(0.75)
        print(sym2, end = ' ')
        time.sleep(0.75)
        print(sym3)
        time.sleep(1)
        
    
        
        print('-------------------------')
        balance -= int(bet)
            
        story.append(f'you lose {bet}')
        if sym1 == sym2 and sym1 == sym3:
            print('JACKPOT🤩')
            print('balance increased by bet')
            story.append(f'balance increased by {bet}')
            balance += int(bet) * 2
            story.append(f'your balance is {balance}')
        if balance == 0:
            game += 1
            print('No money left, you are now a beggar💀')
            story.append('you lost all of your money')
            print('type 1 if you want to watch your story')
            print('type 2 if you want to increase your balance')
            ans = int(input())
            print('\n')
            if ans == 1:
                for i in range(0, len(story)):
                    print(story[i], end = '\n')
                    print('------------------')
                print('By how much do you want to increase your balance?')
                balance += int(input())
            elif ans == 2:
                print('By how much do you want to increase your balance?')
                balance += int(input())
            print('--------------')
