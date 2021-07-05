import random

streak = 0
numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = random.choices(('H', 'T'),k=100)

    # Code that checks if there is a streak of 6 heads or tails in a row.
    flag = 0

    for i in range(len(flips)):
        if i == 0:
            pass
        elif flips[i] == flips[i-1]:  
            streak += 1 
        else:
            streak = 0

        if streak == 5:
            flag = 1
            
    if flag == 1:
        numberOfStreaks+=1
        
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
