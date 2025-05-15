RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():

    from random import randint

    number = randint(1, 100)  # NOSONAR
    answer = "no"
    if number % 2 == 0:
        answer = "yes"
    return answer, number