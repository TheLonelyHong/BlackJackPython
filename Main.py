import tkinter as tk
from Functions import components as Com
from Functions import gameplay as game

# Defining windows size and title
window = tk.Tk()
window.geometry("600x450")
window.title("Black Jack With PC")

frame_A = Com.container(50 , 5 , 5)
announcementLabel = Com.label(frame_A , "Welcome to BlackJack" , (30 , 1) , "#ACD6FF" , (180,15))
createdAnnouncement = announcementLabel.create()


frame_C = Com.container(100 , 5 , 5)
frame_D = Com.container(100 , 5 , 5)
playerLabel = Com.label(frame_C , "Player: " , (30 , 1) , "#ACD6FF" , (0 , 0) )
botLabel = Com.label(frame_D , "Bot: " , (30 , 1) , "#ACD6FF" , (0 , 0))
createdPlayerLabel = playerLabel.create()
botCreatedLabel = botLabel.create()



frame_B = Com.container(100 , 5 , 5)

#Controls
StartButton = Com.button(frame_B , "Start game" , (10 , 1) , "#ACD6FF" , (10 , 20))
AddCardsButton = Com.button(frame_B , "Add Cards" , (10 ,1) , "#ACD6FF" , (100 , 20))
PassTurnButton = Com.button(frame_B , "Pass turn" , (10 ,1) , "#ACD6FF" , (200 , 20))
ResetButton = Com.button(frame_B , "Reset" , (10 ,1) , "#ACD6FF" , (300 , 20))

StartButton.create(lambda:game.startGame(createdAnnouncement , frame_C))
AddCardsButton.create(lambda:game.addCards(createdAnnouncement , frame_C))
PassTurnButton.create(lambda:game.turnPassed(createdAnnouncement , frame_D))
ResetButton.create(lambda:game.resetTheGame(createdAnnouncement))



window.resizable(False , False)
window.mainloop()