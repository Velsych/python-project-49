from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'

EASY = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 50
}

MEDIUM = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 150
}

HARD = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 200
}


def generate_question_and_answer(option=1):
    match option:
        case 1:
            difficult = EASY
        case 2:
            difficult = MEDIUM
        case 3:
            difficult = HARD
    number = randint(difficult["MIN_GEN_NUMBER"], difficult["MAX_GEN_NUMBER"])  # NOSONAR
    answer = "no"
    if number % 2 == 0:
        answer = "yes"
    return answer, number