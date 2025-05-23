from random import choice, randint

RULE = "What is the result of the expression?"
OPERATIONS = ("*", "+", "-")
MAX_GEN_NUMBER = 50
MIN_GEN_NUMBER = 5


def calculate(number1, number2, operation):
    match operation:
        case "*":
            answer = number1 * number2
        case "+":
            answer = number1 + number2
        case "-":
            answer = number1 - number2
    return answer


def generate_question_and_answer():
    
    number1 = randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)  # NOSONAR
    number2 = randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)  # NOSONAR
    operation = choice(OPERATIONS)  # NOSONAR
    answer = calculate(number1, number2, operation)
    question = f'{number1} {operation} {number2}'
    return answer, question
