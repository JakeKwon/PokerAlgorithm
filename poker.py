#********************************************
#poker.py
# 
#Hold'Em supersystem
#
#Written by Jake Kwon   
#********************************************
import random

computerfirstcard = 0
computersecondcard = 0
playerfirstcard = 0
playersecondcard = 0
flopfirst = 0
flopsecond = 0
flopthird = 0
turncard = 0
rivercard = 0
winner = 0
folds = 0
games = 0
bets = 0
 
def main():
    greeting()
    playgame()
    
def assign(card):
    '''assign values'''                                                    
    if card == 1:
        return "Ace of Spades"
    if card == 2:
        return "2 of Spades"
    if card == 3:
        return "3 of Spades"
    if card == 4:
        return "4 of Spades"
    if card == 5:
        return "5 of Spades"
    if card == 6:
        return "6 of Spades"
    if card == 7:
        return "7 of Spades"
    if card == 8:
        return "8 of Spades"
    if card == 9:
        return "9 of Spades"
    if card == 10:
        return "10 of Spades"
    if card == 11:
        return "Jack of Spades"
    if card == 12:
        return "Queen of Spades"
    if card == 13:
        return "King of Spades"
    if card == 14:
        return "Ace of Hearts"
    if card == 15:
        return "2 of Hearts"
    if card == 16:
        return "3 of Hearts"
    if card == 17:
        return "4 of Hearts"
    if card == 18:
        return "5 of Hearts"
    if card == 19:
        return "6 of Hearts"
    if card == 20:
        return "7 of Hearts"
    if card == 21:
        return "8 of Hearts"
    if card == 22:
        return "9 of Hearts"
    if card == 23:
        return "10 of Hearts"
    if card == 24:
        return "Jack of Hearts"
    if card == 25:
        return "Queen of Hearts"
    if card == 26:
        return "King of Hearts"
    if card == 27:
        return "Ace of Diamonds"
    if card == 28:
        return "2 of Diamonds"
    if card == 29:
        return "3 of Diamonds"
    if card == 30:
        return "4 of Diamonds"
    if card == 31:
        return "5 of Diamonds"
    if card == 32:
        return "6 of Diamonds"
    if card == 33:
        return "7 of Diamonds"
    if card == 34:
        return "8 of Diamonds"
    if card == 35:
        return "9 of Diamonds"
    if card == 36:
        return "10 of Diamonds"
    if card == 37:
        return "Jack of Diamonds"
    if card == 38:
        return "Queen of Diamonds"
    if card == 39:
        return "King of Diamonds"
    if card == 40:
        return "Ace of Clubs"
    if card == 41:
        return "2 of Clubs"
    if card == 42:
        return "3 of Clubs"
    if card == 43:
        return "4 of Clubs"
    if card == 44:
        return "5 of Clubs"
    if card == 45:
        return "6 of Clubs"
    if card == 46:
        return "7 of Clubs"
    if card == 47:
        return "8 of Clubs"
    if card == 48:
        return "9 of Clubs"
    if card == 49:
        return "10 of Clubs"
    if card == 50:
        return "Jack of Clubs"
    if card == 51:
        return "Queen of Clubs"
    if card == 52:
        return "King of Clubs"
    
    
def hands():
    '''deals cards'''                                                    
    player1card1 = int(random.random()*52 + 1)
    
    player1card2 = int(random.random()*52 + 1)
    if player1card1 == player1card2:
        while player1card1 == player1card2:
            player1card2 = int(random.random()*52 + 1)
    
    computercard1 = int(random.random()*52 + 1)
    if computercard1 == player1card1 or computercard1 == player1card2:
        while computercard1 == player1card1 or computercard1 == player1card2:
            computercard1 = int(random.random()*52 + 1)
    
    computercard2 = int(random.random()*52 + 1)
    if computercard2 == computercard1 or computercard2 == player1card1 or computercard2 == player1card2:
        while computercard2 == computercard1 or computercard2 == player1card1 or computercard2 == player1card2:
            computercard2 = int(random.random()*52 + 1)
    
    global playerfirstcard
    global playersecondcard
    global computerfirstcard
    global computersecondcard
    
    playerfirstcard = player1card1
    playersecondcard = player1card2
    computerfirstcard = computercard1
    computersecondcard = computercard2
    
    print "your cards are " + assign(player1card1) + ", and " + assign(player1card2)  
    print computercard1
    print computercard2

