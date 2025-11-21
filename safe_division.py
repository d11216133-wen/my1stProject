def safe_division(a, b):
    """
    Safely divide a by b, and avoid ZeroDivisionError.
    Returns:
        a / b if b != 0, otherwise returns None.
    """
    if b == 0:
        return None
    return a / b
