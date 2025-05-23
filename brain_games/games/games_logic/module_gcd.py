from random import randint

RULE = "Find the greatest common divisor of given numbers."
MAX_GEN_NUMBER = 50
MIN_GEN_NUMBER = 1


def find_gcd(number1, number2):
    max_number = max(number1, number2)
    min_number = min(number1, number2)
    while min_number != 0:
        rest = max_number % min_number
        max_number, min_number = min_number, rest
    return max_number


def generate_question_and_answer():

    number1 = randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)  # NOSONAR
    number2 = randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)  # NOSONAR
    answer = find_gcd(number1, number2)
    question = f"{number1} {number2}"
    return answer, question
