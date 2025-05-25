from random import randint

RULE = "Find the greatest common divisor of given numbers."
EASY = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 50
}

MEDIUM = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 150
}

HARD = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 200
}

def find_gcd(number1, number2):
    max_number = max(number1, number2)
    min_number = min(number1, number2)
    while min_number != 0:
        rest = max_number % min_number
        max_number, min_number = min_number, rest
    return max_number


def generate_question_and_answer(option = 1):
    match option:
        case 1:
            difficult = EASY
        case 2:
            difficult = MEDIUM
        case 3:
            difficult = HARD
    
    number1 = randint(difficult["MIN_GEN_NUMBER"], difficult["MAX_GEN_NUMBER"])  # NOSONAR
    number2 = randint(difficult["MIN_GEN_NUMBER"], difficult["MAX_GEN_NUMBER"])  # NOSONAR
    answer = find_gcd(number1, number2)
    question = f"{number1} {number2}"
    return answer, question
