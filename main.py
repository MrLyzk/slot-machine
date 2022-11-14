import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, sym_count in symbols.items():
        for _ in range(sym_count):
            all_symbols.append(symbol)

    columns = [[], [], []]
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append()

        columns.append(column)

    return columns


def deposit():
    while True:
        amount = input("How much do you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                balance = amount
                break
            else:
                print("The deposit must be greater than $0")
        else:
            print("Please insert a whole number.")
    return balance
            

def get_number_of_lines():
    while True:
        amount = input(f"How many lines (1 - {MAX_LINES}) do you want to bet on? ")
        if amount.isdigit():
            amount = int(amount)
            if 1 <= amount <= MAX_LINES:
                lines = int(amount)
                break
            else:
                print("Please insert a correct number of lines.")
        else:
            print("Insert a correct number")
    return lines


def get_bet():
    while True:
        amount = input(f"How much do you want to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if 1 <= amount <= MAX_BET:
                bet = int(amount)
                break
            else:
                print(f"A bet must be between {MIN_BET} - and {MAX_BET}.")
        else:
            print("Insert a whole number")
    return bet


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total = bet * lines
        if balance >= total:
            break
        else:
            print("Insufficient balance ($" + str(balance) + "), please bet lower amount.")
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total}")


main()
