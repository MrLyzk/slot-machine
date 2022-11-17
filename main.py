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

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break

        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, sym_count in symbols.items():
        for _ in range(sym_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("How much do you want to deposit: $").strip()
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


def spin(balance):
    while True:
        lines = get_number_of_lines()
        while True:
            bet = get_bet()
            total = bet * lines
            if balance >= total:
                break
            else:
                print("Insufficient balance ($" + str(balance) + "), please bet lower amount.")
        print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total}")
        answer = input("If you want to change bet options, choose 'c', otherwise press enter to spin\n")
        if answer != "c":
            break

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings} on lines")
    print(f"You won on lines:", *winning_lines)
    return winnings - total


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        while balance <= 0:
            print(f"Your balance is ${balance}, in order to play again you need to deposit more money")
            answer = input("Press 'a' to add funds (q to quit)\n")
            if answer == "q":
                break
            elif answer == "a":
                balance += deposit()
        else:
            answer = input("Press enter to play (q to quit or a to add funds). ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
