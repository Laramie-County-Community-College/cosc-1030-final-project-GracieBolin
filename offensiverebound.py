import random

def offensiverb():
    return "lost" if random.randint(1, 100) >= 51 else "gainedback"

shots = 10000
lost = 0 
gainedback = 0

for _ in range(shots):
    result = offensiverb()
    if result == "gainedback":
        gainedback += 1
        
    else:
        lost += 1

offensiverbsuccess_probability = (gainedback / shots) * 100
offensiverbfailed_probability = (lost / shots) * 100

offensiverbsuccess_probability_decimal = (gainedback / shots)
offensiverbfailed_probability_decimal = (lost / shots)

print(offensiverbsuccess_probability, offensiverbfailed_probability)



















