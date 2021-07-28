from tkinter import *
from variables import *


def showQR(filename, gen_win):
    from PIL import ImageTk, Image
    img = ImageTk.PhotoImage(Image.open(filename))
    qr_img = Label(gen_win, image=img, width=350, height=380, bg=BACKGROUND)
    qr_img.photo = img
    qr_img.grid(row=2, column=0, columnspan=3, padx=10, pady=5)


def generateQR(gen_win):
    from tkinter.filedialog import asksaveasfilename
    import tkinter.messagebox as tmsg
    filename = asksaveasfilename(title="Save QR", initialfile="qr.png",
                                 filetypes=(
                                     ("PNG Images", "*.png"),
                                     ("JPG Images", "*.jpg"),
                                     ("ALL Files", "*.*")
                                 ),
                                 defaultextension=".png")
    if filename != "":
        try:
            import pyqrcode
            url = pyqrcode.create(url_str.get())
            url.png(filename, scale=8)
            showQR(filename, gen_win)
        except:
            tmsg.showerror(title="Error", message="In-appropriate File")


def start(gen_win):
    global url_str

    # Window Design
    url_label = Label(gen_win, text="Enter URL", bg=BACKGROUND)
    url_str = StringVar()
    url_entry = Entry(gen_win, textvariable=url_str, width=50)
    submit_btn = Button(gen_win, text="Generate", command=lambda: generateQR(gen_win))
    url_label.grid(row=0, column=0, padx=11, pady=5)
    url_entry.grid(row=0, column=1, columnspan=3)
    submit_btn.grid(row=1, column=1, pady=5, columnspan=3)