def playgame():    
    '''general game structure'''  
    global games
    global folds
    global bets
    
    smallblind = 5
    bigblind = 10
    buyin = 1000
    again = 'y'
    
    print 'Game goes like this: we both buy-in $' + str(buyin)
    print 'smallblind: $' + str(smallblind)
    print 'bigblind: $' + str(bigblind)
    
    player1cash = buyin
    computercash = buyin       
    #
    #betting
    #
    print "computer starts game as a dealer(big blind)"
    tablemoney = 0
    dealer = "computer"
    
    game = "preflop"
    stage =1
    #table money goes 0 at the end
    raising ="ongoing"

    while again == "y":
        if game == "over":
            #reset the setting
            game = "preflop"
            raising ="ongoing"
            tablemoney = 0
            stage = 1
            bets = 0
            
            #keeping track of the number of game
            games = games +1
            
        while game == "preflop" or game == "flop" or game == "turn" or game == "river":
                                
            if game == "preflop":
                hands()
                tablemoney = smallblind+bigblind
                player1cash = player1cash - smallblind
                computercash = computercash - bigblind
    
            playermove = raw_input("Your turn (call/bet/fold, if you want to bet/raise please type in how much you want to bet/raise)")
                            
            #player calls before the flop
            if playermove != "fold": 
                if (playermove == "call" or playermove == "check") and game == "preflop":
                    tablemoney = tablemoney + smallblind
                    player1cash = player1cash - smallblind
                    print "table money: $" + str(tablemoney)
                    print "you: $" + str(player1cash)
                    print "computer: $" + str(computercash)
                    
                if playermove != "check" and playermove != "call" and playermove != "fold" and playermove >0:
                    print "you bet " + str(playermove)
                    tablemoney = tablemoney + int(playermove)
                    player1cash = player1cash - int(playermove)
                    print "table money: $" + str(tablemoney)
                    print "you: $" + str(player1cash)
                    print "computer: $" + str(computercash)
                
                computermove = "call" ################################################################################################################
                
                #computer checks after player calls the blind
                while raising == "ongoing":###########skeptical
                    raising = "no"
                    if computermove != "fold":
                        if computermove == "check" or computermove == "call":
                            print "computer called"
                            
                            #this codes takes money from computer according to how much it checked player's bet 
                            if playermove != "check" and playermove != "call" and playermove != "fold" and playermove >0:
                                computercash = computercash - int(playermove)
                                tablemoney = tablemoney + int(playermove)
                                print "table money: $" + str(tablemoney)
                                print "you: $" + str(player1cash)
                                print "computer: $" + str(computercash)
                        
                        if computermove != "call" and computermove != "fold" and computermove > 0:
                            print "computer bets" + str(computermove)
                            tablemoney = tablemoney + int(computermove)
                            computercash = computercash - int(computermove) 
                            print "table money: $" + str(tablemoney)
                            print "you: $" + str(player1cash)
                            print "computer: $" + str(computercash)
                            playermove = raw_input("Your turn (call/raise/fold, if you want to bet/raise please type in how much you want to bet/raise)")
                            
                            if playermove == "call":
                                tablemoney = tablemoney + int(computermove)
                                player1cash = player1cash - int(computermove) 
                                print "table money: $" + str(tablemoney)
                                print "you: $" + str(player1cash)
                                print "computer: $" + str(computercash)
                            elif playermove == "fold":
                                print "you lost"
                                computercash = computercash + int(tablemoney)
                                print "table money: $" + str(tablemoney)
                                print "you: $" + str(player1cash)
                                print "computer: $" + str(computercash)
                                again = raw_input("Do you wanna play more? (y/n)")
                                
                                #keeping track of the number of folds
                                folds = folds +1
                                
                            elif playermove != "call" and playermove != "fold" and playermove != "ceck" and playermove > 0:
                                raising ="ongoing"
                                print "you bet " + str(playermove)
                                tablemoney = tablemoney + int(playermove)
                                player1cash = player1cash - int(playermove)
                                print "table money: $" + str(tablemoney)
                                print "you: $" + str(player1cash)
                                print "computer: $" + str(computercash)
                                bets = bets+1
                                computermove = "call" #############################
                                                                    
                        if game == "preflop" and playermove != "fold" and computermove!= "fold" and raising == "no":
                            flop(playerfirstcard, playersecondcard, computerfirstcard, computersecondcard)
                            game = "flop"
                            bets = 0
                            
                        if game == "flop" and stage == 2 and playermove != "fold" and computermove!= "fold" and raising == "no":
                            turn(playerfirstcard, playersecondcard, computerfirstcard, computersecondcard, flopfirst, flopsecond, flopthird)
                            game = "turn"
                            bets = 0
                        
                        if game == "turn" and stage == 3 and playermove != "fold" and computermove!= "fold" and raising == "no":
                            river(playerfirstcard, playersecondcard, computerfirstcard, computersecondcard, flopfirst, flopsecond, flopthird, turn)
                            game = "river"
                            bets = 0
                            
                        if game == "river" and stage ==4 and playermove != "fold" and computermove!= "fold" and raising == "no":
                            winner = showdown()
                            print "computer cards are " + assign(computerfirstcard) + " and " + assign(computersecondcard)
                            
                            if winner == "player":
                                print "you win!"
                                player1cash = player1cash + int(tablemoney)  
                            if winner == "computer":
                                print "computer won"
                                computercash = computercash + int(tablemoney)
                            if winner == "draw":
                                print "draw! split the pot"
                                player1cash = player1cash + int(tablemoney)/2
                                computercash = computercash + int(tablemoney)/2
                            print "table money: $" + str(tablemoney)
                            print "you: $" + str(player1cash)
                            print "computer: $" + str(computercash)
                                
                            again = raw_input("Do you wanna play more? (y/n)")
                            game = "over"
                            
                    if computermove == "fold":
                        print "computer folded. You Win!"
                        player1cash = player1cash + int(tablemoney)  
                        print "table money: $" + str(tablemoney)
                        print "you: $" + str(player1cash)
                        print "computer: $" + str(computercash)
                        again = raw_input("Do you wanna play more? (y/n)")
                     ########skeptical till here                                       
            
            #player folds on the flop
            if playermove == "fold":
                print "you lost"
                computercash = computercash + tablemoney
                print "table money: $" + str(tablemoney)
                print "you: $" + str(player1cash)
                print "computer: $" + str(computercash)
                again = raw_input("Do you wanna play more? (y/n)")
                
                #keeping track of the number of folds
                folds = folds +1
                                        
            stage = stage +1
            raising = "ongoing"
            #dealer = "player"
            
    print "final result: you have $" + str(player1cash) + " computer has $" + str(computercash)
    print "Thanks for playing game"
                
