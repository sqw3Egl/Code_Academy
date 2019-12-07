import random
import time

money = 100
num = random.randint(1, 10)

#Casino Games - functions

def coin_flip():
    bank = money
    bet = input('How much do you want to bet? \n')
    call = input('Make the call - type "heads" or "tails"... \n')
    print('OK mate, ' + call + ' it is! \nFlipping the coin........')
    time.sleep(3)
    #print(num)
#Check the coin flip and return a result.
    if call == 'heads' and num <= 5:
        return 'WINNER!! You have won £' + str(int(bet) * 2) + '!!' 
    elif call == 'tails' and num <= 5:
        return 'Sorry, you lost this time :(' + ' You lose your £' + str(bet) + ' bet.' 
    elif call == 'heads' and num >= 6:
        return 'Sorry, you lost this time :(' + ' You lose your £' + str(bet) + ' bet.' 
    else:
        return 'WINNER!! You have won £' + str(int(bet) * 2) + '!!' 
   
    
##ToDo - Make the account balance update to reflect the result.
#Print the account balance
#print('You have £' + str(bank) + ' remaining in your account. Why not try again?')






#Test calls
print(coin_flip())



