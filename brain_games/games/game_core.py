import prompt

from brain_games.cli import welcome_user

DIFFICULTS = {1: "EASY",
              2: "MEDIUM",
              3: "HARD"
}
EASY = {"number_of_questions": 3,
            "number_of_lives": 3
}

MEDIUM = {"number_of_questions": 5,
            "number_of_lives": 2
}

HARD = {"number_of_questions": 10,
            "number_of_lives": 1
}


def choose_difficult(difficult=1):
    match difficult:
        case 1:
            return EASY
        case 2:
            return MEDIUM
        case 3:
            return HARD


def prin_defeat_message(user_answer, right_answer, user_name):
    print(f"Let's try again, {user_name}!")


def print_congrats_message(user_name):
    print(f"Congratulations, {user_name}!")


def start_game_menu():
    user_name = welcome_user()
    print("""Now please,select difficult:
    1 - EASY(Default)
    2 - MEDIUM
    3 - HARD 
    """)
    choise = prompt.integer("Your choice: ")
    while len(str(choise)) > 1 and choise <= 3:
        choise = prompt.integer("Please write only 1 digit!: ")
    current_dificult = choose_difficult(choise)
    number_of_questions = current_dificult["number_of_questions"]
    number_of_lives = current_dificult["number_of_lives"]
    return user_name, number_of_questions, number_of_lives, choise


def start_game(game_module):
    user_name, number_of_questions, number_of_lives, current_difficult = start_game_menu()
    print(game_module.RULE)
    for _ in range(number_of_questions):
        answer, question = game_module.generate_question_and_answer(current_difficult)
        print(f'Current lives: {number_of_lives}')
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if str(answer) != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. " 
                + f"Correct answer was '{answer}'."
            )
            number_of_lives -= 1
            if number_of_lives == 0:
                prin_defeat_message(user_answer, answer, user_name)
                return
            continue
        print("Correct!")
    print_congrats_message(user_name)