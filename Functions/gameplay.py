import random
from PIL import ImageTk as imgTK , Image as OpenImages
from tkinter import *


PLAYER_CARDS = []
BOT_CARDS = []
EARLY_GAME = True
MID_GAME = False
X_AXIS = 10
Y_AXIS = 20
CARDS_CONTAINER = []
PLAYER_CARDS_POINT = 0
BOT_CARDS_POINT = 0

POKER_CARDS = [
    {
        "card":"Functions\Cards\poker2.png",
        "value":2
    },
    {
        "card":"Functions\Cards\poker3.png",
        "value":3
    },
    {
        "card":"Functions\Cards\poker4.png",
        "value":4
    },
    {
        "card":"Functions\Cards\poker5.png",
        "value":5
    },
    {
        "card":"Functions\Cards\poker6.png",
        "value":6
    },
    {
        "card":"Functions\Cards\poker7.png",
        "value":7
    },
    {
        "card":"Functions\Cards\poker8.png",
        "value":8
    },
    {
        "card":"Functions\Cards\poker9.png",
        "value":9
    },
    {
        "card":"Functions\Cards\poker10.png",
        "value":10
    },
    {
        "card":"Functions\Cards\poker11.png",
        "value":10
    },
    {
        "card":"Functions\Cards\poker12.png",
        "value":10
    },
    {
        "card":"Functions\Cards\poker13.png",
        "value":10
    },
    {
        "card":"Functions\Cards\poker14.png",
        "value":1
    },
]

def imagePhoto(frame , cardName):
     
     global pokerContainer
     global X_AXIS

     img = OpenImages.open(cardName)
     img = img.resize((50 , 70) , OpenImages.ADAPTIVE)
     imgTest = imgTK.PhotoImage(img)

     pokerContainer = Label(
          master= frame,
          image= imgTest
     )

     pokerContainer.place(x = X_AXIS , y = Y_AXIS)
     pokerContainer.image = imgTest
     CARDS_CONTAINER.append(pokerContainer)
     X_AXIS += 70

def randomRangeNumber():
        return random.randrange(0 , 13)

def startGame(changeLabelText , frame):
        
        global EARLY_GAME
        global MID_GAME
        global PLAYER_CARDS_POINT
        
        if EARLY_GAME == True and MID_GAME == False:
            changeLabelText.config(text = "Game Started")
            cardOne = POKER_CARDS[randomRangeNumber()]
            cardTwo = POKER_CARDS[randomRangeNumber()]

            PLAYER_CARDS.append(cardOne)
            PLAYER_CARDS.append(cardTwo)

            
            for playerCards in PLAYER_CARDS:
                #print(playerCards)
                if playerCards["card"] == "BlackJack\Functions\Cards\poker14.png": playerCards["value"] = 11
                
           
            for card in PLAYER_CARDS:
                imagePhoto(frame , card["card"])
                PLAYER_CARDS_POINT += card["value"]

            EARLY_GAME = False
            MID_GAME = True



def addCards(changeTheLabel , frame):
    global EARLY_GAME
    global MID_GAME
    global PLAYER_CARDS_POINT

    if EARLY_GAME == False and MID_GAME == True:
        changeTheLabel.config(text = "Adding cards for player")

        if PLAYER_CARDS_POINT <= 21:
             cardOne = POKER_CARDS[randomRangeNumber()]
             PLAYER_CARDS.append(cardOne)
             PLAYER_CARDS_POINT += cardOne["value"]
             imagePhoto(frame , cardOne["card"])
        else:
             changeTheLabel.config(text = "You cannot add more cards")






def turnPassed(changeTheLabel , frame):
    global EARLY_GAME
    global MID_GAME
    global X_AXIS
    global BOT_CARDS_POINT

    if PLAYER_CARDS_POINT < 16:
         changeTheLabel.config(text = "Must be higher than 15 points")
    else:

        if EARLY_GAME == False and MID_GAME == True:
            changeTheLabel.config(text = "Turn passed to bot")
            X_AXIS = 10

            cardOne = POKER_CARDS[randomRangeNumber()]
            cardTwo = POKER_CARDS[randomRangeNumber()]
            BOT_CARDS.append(cardOne)
            BOT_CARDS.append(cardTwo)
            
            for card in BOT_CARDS:
                if card["card"] == "BlackJack\Functions\Cards\poker14.png" : 
                    card["value"] = 11
            
            for cardValue in BOT_CARDS:
                BOT_CARDS_POINT += cardValue["value"]

            while BOT_CARDS_POINT < 18:
                card = POKER_CARDS[randomRangeNumber()]
                BOT_CARDS.append(card)
                BOT_CARDS_POINT += card["value"]
            else:
                for card in BOT_CARDS:
                    imagePhoto(frame , card["card"])

                if BOT_CARDS_POINT > 21 and PLAYER_CARDS_POINT > 21:
                    changeTheLabel.config(text = "Bot won the game! Yea~")
                elif BOT_CARDS_POINT == 21:
                    changeTheLabel.config(text = "Bot won !")
                elif PLAYER_CARDS_POINT > 21 and BOT_CARDS_POINT <= 21:
                    changeTheLabel.config(text = "Bot won ! you lost !")
                elif PLAYER_CARDS_POINT == 21 and BOT_CARDS_POINT < 21:
                    changeTheLabel.config(text = "You won ! Bot lost !")
                elif PLAYER_CARDS_POINT == BOT_CARDS_POINT:
                    changeTheLabel.config(text = "It's a tie !")
                elif PLAYER_CARDS_POINT > BOT_CARDS_POINT:
                    changeTheLabel.config(text = "You won the game !")
                elif PLAYER_CARDS_POINT < BOT_CARDS_POINT and BOT_CARDS_POINT <= 21:
                    changeTheLabel.config(text = "Bot won the game !")
                else:
                    changeTheLabel.config(text = "You won the game ! Huuray")

            #At the end
            MID_GAME = False




def resetTheGame(changeLabelText):
    global EARLY_GAME
    global MID_GAME
    global pokerContainer
    global X_AXIS
    global PLAYER_CARDS_POINT
    global BOT_CARDS_POINT

    if EARLY_GAME == False and MID_GAME == False:

        for card in CARDS_CONTAINER:
             card.destroy()
        
        CARDS_CONTAINER.clear()
        PLAYER_CARDS.clear()
        BOT_CARDS.clear()
        changeLabelText.config(text = "Game resetted")
        X_AXIS = 10
        PLAYER_CARDS_POINT = 0
        BOT_CARDS_POINT = 0
        EARLY_GAME = True
        MID_GAME = False