def computermind(gametype, tablecash, highraise, playerchoice): #inside ()  game, playermove, number of games played, # of folds, # of bet/raise, # of call
    '''Bot Artificial Intelligence (incomplete)'''  
    global computerfirstcard
    global computersecondcard
    global folds
    global games
    global bets
    
    c1 = computerfirstcard
    c2 = computersecondcard
    cardtype = "else"
    preflopmove = "call"
    flopmove = "call"
    turnmove = "call"
    rivermove = "call"
    playertype = ""
    
    
    #switch gears
    #when player is tight, play loose
    #when player is loose, play tight
    # when player likes to call bluff the hell out
    # and watch what you think that player think of you
    #watch what the player do : ex) he doesnt bluff twice or he changes gear here and there
    if folds !=0:
        if (folds /games)>= .5:
            # you might give it a shot for bluff
            playertype = "tight" 
            
        if .2 < (folds /games) < .5:
            # dont bluff so much but sometimes 
            playertype = "loose" 
        
        if (folds /games) <= .2:
            # dont even
            playertype = "calling station"
        
    #preflop strategy
    if gametype == "preflop":
        #check the cards
        #connecting cards
        if (c1%13 == c2%13 +1 or c1%13 +1 == c2%13):
            cardtype = "call"
        #pocket
        if (c1%13 == c2 %13):
            cardtype = "call"
        #facecards
        if (c1%13 == 1 or c1%13 == 0 or c1 %13 >10) or (c2%13 == 1 or c2%13 == 0 or c2 %13 >10): # notsure whether or or and
            cardtype = "call"
        #suited
        if (c1<=13 and c2<=13) or (14<=c1<=26 and 14<=c2<=26) or (27<=c1<=39 and 27<=c2<=39) or (40<=c1 and 40<=c2):
            cardtype = "call"
        #AA or AK
        if (c1%13 == 1 and c2 %13 == 1) or (c1%13 == 1 and c2 %13 ==0) or (c1%13 == 0 and c2 %13 ==1):
            cardtype = "reraise"
        #KK
        if (c1%13 == 0 and c2 %13 ==0):
            cardtype = "reraise"
        
        if cardtype == "else":
            #probability
            i = random.random()
            #call/check the hand for 70%
            if i >= .5:
                return "call"
            #by 30%
            else:
                return "fold"
                
            #did player raise after i bet?
            if highraise == "ongoing" and tablecash < (playerchoice *2):
                if i <.85:
                    return "fold"
                else: ####################################################################this is bluff
                    return "call"
                    
            if highraise == "ongoing" and tablecash >= (playerchoice *2):
                if i <= .7:
                    return "call"
                elif .7 < i < .9:
                    return "call"
                else: ####################################################################this is bluff
                    return tablecash*2
                    preflopmove= "bet"
        
        if cardtype == "call":
            #probability
            i = random.random()
            #call/check the hand for 70%
            if i >= .3:
                return "call"
            #by 30%
            if i <.3:
                return tablecash*2
                preflopmove= "bet"
                
            #did player raise after i bet?
            if highraise == "ongoing" and tablecash < (playerchoice *2):
                if i <=.6:
                    return "fold"
                elif .6< i <.95:
                    return "call"
                else:####################################################################this is bluff
                    return tablecash*2
                    preflopmove= "bet"
                    
            if highraise == "ongoing" and tablecash >= (playerchoice *2):
                if i < .6:
                    return "call"
                elif .6< i <.95:
                    return "fold"
                else:####################################################################this is bluff
                    return tablecash*2
                    preflopmove= "bet"
                    
        if cardtype == "reraise":
            i = random.random()
            if i<= .15:
                return "call"
            #by 30%
            if i >.15:
                return tablecash*2
                preflopmove= "bet"
            
            #did player raise after i bet?
            if highraise == "ongoing" and tablecash < (playerchoice *2):
                if i <.6:
                    return "call"
                else:
                    return (tablecash * .8)
                    preflopmove= "bet"
                    
            if highraise == "ongoing" and tablecash >= (playerchoice *2):
                if i < .6:
                    return "call"
                else:
                    return (tablecash * .8)
                    preflopmove= "bet"
    
    #on the flop
    f1 = flopfirst 
    f2 = flopsecond 
    f3 = flopthird 
    flopscore = cardrank(f1, f2, f3, c1, c2)
    
    i = random.random()
    #if gametype== "flop":
    #royal flush  ==582165
    if flopscore == 582165:
        if playerchoice != "check" or "call":
            if preflopmove == "bet":
                #80%
                if i < .8:
                    return tablecash *.8
                else:
                    return "call"
            else:
                #50%
                if i < .3:
                    return tablecash *.8
                else:
                    return "call"
            
        #there is no difference between what player does here but make change later if u figure out a better strategy!'''        
        else:
            if preflopmove == "bet":
                #80%
                if i < .8:
                    return tablecash *.8
                else:
                    return "call"
            else:
                #50%
                if i < .3:
                    return tablecash *.8
                else:
                    return "call"
            
               
    #straight flush 582150<  <=582164
    if 582150< flopscore <=582164:
        if playerchoice != "check" or "call":
            if preflopmove == "bet":
                #80%
                if i < .8:
                    return tablecash *.8
                else:
                    return "call"
            else:
                #50%
                if i < .3:
                    return tablecash *.8
                else:
                    return "call"
            
        #there is no difference between what player does here but make change later if u figure out a better strategy!'''        
        else:
            if preflopmove == "bet":
                #80%
                if i < .8:
                    return tablecash *.8
                else:
                    return "call"
            else:
                #50%
                if i < .3:
                    return tablecash *.8
                else:
                    return "call"
            
    
    #four cards 581954<  <=582150
    if 581954< flopscore <=582150:
        if playerchoice != "check" or "call":
            if preflopmove == "bet":
                #80%
                if i < .5:
                    return tablecash *.8
                else:
                    return "call"
            else:
                #50%
                if i < .4:
                    return tablecash *.8
                else:
                    return "call"
            
        #there is no difference between what player does here but make change later if u figure out a better strategy!'''        
        else:
            if preflopmove == "bet":
                #80%
                if i < .3:
                    return tablecash *.8
                else:
                    return "call"
            else:
                #50%
                if i < .2:
                    return tablecash *.8
                else:
                    return "call"
            
    #########################################################strategy same till here cuz u almost guarenteed to win with those hands
    #full house  581758<  <=581954 
    if 581758< flopscore <=581954:
        #note: divide to cases for higher pair and stuff you know : think of stuff that other player has the hand thats just little better than yous
        #ex) QQQKK vs KKKQQ
        if playertype == "tight" and bets >1:
            sort = sorted([c1,c2])
            top = sort[1]
            bot = sort[0]
            
            #it is dangerous when you have pocket or when there are pair on the board with your smaller card
            #player might have four cards or little higher full house
            if c1 ==c2 or  (f1%13 + f2%13 +f3%13 == top%13 + bot%13 *2):
                return "fold"
                
        if playerchoice != "check" or "call":
            if preflopmove == "bet":
                #80%
                if i < .5:
                    return tablecash *.8
                else:
                    return "call"
            else:
                #50%
                if i < .4:
                    return tablecash *.8
                else:
                    return "call"
            
        #there is no difference between what player does here but make change later if u figure out a better strategy!'''        
        else:
            if preflopmove == "bet":
                #
                if i < .3:
                    return tablecash *.8
                else:
                    return "call"
            else:
                #
                if i < .2:
                    return tablecash *.8
                else:
                    return "call"
    #flush  581744<  <=581758
    if 581744< flopscore <=581758:
        if playertype == "tight" and bets >1:
            # if your highest suited card is Jack or lower just fold for the tight player's aggressive move
            if calculator(c1)< 12 and calculator(c2)<12:
                return "fold"
                
        if playerchoice != "check" or "call":
            if preflopmove == "bet":
                #80%
                if i < .5:
                    return tablecash *.8
                else:
                    return "call"
            else:
                #
                if i < .4:
                    return tablecash *.8
                else:
                    return "call"
            
        #there is no difference between what player does here but make change later if u figure out a better strategy!'''        
        else:
            if preflopmove == "bet":
                #80%
                if i < .3:
                    return tablecash *.8
                else:
                    return "call"
            else:
                #50%
                if i < .2:
                    return tablecash *.8
                else:
                    return "call"
                    ################################################################################################here####
    #straight  581728<  <=581744
    if 581728< flopscore <=581744:
        if playerchoice != "check" or "call":
            if preflopmove == "bet":
                #80%
                if i < .5:
                    return tablecash *.8
                else:
                    return "call"
            else:
                #50%
                if i < .4:
                    return tablecash *.8
                else:
                    return "call"
            
        #there is no difference between what player does here but make change later if u figure out a better strategy!'''        
        else:
            if preflopmove == "bet":
                #80%
                if i < .3:
                    return tablecash *.8
                else:
                    return "call"
            else:
                #50%
                if i < .2:
                    return tablecash *.8
                else:
                    return "call"
    
    #trip 578984<  <=581728
    
    
    #two pair 576240<  <=578984
    
    
    #pair 537824<  <=576240
    
    
    #highcard  <= 537824
    
    
    #value check
    f1 = flopfirst 
    f2 = flopsecond 
    f3 = flopthird 
    t = turncard 
    r = rivercard 
    
    list21 = cardrank(c1, f2, f3, t, r)
    list22 = cardrank(f1, c1, f3, t, r)
    list23 = cardrank(f1, f2, c1, t, r) 
    list24 = cardrank(f1, f2, f3, c1, r)
    list25 = cardrank(f1, f2, f3, t, c1)
    list26 = cardrank(c2, f2, f3, t, r)
    list27 = cardrank(f1, c2, f3, t, r)
    list28 = cardrank(f1, f2, c2, t, r)
    list29 = cardrank(f1, f2, f3, c2, r)
    list30 = cardrank(f1, f2, f3, t, c2)
    list31 = cardrank(c1, c2, f3, t, r)
    list32 = cardrank(c1, f2, c2, t, r)
    list33 = cardrank(c1, f2, f3, c2, r)
    list34 = cardrank(c1, f2, f3, t, c2)
    list35 = cardrank(f1, c1, c2, t, r)
    list36 = cardrank(f1, c1, f3, c2, r)
    list37 = cardrank(f1, c1, f3, t, c2)
    list38 = cardrank(f1, f2, c1, c2, r)
    list39 = cardrank(f1, f2, c1, t, c2)
    list40 = cardrank(f1, f2, f3, c1, c2)
    
    scorelist = sorted([list21, list22, list23, list24, list25, list26, list27, list28, list29, list30, \
    list31, list32, list33, list34, list35, list36, list37, list38, list39, list40])
    
    computerrank = scorelist[19]
        
        
        
        
