def tuple_name(n: int):
    '''
    Return the name for an n-tuple of size n.
    For values outside [1,10], defaults to n-fold.
    '''
    
    if 1 <= n <= 10:
        return [
            "Single",
            "Double",
            "Triple",
            "Quadruple",
            "Quintuple",
            "Sextuple",
            "Septuple",
            "Octuple",
            "Nonuple",
            "Dectuple"
        ][n-1]
    else:
        return f"{n}-fold"
