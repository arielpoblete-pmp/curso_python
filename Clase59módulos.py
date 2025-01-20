def calculate_balance(income,expenses):
    balance = income - expenses
    if balance < 0:
        return f'El balance es $ {balance} -> {False}'
    else:
        return f'El balance es $ {balance} -> {True}'

from reports import calculate_balance

balance = calculate_balance(400,100)
print(balance)

balance_2 = calculate_balance(100,600)
print(balance_2)

```El balance es $ 300 -> True

El balance es $ -500 -> False