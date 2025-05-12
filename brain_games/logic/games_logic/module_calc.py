def calc_games():
    from random import choice, shuffle

    import prompt

    from brain_games import logic

    def random_modifier():
        modifiers = ["*", "+", "-"]
        shuffle(modifiers)
        return choice(modifiers)
    
    user_name = logic.hello_username()
    print("What is the result of the expression?")
    no_mistakes = True
    for _ in range(3):
        a, b = logic.random_int(), logic.random_int()
        c = random_modifier()
        match c:
            case "*":
                answer = a * b
            case "+":
                answer = a + b
            case "-":
                answer = a - b
        print(f'Question: {a} {c} {b}')
        user_answer = prompt.integer("Your answer: ")
        if user_answer != answer:
            logic.defeat(user_answer, answer, user_name)
            no_mistakes = False
            break
        else:
            print("Correct!")
    if no_mistakes:
        logic.congrats(user_name)