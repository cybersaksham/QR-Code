from tkinter import *


class GUI(Tk):
    def __init__(self, title="Window", icon=None, width=200,
                 height=200, bg="white", resizableX=0, resizableY=0):
        super().__init__()
        self.title(title)
        self.iconbitmap(icon)
        self.geometry(f"{width}x{height}")
        self.config(bg=bg)
        self.resizable(resizableX, resizableY)

    def start(self):
        self.mainloop()

    def stop(self):
        self.destroy()


def showQR(filename):
    from PIL import ImageTk, Image
    img = ImageTk.PhotoImage(Image.open(filename))
    qr_img = Label(root, image=img, width=350, height=380, bg=BACKGROUND)
    qr_img.photo = img
    qr_img.grid(row=2, column=0, columnspan=3, padx=10, pady=5)


def generateQR():
    from tkinter.filedialog import asksaveasfilename
    filename = asksaveasfilename(title="Save QR", initialfile="qr.png",
                                 filetypes=(
                                     ("PNG Images", "*.png"),
                                     ("JPG Images", "*.jpg"),
                                     ("ALL Files", "*.*")
                                 ),
                                 defaultextension=".png")
    if filename != "":
        import pyqrcode
        url = pyqrcode.create(url_str.get())
        url.png(filename, scale=8)
        showQR(filename)


if __name__ == '__main__':
    # Global Variables
    BACKGROUND = "#FFFFFF"
    ICON = "icon.ico"

    # Making Window
    root = GUI("QR Generator", icon=ICON, width=385, height=450, bg=BACKGROUND)

    # Window Design
    url_label = Label(root, text="Enter URL", bg=BACKGROUND)
    url_str = StringVar()
    url_entry = Entry(root, textvariable=url_str, width=50)
    submit_btn = Button(root, text="Generate", command=generateQR)
    url_label.grid(row=0, column=0, padx=11, pady=5)
    url_entry.grid(row=0, column=1, columnspan=3)
    submit_btn.grid(row=1, column=1, pady=5, columnspan=3)

    # Starting Window
    root.start()