def flop(player1card1, player1card2, computercard1, computercard2):
    '''flop'''  
    flop1 = int(random.random()*52 + 1)
    if flop1 == computercard2 or flop1 == computercard1 or flop1 == player1card1 or flop1 == player1card2:
        while flop1 == computercard2 or flop1 == computercard1 or flop1 == player1card1 or flop1 == player1card2:
            flop1 = int(random.random()*52 + 1)
    global flopfirst
    flopfirst = flop1
            
    flop2 = int(random.random()*52 + 1)
    if flop2 == flop1 or flop2 == computercard2 or flop2 == computercard1 or flop2 == player1card1 or flop2 == player1card2:
        while flop2 == flop1 or flop2 == computercard2 or flop2 == computercard1 or flop2 == player1card1 or flop2 == player1card2:
            flop2 = int(random.random()*52 + 1)
    global flopsecond
    flopsecond = flop2
            
    flop3 = int(random.random()*52 + 1)
    if flop3 == flop2 or flop3 == flop1 or flop3 == computercard2 or flop3 == computercard1 or flop3 == player1card1 or flop3 == player1card2:
        while flop3 == flop2 or flop3 == flop1 or flop3 == computercard2 or flop3 == computercard1 or flop3 == player1card1 or flop3 == player1card2:
            flop3 = int(random.random()*52 + 1)
    
    global flopthird
    flopthird = flop3
            
    print "now here is the flop"            
    print assign(flop1) + ", " + assign(flop2) + ", " + assign(flop3)
    
