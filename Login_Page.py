from database_01 import MyDB

db = MyDB()
db.create_table()

from tkinter import *
from datetime import datetime
from tkinter import messagebox

from database_01 import MyDB

db = MyDB()
db.create_table()


class Window:
    def __init__(self, title, width=500, height=350, resizeable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(resizeable[0], resizeable[1])

        self.full_name = StringVar()
        self.username = StringVar()
        self.email = StringVar()
        self.password = StringVar()

        self.main_frame = Frame(self.root)
        self.start_reg_btn = Button(self.main_frame, text="Ro'yxatdan o'tish", bg="#56ff9c", width=20,
                                    command=self.call_reg_window)
        self.start_log_btn = Button(self.main_frame, text="Login", bg="#0B5ED7", width=20)

    def draw_widgets(self):
        self.main_frame.pack()
        self.start_reg_btn.pack(expand=True, ipady=20, pady=20)
        self.start_log_btn.pack(expand=True, ipady=20, pady=20)

    def reg_draw_widgets(self):
        if len(self.root.winfo_children()) == 2:
            self.label = Label(self.reg_window, text="Ro'yxatdan o'tish", width=45, font=(15,))

            self.f_label1 = Label(self.reg_window, text="F.I.O")
            self.f_entry1 = Entry(self.reg_window, width=30, textvariable=self.full_name)

            self.f_label2 = Label(self.reg_window, text="Username")
            self.f_entry2 = Entry(self.reg_window, width=30, textvariable=self.username)

            self.f_label3 = Label(self.reg_window, text="Email")
            self.f_entry3 = Entry(self.reg_window, width=30, textvariable=self.email)

            self.f_label4 = Label(self.reg_window, text="Password")
            self.f_entry4 = Entry(self.reg_window, width=30, show="*", textvariable=self.password)

            self.submit = Button(self.reg_window, fg="#fff", bg="#9225f6", text="Jo'natish", height=2, width=10,
                                 command=self.reg_btn)
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
        else:
            self.reg_window.destroy()

    def log_draw_widgets(self):
        if len(self.root.winfo_children()) == 2:
            self.label = Label(self.reg_window, text="Ro'yxatdan o'tish", width=45, font=(15,))

            self.f_label3 = Label(self.reg_window, text="Email")
            self.f_entry3 = Entry(self.reg_window, width=30, textvariable=self.email)

            self.f_label4 = Label(self.reg_window, text="Password")
            self.f_entry4 = Entry(self.reg_window, width=30, show="*", textvariable=self.password)

            self.submit = Button(self.reg_window, fg="#fff", bg="#9225f6", text="Jo'natish", height=2, width=10,
                                 command=self.reg_btn)
            self.label.grid()

            self.f_label3.grid()
            self.f_entry3.grid()

            self.f_label4.grid()
            self.f_entry4.grid()

            self.submit.grid()
        else:
            self.reg_window.destroy()

    def reg_btn(self):
        now_date = datetime.now().strftime("%Y/%M/%d %H:%m")
        title, message = self.validated_method(email=self.email.get(), password=self.password.get())
        if type(title) is bool:
            db.insert_method(
                full_name=self.full_name.get(),
                username=self.username.get(),
                password=self.password.get(),
                email=self.email.get(),
                date=now_date,
            )

            messagebox.showinfo(title="Tabriklaymiz", message="Siz ro'yxatdan o'tingiz!")
            for i in range(1, 5):
                eval(f"self.f_entry{i}.delete(0, END)")
        else:
            messagebox.showerror(title=title, message=message)

    def validated_method(self, **kwargs):
        if not kwargs['email'].endswith("@gmail.com") and len(kwargs['password']) < 8:
            return "Error", "Email va Password xato"

        if len(kwargs['password']) < 8:
            return "Error Password", "Password 8 ta simvoldan ko'p bo'lishi kerak!"

        elif not kwargs['email'].endswith("@gmail.com"):
            return "Error Email", "Email xato"

        return True, True

    def call_reg_window(self):
        self.reg_window = Toplevel()
        self.reg_draw_widgets()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()


app = Window('Ro\'yxatdan o\'tish')
app.run()
