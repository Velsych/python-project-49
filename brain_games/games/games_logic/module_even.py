from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_GEN_NUMBER = 50
MIN_GEN_NUMBER = 5


def generate_question_and_answer():

    number = randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)  # NOSONAR
    answer = "no"
    if number % 2 == 0:
        answer = "yes"
    return answer, number