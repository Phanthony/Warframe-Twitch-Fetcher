import webbrowser
import os
from twitch import TwitchClient
from subprocess import Popen
import tkinter
from tkinter import *

client = TwitchClient(client_id='2l7nb587j3r4r5ewwuyjq34vocq03r')
streams = client.streams.get_live_streams(game='warframe',limit=100)
checkList = ['!drop' , 'achievement']

def multiTwitch(myList):
    Popen('taskkill /F /IM chrome.exe', shell=True)
    window.after(2000)
    #multitwitch doesn't allow for more than 20 streams open at once
    while len(myList) > 20:
        url = 'http://multitwitch.tv/'
        for x in range(20):
            url = url + (myList[0] + '/')
            myList.pop(0)
        webbrowser.open_new(url)
        window.after(120000)
        #print(url)
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
                    if (streams[counter]['viewers']) >= 15:
                        streamerID.append(streams[counter]['channel']['name'])
                else:
                    streamerID.append(streams[counter]['channel']['name'])
        counter = counter + 1
    multiTwitch(streamerID)
    return ("Finished")

def Drops():
    global test
    global startButton
    global stopButton
    startButton.config(state='disabled')
    stopButton.config(state='normal')
    warframe()
    test = window.after(12000000, Drops)
    test
        
def End():
    global startButton
    global stopButton    
    global test
    startButton.config(state='normal')
    stopButton.config(state='disabled')    
    window.after_cancel(test)
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


