# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:59:42 2015

@author: chr7stos
"""

import random
import matplotlib
import matplotlib.pyplot as plt

lower_bust = 31.235
higher_profit = 63.208 #variables we want to beat

sampleSize = 100
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
 

def multiple_bettor(funds, initial_wager, wager_count, color):
    global multiple_busts
    global multiple_profits
    
    value = funds
    wager = initial_wager
    
    wagerX = []
    valueY = []

    currentWager = 1
    previousWager = 'win'
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
                    multiple_busts += 1
                    break
                    
        elif previousWager == "loss":
            #print("we lost last, so will now double the next")
            if rollDice():
                wager = previousWagerAmount * random_multiple
                
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
                wager = previousWagerAmount * random_multiple
                if (value-wager)<0:
                    wager = value
                #print("we lost",wager)
                value -= wager
                previousWagerAmount = wager
                wagerX.append(currentWager)
                valueY.append(value)
                if value <= 0:
                    #print("we went broke after",currentWager,"bets")
                    multiple_busts += 1
                    break
                
                #print(value)
                previousWager = "loss"
                
                
            
        currentWager += 1

    #print(value)
    #plt.plot(wagerX, valueY, color)
    if value > funds:
        multiple_profits += 1
    




      
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

while True:
    multiple_busts = 0.0
    multiple_profits = 0.0
    
    multipleSampSize = 100000
    currentSample = 1
    
    random_multiple = random.uniform(0.1, 10.0)
    
    while currentSample <= multipleSampSize: #it will do 10000 attempts
        multiple_bettor(startingFunds,wagerSize,wagerCount, color = 'k')
        currentSample += 1
        
    if ((multiple_busts/multipleSampSize)*100.00 < lower_bust) and ((multiple_profits/multipleSampSize)*100.00 > higher_profit):
        print("##############")
        print("found winner, multiple was:",random_multiple)
        print("lower bust to beat:", lower_bust)
        print("higher profit rate to beat:", higher_profit)
        print("bust rate:",(multiple_busts/multipleSampSize)*100.00)
        print("profit rate",(multiple_profits/multipleSampSize)*100.00)
        print("##############")
        
    else:
        pass
        #print("##############")
        #print("found loser, multiple was:",random_multiple)
        #print("lower bust to beat:", lower_bust)
        #print("higher profit rate to beat:", higher_profit)
        #print("bust rate:",(multiple_busts/multipleSampSize)*100.00)
        #print("profit rate",(multiple_profits/multipleSampSize)*100.00)
        #print("##############")
