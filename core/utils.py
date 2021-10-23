import random


def randomNumber(N):
    min = pow(10, N - 1)
    max = pow(10, N) - 1
    sol = random.randint(min, max)
    return sol


