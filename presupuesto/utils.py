from os import environ


__all__ = ['get_balance', 'reorder_iterable']


def get_balance():
    balance_file_path = environ.get("PRESUPUESTO_BALANCE_FILE", "BALANCE.txt")
    
    with open(balance_file_path) as balance_file:
        balance_raw = balance_file.read()
    
    balance = float(balance_raw)
    return balance


def reorder_iterable(iterable, new_start):
    first_half = iterable[:new_start]
    last_half = iterable[new_start:]
    return last_half + first_half
