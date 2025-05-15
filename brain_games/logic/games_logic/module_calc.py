RULE = "What is the result of the expression?"


def generate_question_and_answer():
    from random import choice, randint, shuffle

    def random_modifier():
        modifiers = ["*", "+", "-"]
        shuffle(modifiers)
        return choice(modifiers)
    
    a, b = randint(1, 50), randint(1, 50)
    c = random_modifier()
    match c:
        case "*":
            answer = a * b
        case "+":
            answer = a + b
        case "-":
            answer = a - b
    question = f'{a} {c} {b}'
    return answer, question
