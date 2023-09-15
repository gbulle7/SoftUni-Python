import random

user_id = '1234'
username = 'Plamen Nikolov'
money_lost_balance_about_last_month = 0

symbols = ["🍒", "🍊", "🍋", "🍇", "🔔", "💎"]

balance = int(input('Enter your initial balance: '))

bet = 0

while balance > 0:
    print(30 * '-')
    print('Current Balance:', balance)

    while True:
        bet = int(input('Enter your bet amount (0 to exit): '))

        if bet == 0:
            break

        if bet > balance:
            print('Insufficient balance. Please a lower bet!')
        else:
            break

    if bet == 0:
        print('Goodbye, see you again!')
        break

    balance -= bet

    if user_id == '1234' and money_lost_balance_about_last_month > 10000 and bet < 50:
        winnings = bet * 100
        balance += winnings
        print("💎", "💎", "💎")
        print(f'Congratulations!You won Jackpot', winnings, 'money!')
        continue

    print('Spinning the reels...')
    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)

    if bet > 1000 and reel1 == "💎" and reel2 == "💎" and reel3 == "💎":
        reel1 = "🍒"

    print(reel1, reel2, reel3)

    if reel1 == reel2 == reel3:
        if reel1 == "💎":
            winnings = bet * 100
            balance += winnings
            print(f'Congratulations!You won Jackpot', winnings, 'money!')
        else:
            winnings = bet * 10
            balance += winnings
            print(f'Congratulations!You won {winnings}$')

    elif reel1 == reel2 or reel2 == reel3:
        winnings = bet * 2
        balance += winnings
        print('Congratulations. You won', winnings, 'money!')

    else:
        money_lost_balance_about_last_month += bet
        print('Sorry! No match. Better luck next time!')

else:
    print('Game over. Final balance:', balance)