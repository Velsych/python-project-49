from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_GEN_NUMBER = 100
MIN_GEN_NUMBER = 1


def check_prime(number):
    flag = True
    if number % 2 == 0:
        flag = False
    else:
        for i in range(3, number, 2):
            if number % i == 0:
                flag = False
    return flag


def generate_question_and_answer():
    answer = "yes"
    number = randint(MIN_GEN_NUMBER, MAX_GEN_NUMBER)  # NOSONAR
    match number:
        case 1:
            answer = "no"
            return answer, number
        case 2:
            return answer, number
    check = check_prime(number)
    if check is False:
        answer = "no"
    return answer, number
        
    