import webbrowser
import os
from twitch import TwitchClient
from subprocess import Popen
import tkinter
from tkinter import *

client = TwitchClient(client_id=)#Need to grab twitch client ID
streams = client.streams.get_live_streams(game='warframe',limit=100)#Change this number to change the amount of streamers the twitch API pulls
checkList = ['!drop' , 'achievement']


#credit to @jancodes for the idea


def multiTwitch(myList):
    Popen('taskkill /F /IM chrome.exe', shell=True)#Can change "chrome" to any other browser, currently script opens up your defualt browser
    #Note this will close all instances of what ever browser is put 
    window.after(2000)
    #multitwitch doesn't allow for more than 25 streams open at once
    #Set my limit to 20 to reduce cpu usage for each multitwitch tab
    while len(myList) > 20:
        url = 'http://multitwitch.tv/'
        for x in range(20):
            url = url + (myList[0] + '/')
            myList.pop(0)
        webbrowser.open_new(url)
        window.after(120000)#number in ms, currently set to 2 minute intervals between opening each multitwitch tab to allow streams to load
    url = 'http://multitwitch.tv/'
    for streamers in myList:
        url = url + (streamers + '/')
    webbrowser.open_new(url)

    
        
def warframe():
    streamerID=[]
    counter = 0
    while counter < (len(streams)-1):
        tester = str.lower((streams[counter]['channel']['status']))
        if any(x in tester for x in checkList):
            if (streams[counter]['stream_type']) == 'live':
                if (streams[counter]['channel']['partner']) == False:
                    if (streams[counter]['viewers']) >= 15: #Number of viewers stream must have to be opened up if they aren't partnered
                        streamerID.append(streams[counter]['channel']['name'])
                else:
                    streamerID.append(streams[counter]['channel']['name'])
        counter = counter + 1
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
window.title("Warframe Stream Drops")


startButton = Button(window, text= "Start", command=Drops, bg='green', fg='black')
stopButton = Button(window, text="Stop", command=End, bg='red', fg='black')
stopButton.config(state='disabled')    
stopButton.pack(side=LEFT, fill=BOTH,expand=1)
startButton.pack(side=LEFT, fill=BOTH,expand=1)



window.geometry('300x100')
window.mainloop()


