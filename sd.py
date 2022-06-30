#####################################################################################################
#                                                                                                   #
#    _____      _       _                  _____ _     _       _   _                       _ _ _    #
#  / ____|    (_)     (_)                / ____| |   (_)     | | | |                     | | (_)    #
# | (___  _ __ _ _ __  ___   ____ _ ___ | |    | |__  _ _ __ | |_| |__   __ _ _ __   __ _| | |_     #
# \___ \| '__| | '_ \| \ \ / / _` / __|| |    | '_ \| | '_ \| __| '_ \ / _` | '_ \ / _` | | | |     #
#  ____) | |  | | | | | |\ V / (_| \__ \| |____| | | | | | | | |_| | | | (_| | |_) | (_| | | | |    #
# |_____/|_|  |_|_| |_|_| \_/ \__,_|___/ \_____|_| |_|_|_| |_|\__|_| |_|\__,_| .__/ \__,_|_|_|_|    #
#                                    ______                                  | |                    #
#                                   |______|                                                        # #|_|                                                                                                #
# Author By Srinivas_chinthapalli                                                                   #
#####################################################################################################

from tkinter import *
import tkinter as tk
import pyautogui
from PIL import ImageTk, Image
import os

class shutdown_window():
    def __init__(self,master):
        width, height= pyautogui.size()
        self.editwindow=master
        self.editwindow.title("Editrecord")
        self.editwindow.wm_geometry("%dx%d+%d+%d" % (420,200,width/3,height/3))
        self.editwindow.resizable(False,False)
        top= tk.Canvas(self.editwindow, bg="#003399", height=50, width=416)
        top.place(x=0,y=0)
        top.create_text(100, 25, text="Turn off Computer", fill="white", font=('Helvetica 15 bold'))
        self.bottom= tk.Canvas(self.editwindow, bg="#003399", height=50, width=416)
        self.bottom.place(x=0,y=150)
        self.center= tk.Canvas(self.editwindow, bg="#80a1ed", height=100, width=416)
        self.center.place(x=0,y=50)
        res = ImageTk.PhotoImage(Image.open("stand.jpg"))
        self.standby=Button(self.editwindow,image=res,width=36,height=35,command=self.logout)
        self.standby.place(x=100,y=80)
        self.standby.configure(bg="#80a1ed",borderwidth=0)
        sh = ImageTk.PhotoImage(Image.open("turnoff.jpg"))
        self.r=Button(self.editwindow,image=sh,width=36,height=35,command=self.shutdown)
        self.r.place(x=200,y=80)
        self.r.configure(bg="#80a1ed",borderwidth=0)
        ress= ImageTk.PhotoImage(Image.open("restart.jpg"))
        self.restart=Button(self.editwindow,image=ress,width=36,height=35,command=self.restart)
        self.restart.place(x=300,y=80)
        self.restart.configure(bg="#80a1ed",borderwidth=0)
        self.txt("Stand By",100,80)
        self.txt("Turn Off",200,80)
        self.txt("Restart",300,80)
        self.shutdown=Button(self.editwindow,text="Cancel",command=self.quit)
        self.shutdown.place(x=350,y=165)
        self.editwindow.overrideredirect(True)
        self.bottom.create_text(100,30, text="Designed By Srinivas_chinthapalli", fill="white", font=('Helvetica 7 bold'))
        self.editwindow.mainloop()
    def shutdown(self):
        return os.system("shutdown /s /t 1")
        
    def restart(self):
        return os.system("shutdown /r /t 1")

    def logout(self):
        return os.system("shutdown -l")
    
    def txt(self,data,x,y):
        self.center.create_text(x+18, y+4, text=data, fill="white", font=('Helvetica 10 bold'))
    def quit(self):
        self.editwindow.quit()
            
root=tk.Tk()

shutdown_window(root)
        


