def even_games():
    from random import randint

    import prompt

    def right_answer():
        random_number = randint(1, 100)
        answer = "no"
        if random_number % 2 == 0 and random_number % random_number == 0:
            answer = "yes"
        return random_number, answer

    def even_game():
        print('Answer "yes" if the number is even, otherwise answer "no".')
        right_answers = 0
        while right_answers < 3:
            number, answer = right_answer()
            print(f'Question: {number}')
            ans = prompt.string("Your answer: ")
            if answer == ans:
                right_answers += 1
                print("Correct!")
            else:
                print(f"'{ans}' is wrong answer ;(. Correct answer was '{answer}'.")
                print(f'Let`s try again, {user_name}')
                break
        if right_answers == 3:
            print(f"Congratulations, {user_name}")
            
    user_name = input("May i have ur name? ")
    even_game()