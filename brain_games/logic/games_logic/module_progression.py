RULE = "What number is missing in the progression?"


def generate_question_and_answer():

    from random import choice, randint
    progression = []
    while len(progression) < 5:
        progression = [str(i) for i in range(0,
            randint(5, 50), randint(2, 5))]  # NOSONAR
    progression = progression[0:10]
    answer = choice(progression)        # NOSONAR
    progression[progression.index(answer)] = ".."
    progression = " ".join(progression)        
    return answer, progression