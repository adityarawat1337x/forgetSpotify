from bs4 import BeautifulSoup
import requests
import re
from msvcrt import getch
from time import time
import vlc
import pafy
from os import system as sys
#from googleapiclient.discovery import build
from func_timeout import func_timeout
from func_timeout.exceptions import FunctionTimedOut
from multiprocessing import Process

# hwnd = win32gui.GetForegroundWindow()
# win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, -5, -25, 600, 70, 0)

# apiKey = "google api key for youtube"

# def download(audio):
#    audio.download(filepath="tempMUSIC/")


key = 13


def getKey():
    global key
    key = ord(getch())


if __name__ == "__main__":
    while True:
        sys('cls||clear')
        query = "https://www.youtube.com/results?search_query=" + \
            input("\t\tMUzIK\n\n   Song: ").replace(" ", "+") + "+lyrics"
        print("\n\t    Searching..")
        data = requests.get(query)
        soup = BeautifulSoup(data.text, 'html.parser')
        temp = re.search(
            ',"title":{"runs":\[{"text":(.*?){"url":"\/watch(.*?)",', str(soup))
        videoUrl = "https://www.youtube.com/watch" + str(temp.group(2))
        # retrieving video link
        # youtube = build('youtube', 'v3', developerKey=apiKey)
        # request = youtube.search().list(q=query, part='snippet', type='video')
        # result = request.execute()
        # Id = result['items'][0]['id']['videoId']

        # videoUrl = "https://www.youtube.com/watch?v=" + Id
        # pafy instance
        video = pafy.new(videoUrl)
        song = video.getbestaudio()
        videoName = str(video.title).partition(' |')[0]
        start = time()
        # player start
        while True:
            pausePLay = True
            player = vlc.MediaPlayer(song.url)
            state = 'Playing'
            player.play()
            key = 97
            while player.is_playing:
                try:
                    sys('cls||clear')
                    elapsed = time() - start
                    print(
                        f"\t\tMUzIK\n\n   {state} : {videoName}")
                    if(pausePLay):
                        try:
                            target = func_timeout(
                                video.length - player.get_time()/1000, getKey)
                        except FunctionTimedOut:
                            break
                        except:
                            pass
                    else:
                        key = ord(getch())
                    if(key == 32 and state == "Playing"):
                        player.pause()
                        state = "Paused"
                        pausePLay = False
                    elif(key == 32):
                        player.play()
                        state = "Playing"
                        pausePLay = False
                    elif(key == 8):
                        player.stop()
                        exit(0)
                    elif(key == 13 or key == 97):
                        player.stop()
                        break
                except:
                    player.stop()
                    break
            if(key == 13):
                player.stop()
                break
            player.stop()
