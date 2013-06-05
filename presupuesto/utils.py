from os import environ


__all__ = ['get_balance', 'reorder_iterable']


def get_balance():
    if "PRESUPUESTO_BALANCE" in environ:
        balance_raw = environ['PRESUPUESTO_BALANCE']
    else:
        try:
            with open("BALANCE.txt") as balance_file:
                balance_raw = balance_file.read()
        except:
            return float(0)

    balance = float(balance_raw)
    return balance


def reorder_iterable(iterable, new_start):
    first_half = iterable[:new_start]
    last_half = iterable[new_start:]
    return last_half + first_half
