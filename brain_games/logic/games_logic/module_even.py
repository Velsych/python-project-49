def even_games():
    import prompt

    from brain_games import logic

    def even_game():
        print('Answer "yes" if the number is even, otherwise answer "no".')
        right_answers = 0
        for _ in range(2):
            number = logic.random_int()
            answer = "no"
            if number % 2 == 0 and number / number == 1:
                answer = "yes"
            print(f'Question: {number}')
            ans = prompt.string("Your answer: ")
            if answer == ans:
                right_answers += 1
                print("Correct!")
            else:
                logic.defeat(ans, answer, user_name)
                break
        if right_answers == 3:
            logic.congrats(user_name)
            
    user_name = input("May i have ur name? ")
    even_game()