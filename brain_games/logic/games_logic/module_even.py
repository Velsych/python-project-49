def even_games():
    import prompt

    from brain_games import logic

    def even_game():
        print('Answer "yes" if the number is even, otherwise answer "no".')
        no_mistakes = True
        for _ in range(3):
            number = logic.random_int()
            answer = "no"
            if number % 2 == 0:
                answer = "yes"
            print(f'Question: {number}')
            user_answer = prompt.string("Your answer: ")
            if user_answer != answer:
                logic.defeat(user_answer, answer, user_name)
                no_mistakes = False
                break
            else:
                print("Correct!")
        if no_mistakes:
            logic.congrats(user_name)
            
    user_name = logic.hello_username()
    even_game()