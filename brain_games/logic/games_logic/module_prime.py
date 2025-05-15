RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer():
    from random import randint
    answer = "yes"
    number = randint(1, 100) #NOSONAR
    match number:
        case 1:
            answer = "no"
            return answer
        case 2:
            return answer
    if number % 2 == 0:
        answer = "no"
    else:
        for i in range(3, number, 2):
            if number % i == 0:
                answer = "no"
                return answer,number
    return answer, number
        
    