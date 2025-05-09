def random_int():
    from random import randint
    random_number = randint(1, 101)
    return random_number


def defeat(user_answer, right_answer, user_name):
    print(f"""'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.""")
    print(f'Let`s try again, {user_name}!')


def congrats(user_name):
    print(f"Congratulations, {user_name}!")


def hello_username():
    import prompt
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name