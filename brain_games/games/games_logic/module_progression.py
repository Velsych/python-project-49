from random import randint

MAX_GEN_NUMBER = 25
MIN_GEN_NUMBER = 0
MAX_PROGRESSION_LENGTH = 10
RULE = "What number is missing in the progression?"


def generate_question_and_answer():

    progression = []
    progression_start = randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)  # NOSONAR
    progression.append(progression_start)
    progression_step = randint(1, 5)  # NOSONAR
    progression_missing = randint(0, MAX_PROGRESSION_LENGTH - 1)  # NOSONAR

    for _ in range(MAX_PROGRESSION_LENGTH - 1):
        progression.append(progression[-1] + progression_step)

    answer = progression[progression_missing]
    progression[progression_missing] = ".."
    question = [str(number) for number in progression]       
    return answer, " ".join(question)