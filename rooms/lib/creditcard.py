import random


def calc_checkdigit(cc_number):
    """
    Calculate the check digit.
    Based on a full 16-digit credit card number, 
    i.e. ignore last digit as this is the digit we want to calculate.
    """
    double = True
    sequence = ""
    for n in cc_number[-2::-1]:
        val = str(int(n)*2) if double else n
        double = not double
        sequence = val + sequence
    # print(sequence)

    sum = 0
    for n in sequence:
        sum += int(n)
    # print(sum)

    rest = sum % 10
    # print(rest)

    result = 0 if rest == 0 else 10 - rest
    # print(result)

    return result


def verify_number(cc_number):
    """
    Compare caluclated check digit with last digit of credit card number
    """
    return int(cc_number[-1]) == calc_checkdigit(cc_number)


def create_number():
    """
    Create valid credit card number.
    Length 16: Issuer=1, Number=14, Checksum=1
    """
    card_number = "4"  # init with issuer=Visa
    for n in range(14):
        card_number += str(random.randint(0, 9))
    card_number += str(calc_checkdigit(card_number+"0"))
    return card_number


def create_and_check():
    nr = create_number()
    print(nr, verify_number(nr))


def input_and_check():
    """
    Valid examples: 4068769099596901, 4483216143305076
    Invalid examples: 4906386927025610, 4152991234567890
    """
    cc_number = input("Kreditkartennummer prüfen: ")
    print(verify_number(cc_number))


def create_random_number():
    card_number = "4"
    for n in range(15):
        card_number += str(random.randint(0, 9))
    return card_number


if __name__ == "__main__":
    input_and_check()
