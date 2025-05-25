from random import randint

RULE = "What number is missing in the progression?"
EASY = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 50,
        "MAX_STEP_NUMBER": 5,
        "MIN_STEP_NUMBER": 1,
        "MIN_PROGRESSION_LENGTH": 0,
        "MAX_PROGRESSION_LENGTH": 10
}

MEDIUM = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 100,
        "MAX_STEP_NUMBER": 10,
        "MIN_STEP_NUMBER": 1,
        "MIN_PROGRESSION_LENGTH": 0,
        "MAX_PROGRESSION_LENGTH": 15
}

HARD = {"MIN_GEN_NUMBER": 0,
        "MAX_GEN_NUMBER": 150,
        "MAX_STEP_NUMBER": 15,
        "MIN_STEP_NUMBER": 1,
        "MIN_PROGRESSION_LENGTH": 0,
        "MAX_PROGRESSION_LENGTH": 20
}

def generate_question_and_answer(option = 1):
    match option:
        case 1:
            difficult = EASY
        case 2:
            difficult = MEDIUM
        case 3:
            difficult = HARD
    progression = []
    progression_start = randint(difficult["MIN_GEN_NUMBER"], difficult["MAX_GEN_NUMBER"])  # NOSONAR
    progression.append(progression_start)
    progression_step = randint(difficult["MIN_STEP_NUMBER"], difficult["MAX_STEP_NUMBER"])  # NOSONAR
    progression_missing = randint(difficult["MIN_PROGRESSION_LENGTH"],   # NOSONAR
     difficult["MAX_PROGRESSION_LENGTH"] - 1  # NOSONAR
     )

    for _ in range(difficult["MAX_PROGRESSION_LENGTH"] - 1):
        progression.append(progression[-1] + progression_step)

    answer = progression[progression_missing]
    progression[progression_missing] = ".."
    question = [str(number) for number in progression]       
    return answer, " ".join(question)