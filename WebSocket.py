import socket , os , webbrowser , threading , time , pygame
from pynput.keyboard import Key, Controller
#try and switch playsound for pygame
keyboard = Controller()
get_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
get_ip.connect(("8.8.8.8", 80))
ip_address = (get_ip.getsockname()[0])
print('Your IP Address is ' + ip_address)
get_ip.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#this helps to stop the socket and open it for my purpose sometimes a socket can be left open forever and we dont want to be wasteful
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#opening the socket
s.bind((ip_address, 9994))
print("Your IP is " + ip_address)
print("Server is up and running")
s.settimeout(1.0)
#allows for 2 devices to connect 
s.listen(2)
#just for me to keep count of all the buttons i use 
preview = 0
Quit = 0
zoom = 0
whatsapp = 0
discord = 0
zoommute = 0
minimise = 0
zoomvideo = 0
meet = 0
houseparty = 0
misc = 0
youtube = 0
spotify = 0
enter = 0
count = 0
#thread for sound effects
class SoundEffect(threading.Thread):
    def __init__(self, soundName):
        threading.Thread.__init__(self)
        self.soundName = soundName
    def run(self):
        if self.soundName != "stop":
            pygame.init()
            pygame.mixer.music.load(self.soundName)
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.stop()
#class to execute commands 
class myThread (threading.Thread) :
    def __init__(self, Command):
        threading.Thread.__init__(self)
        self.Command = Command
    def run(self):
        global preview 
        global Quit 
        global zoom 
        global whatsapp 
        global discord 
        global zoommute 
        global minimise 
        global zoomvideo 
        global meet 
        global houseparty 
        global misc
        global youtube 
        global spotify 
        global enter 
        if command == "spotify":
                os.system(r"C:\Users\amogh\AppData\Roaming\Spotify\Spotify.exe")
                spotify += 1
        elif command == "whatsapp":
            os.system(r"C:\Users\amogh\AppData\Local\WhatsApp\WhatsApp.exe")
            whatsapp += 1
        elif command == "zoom":
            os.system(r"C:\Users\amogh\AppData\Roaming\Zoom\bin\Zoom.exe")
            zoom += 1
        elif command == "zoom-mute":
            os.system(r"C:\Users\amogh\AppData\Roaming\Zoom\bin\Zoom.exe")
            time.sleep(0.1)
            with keyboard.pressed(Key.ctrl):
                with keyboard.pressed(Key.shift):
                    keyboard.press('a')
                    keyboard.release('a')
            zoommute += 1
        elif command == "youtube":
            webbrowser.open_new_tab("https://www.youtube.com/?feature=ytca")
            youtube += 1
        elif command == "enter":
            time.sleep(30)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            enter += 1
        elif command == "quit":
            with keyboard.pressed(Key.alt):
                keyboard.press(Key.f4)
                keyboard.release(Key.f4)
            Quit +=1
        elif command == "minimise":
            with keyboard.pressed(Key.cmd):
                keyboard.press(Key.down)
                keyboard.release(Key.down)
            minimise += 1
        #editable button here
        elif command == "misc":
            pass
        elif command == "zoom-video":
            os.system("open /Applications/zoom.us.app")
            with keyboard.pressed(Key.ctrl):
                with keyboard.pressed(Key.shift):
                    keyboard.press('v')
                    keyboard.release('v')
        elif command == "meet":
            os.system(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            time.sleep(0.1)
            with keyboard.pressed(Key.ctrl):
                keyboard.press('d')
                keyboard.release('d')
            meet += 1
        elif command == "discord":
            os.system(r"C:\Users\amogh\AppData\Local\Discord\app-1.0.9001\Discord.exe")
            time.sleep(0.3)
            with keyboard.pressed(Key.ctrl):
                with keyboard.pressed(Key.shift):
                    keyboard.press('m')
                    keyboard.release('m')
            discord += 1
        #soundboard stuff
        elif command == "build-up":
            SoundEffect(soundName= "Sound/build-up.mp3").start()
        elif command == "drop":
            SoundEffect(soundName="Sound/drop.mp3").start()
        elif self.Command == "crowd-cheer":
            SoundEffect(soundName="Sound/cheer.mp3").start()
        elif self.Command == "stop":
            SoundEffect(soundName="stop").start()
        elif self.Command == "nani":
            SoundEffect(soundName="Sound/nani.mp3").start()
        elif self.Command == "next-time":
            SoundEffect(soundName="Sound/next-time.mp3").start()
        #misc sound effect
        elif self.Command == "misc-sound":
            pass
        elif self.Command == "crickets":
            SoundEffect(soundName="Sound/crickets.mp3").start()
        elif self.Command == "ask-if-fine":
            SoundEffect(soundName="Sound/ask-if-fine.mp3").start()
        elif self.Command == "drumroll":
            SoundEffect(soundName="Sound/drumroll.mp3").start()
        elif self.Command == "big-l":
            SoundEffect(soundName="Sound/big-l.mp3").start()

#detecting messages
while True:
    try:
        clientsocket,addr=s.accept()
        while True:
            message = clientsocket.recv(1024)
            print(message.decode("utf-8"))
            command = message.decode("utf-8")
            thread = myThread(message.decode("utf-8"))
            thread.start()
            count += 1
            if not message:
                break
            elif socket.error:
                clientsocket,addr=s.accept()
    except socket.timeout:
        pass
    except KeyboardInterrupt:
        print("\nServer has shut down")
        if count > 0:
            print("Here is a record of the buttons you used:")
            print("Total:" + str(count))
        if houseparty > 0 :
            print("Houseparty:" + str(houseparty))
        if zoom > 0:
            print("Zoom:" + str(zoom))
        if zoommute > 0:
            print("Zoom Mute:" + str(zoommute))
        if zoomvideo > 0:
            print("Zoom Video:" + str(zoomvideo))
        if meet > 0:
            print("Meet:" + str(meet))
        if Quit > 0:
            print("Quit:" + str(Quit))
        if preview > 0:
            print("Preview:" + str(preview))
        if whatsapp > 0:
            print("WhatsApp:" + str(whatsapp))
        if discord > 0:
            print("Discord:" + str(discord))
        if minimise > 0:
            print("Minimise:" + str(minimise))
        if youtube > 0:
            print("YouTube:" + str(youtube))
        if spotify > 0:
            print("Spotify:" + str(spotify))
        if enter > 0:
            print("Enter:" + str(enter))
        if misc > 0:
            print("Misc:" + str(misc))
        if count == 0:
            print("Why did you code all this shit if you don't want to fucking use it dumbass")
        break
