# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:59:42 2015

@author: chr7stos
"""

import random
import matplotlib
import matplotlib.pyplot as plt

sampleSize = 1000
startingFunds = 10000
wagerSize = 100
wagerCount = 100

def rollDice():
    roll = random.randint(1,100)
    
    if roll == 100:
        #print(roll, "Lose")
        return False
    elif roll <= 50:
        #print(roll, "Lose")
        return False
    else:
        #print(roll, "Win")
        return True
       
def doubler_bettor(funds, initial_wager, wager_count, color):
    value = funds
    wager = initial_wager
    global doubler_busts
    global doubler_profits
    
    wagerX = []
    valueY = []
    
    currentWager = 1
    previousWager = "win"
    previousWagerAmount = initial_wager
    
    while currentWager <= wager_count:
        if previousWager == "win":
            #print("won the last wager, great")
            if rollDice():
                value += wager
                #print(value)
                wagerX.append(currentWager)
                valueY.append(value)
            else:
                value -= wager
                previousWager = "loss"
                #print(value)
                previousWagerAmount = wager
                wagerX.append(currentWager)
                valueY.append(value)
                if value <= 0:
                    #print("went broke after".currentWager,"bets")
                    doubler_busts += 1
                    break
                    
        elif previousWager == "loss":
            #print("we lost last, so will now double the next")
            if rollDice():
                wager = previousWagerAmount * 2
                
                if (value-wager) < 0:
                    wager = value
                #print("we won",wager)
                value += wager
                #print(value)
                wager = initial_wager
                previousWager = "win"
                wagerX.append(currentWager)
                valueY.append(value)
            else:
                wager = previousWagerAmount * 2
                if (value-wager)<0:
                    wager = value
                #print("we lost",wager)
                value -= wager
                previousWagerAmount = wager
                wagerX.append(currentWager)
                valueY.append(value)
                if value <= 0:
                    #print("we went broke after",currentWager,"bets")
                    doubler_busts += 1
                    break
                
                #print(value)
                previousWager = "loss"
                
                
            
        currentWager += 1

    #print(value)
    plt.plot(wagerX, valueY, color)
    if value > funds:
        doubler_profits += 1
    

                
            
def simple_bettor(funds, initial_wager, wager_count, color):
    global simple_busts
    global simple_profits
    value = funds
    wager = initial_wager
    
    wagerX = []
    valueY = []
    
    current_wager = 1 #this way it ends at 100 and not 99
    
    while current_wager <= wager_count:
        if rollDice():
            value += wager
            wagerX.append(current_wager)
            valueY.append(value)
        else:
            value -= wager
            wagerX.append(current_wager)
            valueY.append(value)
        current_wager += 1
        
    if value <= 0:
        #value = "broke" I was getting a type error here, because when the
        #this if condition was satisfied, I ended up comparing an integer with a string
        value = 0
        simple_busts+=1
        
    #print("Funds:", value) #shifting this, prints funds at the very end only

    plt.plot(wagerX,valueY,color)
    if value > funds:
        simple_profits += 1
    

#make a simple counter here

x = 0

simple_busts = 0.0
doubler_busts = 0.0
simple_profits = 0.0
doubler_profits = 0.0


while x < sampleSize:
    simple_bettor(startingFunds,wagerSize,wagerCount, 'k') 
    doubler_bettor(startingFunds,wagerSize,wagerCount, 'c')

    x += 1
    
print('Simple bettor bust chance:',(simple_busts/sampleSize)*100)
print('Doubler bettor bust chance:', (doubler_busts/sampleSize)*100)

print('Simple bettor profit chances:',(simple_profits/sampleSize)*100)
print('Doubler bettor profit chances:',(doubler_profits/sampleSize)*100)

plt.axhline(0, color = 'r')
plt.ylabel("Account value")
plt.xlabel("Wager count")
plt.show()