MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than $0.")
        else:
            print("Please enter an amount.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to bet on(1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid amount of lines.")
        else:
            print("Please enter an amount.")

    return lines

def get_bet():
    while True:
        lines = input("What amount would you like to bet on each line (1" + str(MAX_BET) + ")? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet *lines
print("You are betting ${bet} on {lines} lines. Total bet is equal to: ${}")



main()
