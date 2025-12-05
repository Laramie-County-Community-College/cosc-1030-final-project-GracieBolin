import random

def strat3p(trials=10000):

    #a single 3-point shot
    def shoot():
        return "score" if random.random() < 0.38 else "miss"

    first_shot_made = 0
    both_shots_made = 0

    for _ in range(trials):
        # First 3-pointer
        s1 = shoot()
        if s1 == "score":
            first_shot_made += 1

            # second 3-pointer only happens if first is made
            s2 = shoot()
            if s2 == "score":
                both_shots_made += 1

    p_first = (first_shot_made / trials) * 100
    p_both = (both_shots_made / trials) * 100  # winning probability

    print("First-shot success rate:", p_first, "%")
    print("Win probability (2 straight 3s):", p_both, "%")
























