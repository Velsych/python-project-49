def progression_games():
    import prompt

    from brain_games import logic

    def random_progression():
        from random import choice, randint
        progression = []
        while len(progression) < 5:
            progression = [str(i) for i in range(0,
             randint(5, 50), randint(2, 5))]  # NOSONAR
        progression = progression[0:10]
        answer = choice(progression)        # NOSONAR
        progression[progression.index(answer)] = ".."
        progression = " ".join(progression)        
        return progression, int(answer)
    
    user_name = logic.hello_username()
    print("What number is missing in the progression?")
    no_mistakes = True
    for _ in range(3):
        prog, answer = random_progression()
        print(f'Question: {prog}')
        user_answer = prompt.integer("Your answer: ")
        if user_answer != answer:
            logic.defeat(user_answer, answer, user_name)
            no_mistakes = False
            break
        else:
            print("Correct!")
    if no_mistakes:
        logic.congrats(user_name)