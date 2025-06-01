crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano (ADA)": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}


def get_info():
    for coin in crypto_db:
        print(f'\n{coin}')
        print(
            f'The price at the moment is {crypto_db[coin]['price_trend']}')
        print(f'The market cap is {crypto_db[coin]['market_cap']}')
        print(f'The use of energy is {crypto_db[coin]['energy_use']}')
        print(
            f'The sustainability score is {crypto_db[coin]['sustainability_score']}')
        print()


def best_price():
    for coin in crypto_db:
        if crypto_db[coin]['price_trend'] == 'stable':
            print(f'{coin} is one of the stable crypto coins at the moment!')


def market_cap():
    coins = []
    for coin in crypto_db:
        if crypto_db[coin]['market_cap'] == 'high':
            coins.append(coin)
    print(f'{coins} has/have the best market cap! ')


def best_energy_use():
    coin = min(crypto_db, key=lambda x: crypto_db[x]['energy_use'])
    print(f'{coin} is the best crypto saving energy!')


def get_long_term_growth():
    coin = max(
        crypto_db, key=lambda x: crypto_db[x]['sustainability_score'])
    if coin:
        print(f'{coin} is trending up and has a top-tier sustainability score!')


def get_help():
    print('0: Get info about Crypto Coins at the moment')
    print('1: Get info about the stable crypto coins in the market')
    print('2: Get info about Crypto Coins has/have the best market cap')
    print('3: Get info about the best crypto saving energy')
    print('4: Get info about the trending up & has a top-tier sustainability score!')
    print('5: Have an advice for the most profitable crypto now!')
    print('6: Know which the most sustainable crypto now!')
    print('Quit: To quit')


def profit_advice():
    for coin in crypto_db:
        if crypto_db[coin]['price_trend'] == 'rising' and crypto_db[coin]['market_cap'] == 'high':
            print(
                f'If you want to invest your money, {coin} will be a good choice!')


def sustainable_advice():
    for coin in crypto_db:
        if crypto_db[coin]['energy_use'] == 'low' and crypto_db[coin]['sustainability_score'] > 7/10:
            print(
                f'If you want the best sustainable crypto, so go for {coin}!')


print('~ Welcome to Your CryptoBuddy ~ ')
print('How can i help you today?')
print('If you need help: just type "Help"')
user_query = input('How can i help you? ').lower().strip()

while True:
    if user_query == 'help':
        get_help()

    if user_query in ['0', 'general']:
        get_info()

    if user_query in ['stable', 'least price', '1']:
        best_price()
    if user_query in ['market cap', 'cap', '2']:
        market_cap()
    if user_query in ['energy', '3']:
        best_energy_use()
    if user_query in ['long-term', 'growth', 'sustainability score', '4']:
        get_long_term_growth()

    if user_query in ['profit', '5']:
        profit_advice()
    if user_query in ['sustainable', '6']:
        sustainable_advice()

    if not user_query:
        print('Please tell me how to help you or just type "Help"')
    if user_query in ['quit', 'exit']:
        print('See you later!')
        break
    user_query = input('So what\'s your choice? ').lower().strip()
