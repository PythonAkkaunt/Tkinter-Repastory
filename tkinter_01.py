from datetime import datetime
from tkinter import *
from tkinter import messagebox

from database_01 import MyDB

db = MyDB()
db.create_table()


class MyApp:
    def __init__(self, title, width=500, height=500, resiazible=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resiazible[0], resiazible[1])

        self.fullname = StringVar()
        self.username = StringVar()
        self.email = StringVar()
        self.password = StringVar()

        self.label = Label(self.root, text="Ro'yhatdan o'tish", width=70)

        self.f_label1 = Label(self.root, text="F.I.O", font=15)
        self.f_entry1 = Entry(self.root, width=30, textvariable=self.fullname, font=15)

        self.f_label2 = Label(self.root, text="username", font=15)
        self.f_entry2 = Entry(self.root, width=30, textvariable=self.username, font=15)

        self.f_label3 = Label(self.root, text="Email", font=15)
        self.f_entry3 = Entry(self.root, width=30, textvariable=self.email, font=15)

        self.f_label4 = Label(self.root, text="Password", font=15)
        self.f_entry4 = Entry(self.root, width=30, show='*', textvariable=self.password, font=15)

        self.submit = Button(self.root, bg="blue", fg="white", text="Jo'natish", height=2, width=10,
                             command=self.reg_btn, font=15)

    def draw_widgets(self):

        self.label.grid()

        self.f_label1.grid()
        self.f_entry1.grid()

        self.f_label2.grid()
        self.f_entry2.grid()

        self.f_label3.grid()
        self.f_entry3.grid()

        self.f_label4.grid()
        self.f_entry4.grid()

        self.submit.grid()

    def reg_btn(self):
        now_date = datetime.now().strftime("%Y.%M.%d %H:%m")
        title, message = self.tekshiruv(email=self.email.get(), password=self.password.get())
        if type(title) is bool:
            db.insert_method(
                fullname=self.fullname.get(),
                username=self.username.get(),
                password=self.password.get(),
                email=self.email.get(),
                date=now_date,
            )
            for i in range(1, 5):
                eval(f"self.f_entry{i}.delete(0, END)")
            messagebox.showinfo("Registartsiya", "Registartsiyadan O'tdingiz")
        else:
            messagebox.showerror(title=title, message=message)

    def tekshiruv(self, **kwargs):
        if not kwargs['email'].endswith("@gmail.com") and len(kwargs['password']) < 8:
            return "Error", "Email and Password Error"

        if len(kwargs['password']) < 8:
            return "Error password", "Password 8 ta emas !"
        elif not kwargs['email'].endswith("@gmail.com"):
            return "Error Email", "Email xato"

        return True, True

    def run(self):
        self.draw_widgets()
        self.root.mainloop()


window = MyApp("Ro'yxatdan o'tish", 500, 500)
window.run()
