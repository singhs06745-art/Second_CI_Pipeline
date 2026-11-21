def is_armstrong(number):
    if number < 0:
        return False

    digits = str(number)
    power = len(digits)

    total = sum(int(digit) ** power for digit in digits)

    return total == number