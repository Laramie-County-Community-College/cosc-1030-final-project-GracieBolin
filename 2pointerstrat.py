import random

def strat2p():
    return "miss" if random.randint(1, 100) >= 58 else "score"

shots = 10000
scores2 = 0
misses2 = 0

for _ in range(shots):
    game_time = 8
    result = strat2p()
    if result == "score":
        scores2 += 1

    else:
        misses2 += 1


p2percentage_success = (scores2 / shots) * 100
p2percentage_success_decimal = (scores2 / shots)


print(p2percentage_success)




























