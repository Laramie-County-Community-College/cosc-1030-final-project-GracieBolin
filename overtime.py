import random
 
#going into overtime, function
def overtime(): 
    return "loss" if random.randint(1, 100) >= 51 else "win"

shots = 10000
totalwins = 0
totallosses = 0


#for loop to run trials for probability you win the game in overtime
for _ in range(shots):
    result = overtime()
    if result == "win":
        totalwins += 1
        team1score = 78
        
    else:
        totallosses += 1
        team1score = 75

overtime_success_rate = (totalwins / shots) * 100

overtime_success_rate_decimal = (totalwins / shots)

print(overtime_success_rate, overtime_success_rate_decimal)






















