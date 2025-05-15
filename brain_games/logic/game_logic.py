def defeat(user_answer, right_answer, user_name):
    print(
        f"'{user_answer}' is wrong answer ;(. " 
        + f"Correct answer was '{right_answer}'."
    )
    print(f"Let's try again, {user_name}!")


def congrats(user_name):
    print(f"Congratulations, {user_name}!")


def hello_username():
    import prompt
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def game_start(game_module):
    import prompt
    user_name = hello_username()
    print(game_module.RULE)
    for _ in range(3):
        answer, question = game_module.generate_question_and_answer()
        print(f'Question: {question}')
        if type(answer) is str:
            user_answer = prompt.string("Your answer: ")
        else:
            user_answer = prompt.integer("Your answer: ")
        if answer != user_answer:
            defeat(user_answer, answer, user_name)
            return
        print("Correct!")
    congrats(user_name)