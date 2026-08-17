import random
import time
symbols = ['🍒', '🍋', '🍇']
balance = 100
print('Добро пожаловать в деп машинку!🎰')
while balance > 0:
    print(f'Ваш баланс равен {balance} тенге')
    sym1 = symbols[random.randint(0, len(symbols)-1)]
    sym2 = symbols[random.randint(0, len(symbols)-1)]
    sym3 = symbols[random.randint(0, len(symbols)-1)]
    bet = input('Ваша ставка? ')
    if int(bet) > balance:
        print('у тебя столько нет, дебил')
        print('--------------------------')
        continue
    if bet == '67':
        print('СИКС СЕВЕН!!!')
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
            print('ДЖЕКПОТ🤩')
            print('баланс увеличен на ставку')
            balance += int(bet) * 2
print('денег нет, ты теперь бомж💀')