from random import choice, randint

RULE = "What is the result of the expression?"
OPERATIONS = ("*", "+", "-")
EASY = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 50
}

MEDIUM = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 150
}

HARD = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 200
}


def calculate(number1, number2, operation):
    match operation:
        case "*":
            answer = number1 * number2
        case "+":
            answer = number1 + number2
        case "-":
            answer = number1 - number2
    return answer


def generate_question_and_answer(option=1):
    match option:
        case 1:
            difficult = EASY
        case 2:
            difficult = MEDIUM
        case 3:
            difficult = HARD
    
    number1 = randint(difficult["MIN_GEN_NUMBER"], difficult["MAX_GEN_NUMBER"])  # NOSONAR
    number2 = randint(difficult["MIN_GEN_NUMBER"], difficult["MAX_GEN_NUMBER"])  # NOSONAR
    operation = choice(OPERATIONS)  # NOSONAR
    answer = calculate(number1, number2, operation)
    question = f'{number1} {operation} {number2}'
    return answer, question
