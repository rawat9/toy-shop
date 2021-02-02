# ================================== TKINTER IMPORTS =========================================
import tkinter as tk
from tkinter import *
import tkinter.font as font
from PIL import ImageTk
from tkinter import messagebox as msg
# ============================================================================================
# =================================== FILE IMPORTS ===========================================
from Feature_01.F1_login import F1Feature
from Feature_02.F2_catalogue import F2Feature
# ==================================== OTHERS ================================================
import time
# ============================================================================================


class AAToys(tk.Tk):
    def __init__(self, *args, **kwargs):  # *args are to pass non-keyword arguments,whereas **kwargs are keyword argu
        tk.Tk.__init__(self, *args, **kwargs)   # initializing the inherited class

        master = tk.Frame(self)
        master.pack(side="top", fill="both", expand=True)
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        photo = ImageTk.PhotoImage(file="assets/images/toys_icon.ico")  # icon
        self.iconphoto(True, photo)

        self.frames = {}

        for F in (Home, LoginOrSignup, Catalogue):  # function to propagate through frames
            frame = F(master, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Home)

    def show_frame(self, cont):  # Another method, with self and an argument of cont for controller.
        frame = self.frames[cont]
        frame.tkraise()


class Home(tk.Frame):   # Home class, inheriting from tk.Frame.
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global img3  # global keyword allows to access the variable outside the class
        global img

        def close():
            response = msg.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                       icon=msg.WARNING)
            if response == 'yes':
                exit()
            else:
                pass

        self.canvas = Canvas(self, width=1200, height=620)  # Background Image(Home)
        self.canvas.pack(fill=BOTH, expand=True)
        img3 = ImageTk.PhotoImage(file="assets/images/background_img1.jpg")
        self.canvas.create_image(-100, 310, anchor=W, image=img3)

        img = PhotoImage(file="assets/images/AAT.png")  # AAT Logo on Home
        self.canvas.create_image(800, 160, anchor=W, image=img)

        button_font = font.Font(family='Helvetica', size='15', weight='bold')
        self.login = tk.Button(self, text='LOGIN / SIGN-UP', font=button_font, width=20, height=2,
                               command=lambda: controller.show_frame(LoginOrSignup))
        self.login.place(x=900, y=320)

        self.catalogue = tk.Button(self, text='CATALOGUE', font=button_font, width=20, height=2,
                                   command=lambda: controller.show_frame(Catalogue))
        self.catalogue.place(x=900, y=375)

        self.exitprogram = tk.Button(self, text='EXIT', font=button_font, width=20, height=2,
                                     command=close)
        self.exitprogram.place(x=900, y=430)

        self.statusbar = Label(self, text='PYTHON COURSE-WORK', relief=SUNKEN, anchor=CENTER)
        self.statusbar.pack(side=BOTTOM, fill=X)


class LoginOrSignup(tk.Frame):  # inherited from the parent class
    """
    F1 Feature
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        F1Feature(self)  # imported class from another file

        Button(self, text='Back', width=10, height=2, command=lambda: controller.show_frame(Home)).place(x=1150, y=30)


class Catalogue(tk.Frame):
    """
    F2 Feature
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        global logo

        # Logo
        logo = ImageTk.PhotoImage(file="assets/images/AATsmall.png")

        F2Feature(self)  # imported class from another file

        # clock on the toolbar
        def clock():
            hour = time.strftime("%I")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            am_pm = time.strftime("%p")

            clock_label.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
            clock_label.after(1000, clock)

        # Toolbar
        toolbar = PanedWindow(self, orient=HORIZONTAL, height=100, bd=2, width=1280, relief=FLAT, bg='white')
        toolbar.grid(row=0)

        image_label = tk.Label(toolbar, image=logo, bg='white', relief=FLAT)
        image_label.place(x=80, y=50, anchor=CENTER)

        logo_label = tk.Label(toolbar, text='Catalogue', bg='white', font=('Avenir', 40, 'bold'))
        logo_label.place(x=150, y=25)

        clock_label = tk.Label(toolbar, text='', font=('', 40), fg='white', bg='black')
        clock_label.place(x=500, y=25)
        clock()

        back_button = tk.Button(toolbar, text='Back', width=10, height=2,
                                command=lambda: controller.show_frame(Home))
        back_button.place(x=1140, y=30)


if __name__ == '__main__':
    root = AAToys()
    menu_bar = tk.Menu(root)  # Menu Bar
    message_menu = tk.Menu(menu_bar, tearoff=True)
    root.config(menu=menu_bar)
    root.title('All About Toys')
    root.geometry('1280x700+40+40')
    # root.attributes("-fullscreen", 1)   full screen mode
    root.mainloop()
