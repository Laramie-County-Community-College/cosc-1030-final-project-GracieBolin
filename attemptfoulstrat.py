import random


def foulstrat():
    def attempt_foul():
        return random.random() < 0.50   # 50% success

    trials = 10000
    successes = 0

    for _ in range(trials):
        if attempt_foul():
            successes += 1
    
    #decimal form
    foul_attempt_percentage = (successes / trials) 
    return foul_attempt_percentage


def free_throw_simulation():
    def free_throw(make_rate=0.70):
        return random.random() < make_rate


    def defensive_rebound(rate=0.90):
        return random.random() < rate

    # chance your team scores if you get the ball back
    def final_possession(score_rate=0.40):
        return random.random() < score_rate


    def simulate_endgame(trials=10000,
                        ft_rate=0.70,
                        dreb_rate=0.90,
                        final_score_rate=0.40):

        wins = 0
        losses = 0

        for _ in range(trials):

            ft1 = free_throw(ft_rate)


            ft2 = free_throw(ft_rate)

            # If opponent makes the second ft game over, you lose
            if ft2:
                losses += 1
                continue

            # If the second ft misses you have a chance to rebound
            got_rebound = defensive_rebound(dreb_rate)

            if not got_rebound:
                # Opponent gets offensive rebound you lose
                losses += 1
                continue

            # You get final possession
            made_final_shot = final_possession(final_score_rate)

            if made_final_shot:
                wins += 1
            else:
                losses += 1

        # decimal forms
        win_percentage = (wins / trials)
        loss_percentage = (losses / trials)
        
        return win_percentage, loss_percentage

    return simulate_endgame()


foul_attempt_probability = foulstrat()                     
win_probability, loss_probability = free_throw_simulation()


final_win_probability = (foul_attempt_probability * win_probability) * 100
final_loss_probability = (foul_attempt_probability * loss_probability) * 100


print("Final Win Probability:", final_win_probability)
print("Final Loss Probability:", final_loss_probability)





















