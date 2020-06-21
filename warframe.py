import webbrowser
import os
from twitch import Helix
from subprocess import Popen
import tkinter
from tkinter import *

client = Helix(client_id='', bearer_token='')#Need to grab twitch client ID and bearer token
count=20#Change this number to change the amount of streamers the twitch API pulls
game_name="warframe"
f=input("write game name : ")
while(len(f)>0):
    if client.game(name=f)==None:
        f=input("wrong name write game name : ")
    else:
        game_name=f
        break
game = client.game(name=game_name).id
print(game)
def check_for_streams():
    global streams
    streams = client.streams(game_id=game, first=count).users


#credit to @jancodes for the idea


def multiTwitch(myList):
    Popen('taskkill /F /IM chrome.exe', shell=True)#Can change "chrome" to any other browser, currently script opens up your defualt browser
    #Note this will close all instances of what ever browser is put 
    window.after(2000)
    #multitwitch doesn't allow for more than 25 streams open at once
    #Set my limit to 5 to reduce cpu usage for each multitwitch tab
    url = 'http://multitwitch.tv/'
    max=5
    if(len(myList)<5):
        max=len.myList
    for i in range(max):
        url = url + (myList[i] + '/')
    webbrowser.open_new(url)

    
        
def warframe():
    check_for_streams()
    streamerID=[]
    for i in range(count-1):
        try:
            a=next(streams)
        except StopIteration:
            break
        tester = str.lower(a[0].user_name)
        if (a[0].type) == 'live':
            if (a[1].broadcaster_type) != 'partner':
                if (a[0].viewer_count) >= 15: #Number of viewers stream must have to be opened up if they aren't partnered
                    streamerID.append(tester)
            else:
                streamerID.append(tester)
    multiTwitch(streamerID)
    return ("Finished")

def Drops():
    global repeater
    global startButton
    global stopButton
    startButton.config(state='disabled')
    stopButton.config(state='normal')
    warframe()
    repeater = window.after(12000000, Drops)#Currently set to 20 minute intervals before it checks for new streamers
    #This allows offline streams to be closed and then opens up new streams
    repeater
        
def End():
    global startButton
    global stopButton    
    global repeater
    startButton.config(state='normal')
    stopButton.config(state='disabled')    
    window.after_cancel(repeater)
    Popen('taskkill /F /IM chrome.exe', shell=True)
        

window = tkinter.Tk()
window.title(client.game(name=game_name).name +" Stream Drops")


startButton = Button(window, text= "Start", command=Drops, bg='green', fg='black')
stopButton = Button(window, text="Stop", command=End, bg='red', fg='black')
stopButton.config(state='disabled')    
stopButton.pack(side=LEFT, fill=BOTH,expand=1)
startButton.pack(side=LEFT, fill=BOTH,expand=1)



window.geometry('300x100')
window.mainloop()


