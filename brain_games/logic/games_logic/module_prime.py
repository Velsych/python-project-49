def prime_games():
    import prompt

    from brain_games import logic

    def is_prime(num):
        answer = "yes"
        match num:
            case 1:
                answer = "no"
                return answer
            case 2:
                return answer
        if num % 2 == 0:
            answer = "no"
        else:
            for i in range(3, num, 2):
                if num % i == 0:
                    answer = "no"
                    return answer
        return answer

    user_name = logic.hello_username()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    no_mistakes = True
    for _ in range(3):
        number = logic.random_int()
        print(f'Question: {number}')
        user_answer = prompt.string("Your answer: ")
        answer = is_prime(number)
        if user_answer != answer:
            logic.defeat(user_answer, answer, user_name)
            no_mistakes = False
            break
        else: 
            print("Correct!")
    if no_mistakes:
        logic.congrats(user_name)  # god witness i make this very sleepy 
        
    