from brain_games import welcome_user
import prompt


def defeat_message(user_answer, right_answer, user_name):
    print(
        f"'{user_answer}' is wrong answer ;(. " 
        + f"Correct answer was '{right_answer}'."
    )
    print(f"Let's try again, {user_name}!")


def congrats_message(user_name):
    print(f"Congratulations, {user_name}!")


def full_user_greet():
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def game_start(game_module):
    user_name = welcome_user()
    print(game_module.RULE)
    for _ in range(3):
        answer, question = game_module.generate_question_and_answer()
        print(f'Question: {question}')
        if type(answer) is str:
            user_answer = prompt.string("Your answer: ")
        else:
            user_answer = prompt.integer("Your answer: ")
        if answer != user_answer:
            defeat_message(user_answer, answer, user_name)
            return
        print("Correct!")
    congrats_message(user_name)