def turn(player1card1, player1card2, computercard1, computercard2, flop1, flop2, flop3):
    '''the turn card'''
    turn = int(random.random()*52 + 1)
    if turn == flop3 or turn == flop2 or turn == flop1 or turn == computercard2 or turn == computercard1 or turn == player1card1 or turn == player1card2:
        while turn == flop3 or turn == flop2 or turn == flop1 or turn == computercard2 or turn == computercard1 or turn == player1card1 or turn == player1card2:
            turn = int(random.random()*52 + 1)
    global turncard
    turncard = turn
            
    print "the turn card is " + assign(turn)
    
def river(player1card1, player1card2, computercard1, computercard2, flop1, flop2, flop3, turn):
    '''the river card'''
    river = int(random.random()*52 + 1)
    if river == turn or river == flop3 or river == flop2 or river == flop1 or river == computercard2 or river == computercard1 or river == player1card1 or river == player1card2:
        while river == turn or river == flop3 or river == flop2 or river == flop1 or river == computercard2 or river == computercard1 or river == player1card1 or river == player1card2:
            river = int(random.random()*52 + 1)
    global rivercard
    rivercard = river
            
    print "the river card is " + assign(river)

def showdown():
    global playerfirstcard
    global playersecondcard
    global computerfirstcard
    global computersecondcard
    global flopfirst
    global flopsecond
    global flopthird
    global turncard
    global rivercard
    
    p1 = playerfirstcard 
    p2 = playersecondcard 
    c1 = computerfirstcard 
    c2 = computersecondcard 
    f1 = flopfirst 
    f2 = flopsecond 
    f3 = flopthird 
    t = turncard 
    r = rivercard 
  
    list1 = cardrank(p1, f2, f3, t, r) 
    list2 = cardrank(f1, p1, f3, t, r)
    list3 = cardrank(f1, f2, p1, t, r)
    list4 = cardrank(f1, f2, f3, p1, r)
    list5 = cardrank(f1, f2, f3, t, p1)
    list6 = cardrank(p2, f2, f3, t, r)
    list7 = cardrank(f1, p2, f3, t, r)
    list8 = cardrank(f1, f2, p2, t, r)
    list9 = cardrank(f1, f2, f3, p2, r)
    list10 = cardrank(f1, f2, f3, t, p2)
    list11 = cardrank(p1, p2, f3, t, r)
    list12 = cardrank(p1, f2, p2, t, r)
    list13 = cardrank(p1, f2, f3, p2, r)
    list14 = cardrank(p1, f2, f3, t, p2)
    list15 = cardrank(f1, p1, p2, t, r)
    list16 = cardrank(f1, p1, f3, p2, r)
    list17 = cardrank(f1, p1, f3, t, p2)
    list18 = cardrank(f1, f2, p1, p2, r)
    list19 = cardrank(f1, f2, p1, t, p2)
    list20 = cardrank(f1, f2, f3, p1, p2)
    list21 = cardrank(c1, f2, f3, t, r)
    list22 = cardrank(f1, c1, f3, t, r)
    list23 = cardrank(f1, f2, c1, t, r) 
    list24 = cardrank(f1, f2, f3, c1, r)
    list25 = cardrank(f1, f2, f3, t, c1)
    list26 = cardrank(c2, f2, f3, t, r)
    list27 = cardrank(f1, c2, f3, t, r)
    list28 = cardrank(f1, f2, c2, t, r)
    list29 = cardrank(f1, f2, f3, c2, r)
    list30 = cardrank(f1, f2, f3, t, c2)
    list31 = cardrank(c1, c2, f3, t, r)
    list32 = cardrank(c1, f2, c2, t, r)
    list33 = cardrank(c1, f2, f3, c2, r)
    list34 = cardrank(c1, f2, f3, t, c2)
    list35 = cardrank(f1, c1, c2, t, r)
    list36 = cardrank(f1, c1, f3, c2, r)
    list37 = cardrank(f1, c1, f3, t, c2)
    list38 = cardrank(f1, f2, c1, c2, r)
    list39 = cardrank(f1, f2, c1, t, c2)
    list40 = cardrank(f1, f2, f3, c1, c2)
    list41 = cardrank(f1, f2, f3, t, r)
    
    scorelist = sorted([list1, list2, list3, list4, list5, list6, list7, list8, \
    list9, list10, list11, list12, list13, list14, list15, list16, list17, list18, list19, \
    list20, list21, list22, list23, list24, list25, list26, list27, list28, list29, list30, \
    list31, list32, list33, list34, list35, list36, list37, list38, list39, list41, list40])
    
    winscore = scorelist[40]
    if winscore == list1 or winscore == list2 or winscore == list3 or winscore == list4\
    or winscore == list5 or winscore == list6 or winscore == list7 or winscore == list8\
    or winscore == list9 or winscore == list10 or winscore == list11 or winscore == list12\
    or winscore == list13 or winscore ==  list14 or winscore == list15 or winscore == list16\
    or winscore == list17 or winscore == list18 or winscore == list19 or winscore == list20:
        return "player"
        
    if winscore == list21 or winscore == list22 or winscore == list23 or winscore == list24\
    or winscore == list25 or winscore == list26 or winscore == list27 or winscore == list28\
    or winscore == list29 or winscore == list30 or winscore == list31 or winscore == list32\
    or winscore == list33 or winscore == list34 or winscore == list35 or winscore == list36\
    or winscore == list37 or winscore == list38 or winscore == list39 or winscore == list40:
        return "computer"
    
    if winscore == list41 or ((winscore == list1 or winscore == list2 or winscore == list3 or winscore == list4\
    or winscore == list5 or winscore == list6 or winscore == list7 or winscore == list8\
    or winscore == list9 or winscore == list10 or winscore == list11 or winscore == list12\
    or winscore == list13 or winscore ==  list14 or winscore == list15 or winscore == list16\
    or winscore == list17 or winscore == list18 or winscore == list19 or winscore == list20) and \
    (winscore == list21 or winscore == list22 or winscore == list23 or winscore == list24\
    or winscore == list25 or winscore == list26 or winscore == list27 or winscore == list28\
    or winscore == list29 or winscore == list30 or winscore == list31 or winscore == list32\
    or winscore == list33 or winscore == list34 or winscore == list35 or winscore == list36\
    or winscore == list37 or winscore == list38 or winscore == list39 or winscore == list40)):
        return "draw"
        print winscore
    
