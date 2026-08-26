import random
import time
symbols = ['🍒', '🍋', '🍇']
balance = 100
ans = 0
print('Welcome to slot machine!🎰')
while balance > 0:
    print(f'Your balance is {balance} dollars')
    sym1 = symbols[random.randint(0, len(symbols)-1)]
    sym2 = symbols[random.randint(0, len(symbols)-1)]
    sym3 = symbols[random.randint(0, len(symbols)-1)]
    bet = input('Your bet? ')
    if int(bet) > balance:
        print('You don\'t have that much money, idiot')
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
        print(sym3, end = ' ')
        time.sleep(1)
        print('\n','-------------------------')
        balance -= int(bet)
        if sym1 == sym2 and sym1 == sym3:
            print('JACKPOT🤩')
            print('balance increased by bet')
            balance += int(bet) * 2
        if balance == 0:
            print('no money left, you are now a beggar💀')
            print('by how much do you want to increase your balance?')
            ans = int(input())
            balance += ans
            print('\n','-------------------------')