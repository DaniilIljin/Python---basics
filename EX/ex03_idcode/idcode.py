"""EX03 - ID-code."""


def find_id_code(text: str):
    """description here."""
    id = ""
    count = 0
    for i in text:
        if i.isdigit():
            id += i
            count += 1
    if count > 11:
        return "Too many numbers!"
    elif count < 11:
        return "Not enough numbers!"
    else:
        return id

