from tkinter import *
from tkinter import messagebox
import mysql.connector

# ================= COLORS =================
bg_color = "#0b2c4d"
entry_bg = "#3d5a80"
btn_color = "#ff5c5c"

# ================= ROOT =================
root = Tk()
root.title("Login System")
root.geometry("800x500")
root.config(bg=bg_color)
root.resizable(False, False)

# ================= GLOBAL =================
trial_no = 0
show_password = False

# ================= FUNCTIONS =================
def toggle_password():
    global show_password
    if show_password:
        code.config(show="*")
        eye_btn.config(text="👁")
        show_password = False
    else:
        code.config(show="")
        eye_btn.config(text="🙈")
        show_password = True


def trial():
    global trial_no
    trial_no += 1

    if trial_no >= 3:
        messagebox.showwarning("Blocked", "Too many failed attempts!")
        root.destroy()


def loginuser():
    username = user.get()
    password = code.get()

    # Empty check
    if username == "" or username == "UserID" or password == "" or password == "Password":
        messagebox.showerror("Error", "Enter username and password!")
        return

    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="studentregisteration"   # ⚠ match your DB exactly
        )

        mycursor = mydb.cursor()

        query = "SELECT * FROM login WHERE username=%s AND Password=%s"
        mycursor.execute(query, (username, password))
        result = mycursor.fetchone()

        if result is None:
            messagebox.showerror("Invalid", "Wrong username or password!")
            trial()
        else:
            messagebox.showinfo("Success", "Login Successful!")
            root.destroy()

    except Exception as e:
        messagebox.showerror("DB Error", str(e))


# ================= MAIN FRAME =================
frame = Frame(root, bg=bg_color)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# ================= USER FIELD =================
user_frame = Frame(frame, bg=entry_bg)
user_frame.grid(row=0, column=0, pady=15)

user = Entry(user_frame,
             font=('Arial', 14),
             bg=entry_bg,
             fg='white',
             bd=0,
             insertbackground='white')

user.insert(0, "UserID")
user.place(x=10, y=5, width=260, height=30)

user_frame.config(width=300, height=40)

# ================= PASSWORD FIELD =================
pass_frame = Frame(frame, bg=entry_bg)
pass_frame.grid(row=1, column=0, pady=15)

code = Entry(pass_frame,
             font=('Arial', 14),
             bg=entry_bg,
             fg='white',
             bd=0,
             insertbackground='white',
             show="*")

code.insert(0, "Password")
code.place(x=10, y=5, width=230, height=30)

pass_frame.config(width=300, height=40)

# Eye button (perfect alignment)
eye_btn = Button(pass_frame,
                 text="👁",
                 bg=entry_bg,
                 fg="white",
                 bd=0,
                 cursor="hand2",
                 command=toggle_password)

eye_btn.place(x=260, y=8)

# ================= LOGIN BUTTON =================
login_btn = Button(root,
                   text="LOGIN",
                   font=('Arial', 14, 'bold'),
                   bg=btn_color,
                   fg="white",
                   bd=0,
                   activebackground="#ff3b3b",
                   cursor="hand2",
                   command=loginuser)

login_btn.place(relx=0.5, rely=0.7, anchor=CENTER, width=200, height=45)

# ================= RUN =================
root.mainloop()
