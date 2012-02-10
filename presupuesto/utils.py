

def reorder_iterable(iterable, new_start):
    first_half = iterable[:new_start]
    last_half = iterable[new_start:]
    return last_half + first_half