def cardrank(a,b,c,d,e):
    '''compares the value'''  
    inorder = sorted([a,b,c,d,e])
    c1 = inorder[0]
    c2 = inorder[1]
    c3 = inorder[2]
    c4 = inorder[3]
    c5 = inorder[4]
    
    #*************#
    # royal flush #
    #*************#
    if (c1 == 1 and c2 == 10 and c3 == 11 and c4 == 12 and c5 == 13) or \
    (c1 == 14 and c2 == 23 and c3 == 24 and c4 == 25 and c5 == 26) or \
    (c1 == 27 and c2 == 36 and c3 == 37 and c4 == 38 and c5 == 39) or \
    (c1 == 40 and c2 == 49 and c3 == 50 and c4 == 51 and c5 == 52):
        return 582165
    
    #****************#
    # straight flush #
    #****************#
    if (c5 <14 and c5 == c4 + 1 and c4 == c3 +1 and c3 == c2 +1 and c2 == c1+1) or \
    (c5 <27 and c1 > 13 and c5 == c4 + 1 and c4 == c3 +1 and c3 == c2 +1 and c2 == c1+1) or \
    (c5 <40 and c1 >30 and c5 == c4 + 1 and c4 == c3 +1 and c3 == c2 +1 and c2 == c1+1) or \
    (c1 >43 and c5 == c4 + 1 and c4 == c3 +1 and c3 == c2 +1 and c2 == c1+1): 
        i1 = 13
        i2 = 26
        i3 = 39
        i4 = 52
        score = 582164
        while i1 >4:
            if c5 == i1 or c5 == i2 or c5 == i3 or c5 == i4:
                return score
            i1 = i1 -1
            i2 = i2 -1
            i3 = i3 -1
            i4 = i4 -1
            score = score -1
            
    #****************#
    # four of a kind #
    #****************#
    if (c1%13 == c2%13 == c3%13 == c4%13) or \
    (c1%13 == c2%13 == c3%13 == c5%13) or \
    (c1%13 == c2%13 == c4%13 == c5%13) or \
    (c1%13 == c3%13 == c4%13 == c5%13) or \
    (c2%13 == c3%13 == c4%13 == c5%13):
        
        c1 = calculator(c1)
        c2 = calculator(c2)
        c3 = calculator(c3)
        c4 = calculator(c4)
        c5 = calculator(c5)
        #variables
        score = 582150
        fourcard1 = 14
        kicker = 14
        
        if (c1 == c2 == c3 == c4):       
            fourcardhand = c2
            kickerhand = c5
            
        if (c1 == c2 == c3 == c5):
            fourcardhand = c2
            kickerhand = c4
            
        if (c1 == c2 == c4 == c5):
            fourcardhand = c2
            kickerhand = c3
            
        if (c1 == c3 == c4 == c5):
            fourcardhand = c1
            kickerhand = c2
            
        if (c2 == c3 == c4 == c5):
            fourcardhand = c2
            kickerhand = c1      
        
        while fourcard1 > 1:
            if fourcardhand == fourcard1:
                while kicker >14:
                    if kickerhand == kicker:
                        return score
                    score = score -1
                    kicker = kicker-1
            else:
                score = score -14
            fourcard1 =fourcard1 -1
   
    #************#            
    # full house #
    #************#
    if (c1 %13 == c2%13 and c3 %13 == c4 % 13 == c5 % 13) or \
    (c1 %13 == c3%13 and c2 %13 == c4 % 13 == c5 % 13) or \
    (c1 %13 == c4%13 and c3 %13 == c2 % 13 == c5 % 13) or \
    (c1 %13 == c5%13 and c3 %13 == c4 % 13 == c2 % 13) or \
    (c3 %13 == c2%13 and c1 %13 == c4 % 13 == c5 % 13) or \
    (c4 %13 == c2%13 and c3 %13 == c1 % 13 == c5 % 13) or \
    (c5 %13 == c2%13 and c3 %13 == c4 % 13 == c1 % 13) or \
    (c3 %13 == c4%13 and c1 %13 == c2 % 13 == c5 % 13) or \
    (c3 %13 == c5%13 and c1 %13 == c4 % 13 == c2 % 13) or \
    (c4 %13 == c5%13 and c3 %13 == c1 % 13 == c2 % 13):
        
        c1 = calculator(c1)
        c2 = calculator(c2)
        c3 = calculator(c3)
        c4 = calculator(c4)
        c5 = calculator(c5)
        score = 581954
        house = 14
        kicker = 14
        
        if (c1 == c2 and c3 == c4 == c5):
            triphand = c3
            pairhand =c2
    
        if (c1 == c3 and c2 == c4 == c5) or \
        (c1 == c4 and c3 == c2 == c5) or \
        (c1 == c5 and c3 == c4 == c2):
            triphand = c2
            pairhand =c1
            
        if (c3 == c2 and c1 == c4 == c5) or \
        (c4 == c2 and c3 == c1 == c5) or \
        (c5 == c2 and c3 == c4 == c1):
            triphand = c1
            pairhand =c2
            
        if (c3 == c4 and c1 == c2 == c5) or \
        (c3 == c5 and c1 == c4 == c2):
            triphand = c1
            pairhand =c3
    
        if (c4 == c5 and c3 == c1 == c2):
            triphand = c1
            pairhand =c4
        
        while house > 1:
            if triphand == house:
                while kicker >1:
                    if pairhand == kicker:
                        return score
                    kicker = kicker -1
                    score = score -1
            else:
                score = score -14
            house = house -1
        
    #*******#
    # flush #
    #*******#
    if (1<=c1<=13 and 1<=c2<=13 and 1<=c3<=13 and 1<=c4<=13 and 1<=c5<=13) or\
    (14<=c1<=26 and 14<=c2<=26 and 14<=c3<=26 and 14<=c4<=26 and 14<=c5<=26) or\
    (27<=c1<=39 and 27<=c2<=39 and 27<=c3<=39 and 27<=c4<=39 and 27<=c5<=39) or\
    (40<=c1<=52 and 40<=c2<=52 and 40<=c3<=52 and 40<=c4<=52 and 40<=c5<=52):
        if c1% 13 ==1:
            return 581758
        
        if c5%13 == 0:
            return 581757
        
        kicker = 12
        score = 581756
        while kicker<1:
            if c5%13 == kicker:
                return score
            kicker = kicker -1
            score = score -1
            
    #**********#
    # straight #
    #**********#
    c1 = calculator(c1)
    c2 = calculator(c2)
    c3 = calculator(c3)
    c4 = calculator(c4)
    c5 = calculator(c5)
    
    straightlist=sorted([c1,c2,c3,c4,c5])
    st1=straightlist[0]
    st2=straightlist[1]
    st3=straightlist[2]
    st4=straightlist[3]
    st5=straightlist[4]
            
    if (st1 +1 == st2 and st2 +1 == st3 and st3 +1 == st4 and st4+1 ==st5):
        ruler = 14
        score = 581744
        while ruler > 4:
            if st5 == ruler:
                return score
            ruler = ruler-1
            score = score-1
   
    #*****************#    
    # three of a kind #
    #*****************#
    if c3 == c4 == c5 or c3 == c4 == c2 or c3 == c4 == c1 or c1 == c4 == c2 or\
    c3 == c1 == c2 or c2 == c4 == c5 or c3 == c2 == c5 or c1 == c4 == c5 or\
    c3 == c1 == c5 or c1 == c2 == c5:
        
        #variables
        score = 581728
        kicker = 14
        trips = 14
        trips2 = 14
        trips3 = 14
        
        if (c3 == c4 == c5):
            tripshand = c3
            tripslist = sorted([c1,c2])
    
        elif (c3 == c4 == c2):
            tripshand = c3
            tripslist = sorted([c1,c5])
            
        elif (c3 == c4 == c1):
            tripshand = c3
            tripslist = sorted([c5,c2])
            
        elif (c1 == c4 == c2):
            tripshand = c1
            tripslist = sorted([c3,c5])
            
        elif (c3 == c1 == c2):
            tripshand = c3
            tripslist = sorted([c4,c5])
        
        elif (c2 == c4 == c5):
            tripshand = c2
            tripslist = sorted([c1,c3])
            
        elif (c3 == c2 == c5):
            tripshand = c3
            tripslist = sorted([c1,c4])
                
        elif (c1 == c4 == c5):
            tripshand = c1
            tripslist = sorted([c2,c3])
            
        elif (c3 == c1 == c5):
            tripshand = c3
            tripslist = sorted([c4,c2])
            
        elif (c1 == c2 == c5):
            tripshand = c1
            tripslist = sorted([c3,c4])
        
        #variable
        topkicker = tripslist[1]
        botkicker = tripslist[0]
        
        while trips > 1:
            if tripshand == trips:
                while trips2>1:
                    if topkicker == trips2:
                        while trips3>1:
                            if botkicker ==trips3:
                                return score
                            trips3 = trips3-1
                            score = score -1
                    else:
                        score = score - 14
                    trips2 =trips2 -1
            else:
                score = score -196
            trips = trips -1
        
            
    #**********#   
    # two pair #
    #**********# 
    if (c2 == c3 and c4 == c5) or (c2 == c4 and c3 == c5) or (c2 == c5 and c4 == c3)\
    or (c1 == c3 and c4 == c5) or (c1 == c4 and c3 == c5) or (c1 == c5 and c4 == c3)\
    or (c1 == c2 and c4 == c5) or (c1 == c5 and c4 == c2) or (c1 == c4 and c2 == c5)\
    or (c2 == c1 and c3 == c5) or (c1 == c3 and c2 == c5) or (c1 == c5 and c2 == c3)\
    or (c2 == c1 and c4 == c3) or (c1 == c3 and c4 == c2) or (c1 == c4 and c2 == c3):
        
        #assign variables
        twopair1 =14
        twopair2 =14
        kicker = 14
        score= 578984
        
        if (c2 == c3 and c4 == c5):
            twopairlist = sorted([c2,c4])
            kickerhand = c1
        
        if (c2 == c4 and c3 == c5):
            twopairlist = sorted([c2,c3])
            kickerhand = c1
                    
        if (c2 == c5 and c4 == c3):
            twopairlist = sorted([c2,c4])
            kickerhand = c1
            
        #    
        if (c1 == c3 and c4 == c5):
            twopairlist = sorted([c1,c4])
            kickerhand = c2
            
        if (c1 == c4 and c3 == c5):
            twopairlist = sorted([c1,c3])
            kickerhand = c2
            
        if (c1 == c5 and c4 == c3):
            twopairlist = sorted([c1,c3])
            kickerhand = c2
                    
        #
        if (c1 == c2 and c4 == c5):
            twopairlist = sorted([c2,c4])
            kickerhand = c3
            
        if (c1 == c5 and c4 == c2):
            twopairlist = sorted([c1,c4])
            kickerhand = c3
            
        if (c1 == c4 and c2 == c5):
            twopairlist = sorted([c2,c4])
            kickerhand = c3
        
        #    
        if (c1 == c2 and c3 == c5):
            twopairlist = sorted([c2,c3])
            kickerhand = c4
            
        if (c1 == c3 and c2 == c5):
            twopairlist = sorted([c2,c3])
            kickerhand = c4
            
        if (c1 == c5 and c2 == c3):
            twopairlist = sorted([c2,c1])
            kickerhand = c4
            
        #    
        if (c1 == c2 and c4 == c3):
            twopairlist = sorted([c2,c4])
            kickerhand = c5
            
        if (c1 == c3 and c4 == c2):
            twopairlist = sorted([c2,c1])
            kickerhand = c5
            
        if (c1 == c4 and c2 == c3):
            twopairlist = sorted([c2,c4])
            kickerhand = c5
        
        #assign the higher hand
        toppair = twopairlist[1]
        botpair = twopairlist[0]
        
        while twopair1>1:
            if toppair == twopair1:
                while twopair2>1:
                    if botpair == twopair2:
                        while kicker>1:
                            if kickerhand ==kicker:
                                return score 
                            kicker = kicker-1
                            score = score-1
                    else:
                        score = score -14
                    twopair2 = twopair2-1
            else:
                score= score-196
            twopair1= twopair1-1
        
        
    #**********#    
    # one pair #
    #**********#
    if c1 == c2 or c1 == c3 or c1 == c4 or c1 == c5 or c2 == c3 or c2 == c4 or\
    c2 == c5 or c3 == c4 or c3 == c5 or c4 == c5 or c1 == c2:###########use this method for other checkups
        
        #variables
        thepair = 14
        kicker1 = 14
        kicker2 = 14
        kicker3 = 14
        score = 576240
        
        if c1 == c2:
            onepairlist = sorted([c3,c4,c5])
            pairhand =c1
            
        if c1 == c3:
            onepairlist = sorted([c2,c4,c5])
            pairhand =c1
           
        if c1 == c4:
            onepairlist = sorted([c3,c2,c5])
            pairhand =c1
            
        if c1 == c5:
            onepairlist = sorted([c3,c4,c2])
            pairhand =c1
            
        if c2 == c3:
            onepairlist = sorted([c1,c4,c5])
            pairhand =c2
            
        if c2 == c4:
            onepairlist = sorted([c3,c1,c5])
            pairhand =c2
           
        if c2 == c5:
            onepairlist = sorted([c3,c4,c1])
            pairhand =c2
            
        if c3 == c4:
            onepairlist = sorted([c1,c2,c5])
            pairhand =c3
        
        if c3 == c5:
            onepairlist = sorted([c1,c2,c4])
            pairhand =c3
               
        if c4 == c5:
            onepairlist = sorted([c3,c1,c2])
            pairhand =c4
            
        #variables
        topkicker = onepairlist[2]
        midkicker = onepairlist[1]
        botkicker = onepairlist[0]
            
        #the pair
        while thepair>1:
            if pairhand == thepair:
                #first kicker
                while kicker1>1:
                    if topkicker == kicker1:
                        #second kicker
                        while kicker2>1:
                            if midkicker ==kicker2:
                                #third kicker
                                while kicker3>1:
                                    if botkicker == kicker3:
                                        return score
                                    score = score -1
                                    kicker3 = kicker3-1                  
                            else:
                                score = score-14
                            kicker2 = kicker2-1
                    else:
                        score = score -196
                    kicker1 = kicker1-1
            else:
                score= score-2744
            thepair= thepair-1
    
    #***********#
    # high card #
    #***********#
    highcardlist = sorted([c1,c2,c3,c4,c5])
    
    #highcard1 is the smallest highcard5 is the biggest
    highcard1 = highcardlist[0]
    highcard2 = highcardlist[1]
    highcard3 = highcardlist[2]
    highcard4 = highcardlist[3]
    highcard5 = highcardlist[4]
    
    hc1 = 14
    hc2 = 14
    hc3 = 14
    hc4 = 14
    hc5 = 14
    score=537824
            
    #first kicker
    while hc5>1:
        if highcard5 == hc5:
            #second kicker
            while hc4>1:
                if highcard4 == hc4:
                    #third kicker
                    while hc3>1:
                        if highcard3 ==hc3:
                            #fourth kicker
                            while hc2>1:
                                if highcard2 == hc2:
                                    #fifth kicker
                                    while hc1>1:
                                        if highcard1 == hc1:
                                            return score
                                        score = score -1
                                        hc1 = hc1-1                        
                                else:
                                    score = score -14
                                hc2 = hc2-1                  
                        else:
                            score = score-196
                        hc3 = hc3-1
                else:
                    score = score -2744
                hc4 = hc4-1
        else:
            score= score-38416
        hc5= hc5-1
        
        
def calculator(inputcard):
    '''converts card values that is easier for methods to execute'''  
    if inputcard %13 == 1:
        return 14
    if inputcard %13 == 0:
        return 13
    if inputcard %13 == 12:
        return 12
    if inputcard %13 == 11:
        return 11
    if inputcard %13 == 10:
        return 10
    if inputcard %13 == 9:
        return 9
    if inputcard %13 == 8:
        return 8
    if inputcard %13 == 7:
        return 7
    if inputcard %13 == 6:
        return 6
    if inputcard %13 == 5:
        return 5
    if inputcard %13 == 4:
        return 4
    if inputcard %13 == 3:
        return 3
    if inputcard %13 == 2:
        return 2
    

def greeting():
    print 'Welcome to Texas Holdem Death Match'
    
main()