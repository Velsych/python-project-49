import prompt


def welcome_user():
    user_name = prompt.string("May i have ur name? ")
    print(f"Hello, {user_name}")
    return user_name