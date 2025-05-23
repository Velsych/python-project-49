import prompt

from brain_games.cli import welcome_user


def defeat_message(user_answer, right_answer, user_name):
    print(
        f"'{user_answer}' is wrong answer ;(. " 
        + f"Correct answer was '{right_answer}'."
    )
    print(f"Let's try again, {user_name}!")


def congrats_message(user_name):
    print(f"Congratulations, {user_name}!")


def user_welcome():
    print("Welcome to the brain games!")
    user_name = welcome_user()
    return user_name  # я сделал это что бы не ломать тесты


def game_start(game_module):
    user_name = user_welcome()
    print(game_module.RULE)
    for _ in range(3):
        answer, question = game_module.generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if str(answer) != user_answer:
            defeat_message(user_answer, answer, user_name)
            return
        print("Correct!")
    congrats_message(user_name)