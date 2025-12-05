import three_pointer

import attemptfoulstrat



print("Simulation: What Stradegy in Basketball has the Highest Success Rate in the Last 30 Seconds of the Game?")

print("There are 2 main strategys: The Three pointer and Attempting a Foul")


print("=== The Three-Pointer Strategy ===")
print("Assuming the 3 pointer stradegy is trying to score 2 three pointers within the last 30 seconds of the game, the results for this strategy are:")

three_pointer.strat3p() 

print("=== Attemping a Foul ===")

print("Now the assuming the foul strategy is trying to pull a foul on your own team to stop the clock the results of that strategy would be:")

print("Final loss probability:", attemptfoulstrat.final_loss_probability,"%")
print("Final win probability:", attemptfoulstrat.final_win_probability,"%")

print("In comparison the three-pointer strategy is about three times higher in probability to win.")







































