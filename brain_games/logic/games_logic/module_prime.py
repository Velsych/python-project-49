def prime_games():
    import prompt

    from brain_games import logic

    def is_prime(num):
        answer = "yes"
        if num % 2 == 0:
            answer = "no"
        else:
            for i in range(3, num, 2):
                if num % i == 0:
                    answer = "no"
        return answer

    user_name = logic.hello_username()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    
    right_answer = 0
    for _ in range(3):
        number = logic.random_int()
        print(f'Question: {number}')
        ans = prompt.string("Your answer: ")
        answer = is_prime(number)
        if ans != answer:
            logic.defeat(ans, answer, user_name)
            break
        right_answer += 1
    if right_answer == 3:
        logic.congrats(user_name)  # god witness i make this very sleepy 
        
    