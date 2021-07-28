from tkinter import *
import cv2
from variables import *


def copyData(data):
    win = Tk()
    win.withdraw()
    win.clipboard_clear()
    win.clipboard_append(data)


def showQR(scan_win, data):
    qr_data = Label(scan_win, bg=BACKGROUND, width=35)
    copy_btn = Button(scan_win, text="Copy", state=DISABLED, command=lambda: copyData(data))
    if data is not None and data != "":
        qr_data.config(text=data)
        copy_btn.config(state=ACTIVE)
    else:
        qr_data.config(text="Data not found")
        copy_btn.config(state=DISABLED)
    qr_data.grid(row=3, column=0, pady=10)
    copy_btn.grid(row=4, column=0, pady=2, padx=45)


def detect(img):
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)
    if bbox is not None:
        return data
    else:
        return None


def camThd(scan_win):
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cap.read()
        try:
            data, bbox, _ = detector.detectAndDecode(img)
            if bbox is not None:
                if data:
                    showQR(scan_win, data)
                    break
        finally:
            cv2.imshow("img", img)
        if cv2.waitKey(1) == ord("q"):
            break
    try:
        cap.release()
        cv2.destroyAllWindows()
    finally:
        return


def camera(scan_win):
    from threading import Thread
    t1 = Thread(target=camThd, args=[scan_win])
    t1.daemon = 1
    t1.start()


def image(scan_win):
    from tkinter.filedialog import askopenfilename
    import tkinter.messagebox as tmsg
    filename = askopenfilename(title="Open Image",
                               filetypes=(
                                   ("PNG Images", "*.png"),
                                   ("JPG Images", "*.jpg"),
                                   ("ALL Files", "*.*")
                               ),
                               defaultextension=".png")
    if filename != "":
        try:
            img = cv2.imread(filename)
            data = detect(img)
            showQR(scan_win, data)
        except:
            tmsg.showerror(title="Error", message="In-appropriate File")


def start(scan_win):
    # Window Design
    cam_btn = Button(scan_win, text="Camera", width=20, command=lambda: camera(scan_win))
    img_btn = Button(scan_win, text="Image", width=20, command=lambda: image(scan_win))
    cam_btn.grid(row=1, column=0, pady=10, padx=45)
    img_btn.grid(row=2, column=0, pady=10, padx=45)
