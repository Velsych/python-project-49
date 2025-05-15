RULE = "Find the greatest common divisor of given numbers."


def generate_question_and_answer():

    def random_for_gcd():
        from random import randint

        numbers = []
        for _ in range(2):
            numbers.append(randint(1, 25))  # NOSONAR
        return numbers

    def gcd(numbers):
        i = max(numbers)
        j = min(numbers)
        while j != 0:
            c = i % j
            i, j = j, c
        return i
    final = []
    numbers = random_for_gcd()
    answer = gcd(numbers)
    for i in numbers:
        final.append(str(i))
    final = " ".join(final)
    return answer, final
