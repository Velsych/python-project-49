import prompt

from brain_games.cli import welcome_user

NUMBER_OF_QUESTIONS = 3


def prin_defeat_message(user_answer, right_answer, user_name):
    print(
        f"'{user_answer}' is wrong answer ;(. " 
        + f"Correct answer was '{right_answer}'."
    )
    print(f"Let's try again, {user_name}!")


def print_congrats_message(user_name):
    print(f"Congratulations, {user_name}!")


def start_game(game_module):
    user_name = welcome_user()
    print(game_module.RULE)
    for _ in range(NUMBER_OF_QUESTIONS):
        answer, question = game_module.generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if str(answer) != user_answer:
            prin_defeat_message(user_answer, answer, user_name)
            return
        print("Correct!")
    print_congrats_message(user_name)