# V2 do sistema bancario com funcoes de deposito, saque e extrato
# author: Miguel Oliveira
def menu():
    menu = """
    CLI BANK SYSTEM v2
    [1] Deposit
    [2] Withdrawal
    [3] Bank Statement
    [4] New User
    [5] New Account
    [6] Accounts
    [0] Quit
    => """
    return int(input(menu))

def deposit(balance, amount, statement, /):
    if amount > 0:
        balance += amount
        statement += f"Deposit: $ {amount:.2f}\n"
        print("Desposit was sucessful")
    else:
        print("Operation failed! Not a valid input")

    return balance, statement

def withdrawal(*, balance, amount, statement, limit, number_withdrawals, withdrawal_limit):
    exceeded_balance = amount > balance
    exceeded_limit = amount > limit
    exceeded_withdrawal = number_withdrawals >= withdrawal_limit

    if exceeded_balance:
        print("Operation failed! You don't have enough balance.")

    elif exceeded_limit:
        print("Operation failed! Limit exceeded.")

    elif exceeded_withdrawal:
        print("Operation failed! Maximum number of withdrawals exceed.")

    elif amount > 0:
        balance -= amount
        statement += f"Withdrawal: $ {amount:.2f}"
        withdrawal_limit += 1
        print("Withdrawal successful!")

    else:
        print("Operation failed! Invalid input.")

    return balance, statement

def print_statement(balance, /, *, statement):
    print("\n=== BANK STATEMENT ===")
    print("There wasn't any operation." if not statement else statement)
    print(f"\nBalance: $ {balance:.2f}")
    print("=================")

def create_user(users):
    id_number = input("Enter your ID number: ")
    user = filter_user(id_number, users)

    if user:
        print("This ID has been registered!")
        return

    name = input("Enter your name: ")
    birth_date = input("Enter your Birth Date (dd-mm-aaaa): ")
    address = input("Enter your address: ")

    users.append({"name": name, "birth_date": birth_date, "id_number": id_number, "address": address})

    print("User created successfully")

def filter_user(id_number, users):
    filtered_users = [user for user in users if user["id_number"] == id_number]
    return filtered_users[0] if filtered_users else None

def create_account(agency, account_number, users):
    id_number = input("Enter user ID: ")
    user = filter_user(id_number, users)

    if user:
        print("Account created successfully!")
        return {"agency": agency, "account_number": account_number, "user": user}

    print("User not found! Ending operation!")

def print_accounts(accounts):
    for account in accounts:
        line = f"""\
                Agency: {account['agency']}
                CC: {account['account_number']}
                Holder: {account['user']['name']}
        """
        print("=" * 6)
        print(line)


def main():
    WITHDRAWAL_LIMIT = 3
    AGENCY = "0001"

    balance = 0
    limit = 5000
    statement = ""
    number_withdrawals = 0
    users = []
    accounts = []

    while True:
        option = menu()

        if option == 1:
            account_number = int(input("Enter account number: "))
            if account_number in accounts:

                amount = float(input("Enter amount to deposit: "))
                balance, statement = deposit(balance, amount, statement)

            else:
                print("This account doesn't exist!")

        elif option == 2:
            account_number = int(input("Enter account number: "))

            if account_number in accounts:
                amount = float(input("Enter withdrawal amount: "))

                balance, statement = withdrawal(
                        balance=balance,
                        amount=amount,
                        statement=statement,
                        limit=limit,
                        number_withdrawals=number_withdrawals,
                        withdrawal_limit=WITHDRAWAL_LIMIT
                )
            else:
                print("Operation failed! Enter the correct account number.")

        elif option == 3:
            print_statement(balance, statement=statement)

        elif option == 4:
            create_user(users)

        elif option == 5:
            account_number = len(accounts) + 1
            account = create_account(AGENCY, account_number, users)

            if account:
                accounts.append(account)

        elif option == 6:
            print_accounts(accounts)

        elif option == 0:
            break

        else:
            print("Invalid Operation!!!")

main()
