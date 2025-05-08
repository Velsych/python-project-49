def gcd_games():
    import prompt

    from brain_games import logic

    def random_for_gcd():
        from random import randint

        numbers = []
        for _ in range(2):
            numbers.append(randint(1, 100))
        return numbers

    def gcd():
        numbers = random_for_gcd()
        i = max(numbers)
        j = min(numbers)
        while j != 0:
            c = i % j
            i, j = j, c
        return i, numbers
    
    user_name = logic.hello_username()
    print("Find the greatest common divisor of given numbers.")
    right_answers = 0
    for _ in range(3):
        answer, numbers = gcd()
        a, b = numbers
        print(f"Question {a} {b}")
        ans = prompt.integer("Your answer: ")
        if ans != answer:
            logic.defeat(ans, answer, user_name)
            break
        else:
            print("Correct!")
            right_answers += 1
    if right_answers == 3:
        logic.congrats(user_name)