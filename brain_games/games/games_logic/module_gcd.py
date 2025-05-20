from random import randint

RULE = "Find the greatest common divisor of given numbers."
MAX_GEN_NUMBERS = (25, 50)
MIN_GEN_NUMBERS = (1, 25)


def gcd_finder(numbers):
    number1 = numbers[0]
    number2 = numbers[1]
    while number2 != 0:
        rest = number1 % number2
        number1, number2 = number2, rest
    return number1


def generate_question_and_answer():

    final_string = []
    numbers = []
    numbers.append(randint(MAX_GEN_NUMBERS[0], MAX_GEN_NUMBERS[1]))  # NOSONAR
    numbers.append(randint(MIN_GEN_NUMBERS[0], MIN_GEN_NUMBERS[1]))  # NOSONAR
    answer = gcd_finder(numbers)
    for i in numbers:
        final_string.append(str(i))
    final_string = " ".join(final_string)
    return answer, final_string
