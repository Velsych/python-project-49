from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_GEN_NUMBER = 100
MIN_GEN_NUMBER = 1


def is_prime(number):
    if number % 2 == 0:
        return False
    elif number == 1:
         return False
    for i in range(3, number, 2):
        if number % i == 0:
                return False
    return True

def generate_question_and_answer():
    answer = "yes"
    number = randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)  # NOSONAR
    if number == 2:
        return answer, number
    answer = 'yes' if is_prime(number) else "no"

    return answer, number
        
    