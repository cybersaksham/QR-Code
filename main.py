from tkinter import *
from threading import Thread
from gui import *
from variables import *
import generate
import scan


def scanThread():
    scan_win = NewWindow(root, title="QR Scanner", icon=ICON,
                         width=250, height=175, bg=BACKGROUND, resizableX=1, resizableY=1)
    scan.start(scan_win)


def scanQR():
    t1 = Thread(target=scanThread)
    t1.daemon = 1
    t1.start()


def genThread():
    gen_win = NewWindow(root, title="QR Generator", icon=ICON,
                        width=385, height=450, bg=BACKGROUND)
    generate.start(gen_win)


def generateQR():
    t1 = Thread(target=genThread)
    t1.daemon = 1
    t1.start()


if __name__ == '__main__':
    # Making Window
    root = GUI("QR Code", icon=ICON, width=250, height=100, bg=BACKGROUND)

    # Window Design
    scan_btn = Button(root, text="Scan", width=20, command=scanQR)
    gen_btn = Button(root, text="Generate", width=20, command=generateQR)
    scan_btn.pack(pady=10)
    gen_btn.pack(pady=10)

    # Starting Window
    root.start()
