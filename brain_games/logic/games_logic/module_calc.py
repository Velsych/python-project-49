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
    right_answers = 0
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
        ans = prompt.integer("Your answer: ")
        if ans != answer:
            logic.defeat(ans, answer, user_name)
            break
        right_answers += 1
    if right_answers == 3:
        logic.congrats(user_name)