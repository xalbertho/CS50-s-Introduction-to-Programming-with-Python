def main():
    s = input('Plate: ')
    if is_valid(s):
        print('Valid')
    else:
        print('Invalid')


def is_valid(s):
    if (len(s) < 2 or len(s) > 6):
        return False

    if not s.isalnum():
        return False

    # Empiece con 2 letras
    if not s[:2].isalpha():
        return False

    seen_digit = False

    for ch in s:
        if ch.isdigit():
            # Si es el primer número, no puede ser 0
            if not seen_digit and ch == "0":
                return False
            seen_digit = True
        else:
            # Si ya apareció un número, ya no pueden venir letras después
            if seen_digit:
                return False

    return True


if __name__ == "__main__":
    main()
