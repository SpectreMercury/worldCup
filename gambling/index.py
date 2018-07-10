# -*- coding: UTF-8 -*-
import random
import matplotlib.pyplot as plt
import matplotlib as mpl

value_set = []
Loser = 0
Broker = 0
BET_TIMES = 100

# let us go ahead and change this to return a simple win/loss
def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        #print roll,'roll was 100, you lose. What are the odds?! Play again!'
        return False
    elif roll <= 50:
        #print roll,'roll was 1-50, you lose.'
        return False
    elif 100 > roll >= 50:
        #print roll,'roll was 51-99, you win! *pretty lights flash* (play more!)'
        return True

def simple_bettor(funds,initial_wager,wager_count):
    global value_set
    global Loser
    global Broker
    value = funds
    wager = initial_wager
    currentWager = 0
    while currentWager < wager_count:
        if rollDice():
            value += wager
            if initial_wager != 100:
              initial_wager = initial_wager - 100
        else:
            value -= wager
            initial_wager = initial_wager + 100
        value_set.append(value)
        currentWager += 1
    plt.plot(value_set)
    value_set = []
    # changed to reduce spam
    if value < 0:
      #Broker = Broker + 1
      print 'Broke!'
    if value < funds:
      Loser = Loser + 1
    #print 'Funds:', value
    return value

# lots of wagers now....
x = 0

while x < 100:
    value = simple_bettor(10000,100,BET_TIMES)
    value_set.append(value)
    #print value_set
    x += 1
print Broker
print Loser
plt.xlabel('WAGER TIMES')
plt.ylabel('PAY OFF') 
plt.title('BET TIMES:' + str(BET_TIMES) + ' / LOSER:' + str(Loser) + ' / BROKERS:' + str(Broker))
plt.text(60, 10, r'$\mu=100,\ \sigma=15$')
plt.show()
