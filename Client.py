import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer

IP_ADDRESS = "127.0.0.1"
port = 8080
SERVER = None
BUFFER_SIZE = 4096

def setup():
    global port
    global IP_ADDRESS
    global SERVER
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, port))
    openChatWindow()

def openChatWindow():
    print("IP Messenger")
    window = Tk()
    window.title("Music Window")
    window.geometry("300x300")
    window.configure(bg = "LightSkyBlue")
    window.mainloop()

setup()