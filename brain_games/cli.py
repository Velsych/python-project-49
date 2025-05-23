import prompt
from brain_games import user_greet


def welcome_user():
    user_greet()
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}")
    return user_name