from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
EASY = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 50
}

MEDIUM = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 150
}

HARD = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 200
}

def is_prime(number):
    if number % 2 == 0:
        return False
    elif number == 1:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer(option = 1):
    match option:
        case 1:
            difficult = EASY
        case 2:
            difficult = MEDIUM
        case 3:
            difficult = HARD
    answer = "yes"
    number = randint(difficult["MIN_GEN_NUMBER"], difficult["MAX_GEN_NUMBER"])  # NOSONAR
    if number == 2:
        return answer, number
    answer = 'yes' if is_prime(number) else "no"

    return answer, number
        
    