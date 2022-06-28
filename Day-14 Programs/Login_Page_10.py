import tkinter as tk
import mysql.connector


def submit_act():
    user_name = Username.get()
    pass_word = password.get()

    print(f"The name entered by you is {user_name} {pass_word}")

    log_to_db(user_name, pass_word)


def log_to_db(user, pass_w):
    if pass_w:
        db = mysql.connector.connect(host='localhost', database='Demo_1', user=user, password=pass_w)
        cursor = db.cursor()
    else:
        db = mysql.connector.connect(host="localhost", user=user, database=pass_w)
        cursor = db.cursor()
    Query = "select * from employee"
    cursor.execute(Query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    print("Query Executed successfully")


root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")

# Defining the first row
lbl_frst_row = tk.Label(root, text="Username -", )
lbl_frst_row.place(x=50, y=20)

Username = tk.Entry(root, width=35)
Username.place(x=150, y=20, width=100)

lbl_sec_row = tk.Label(root, text="Password -")
lbl_sec_row.place(x=50, y=50)

password = tk.Entry(root, width=35)
password.place(x=150, y=50, width=100)

submit_btn = tk.Button(root, text="Login", bg='blue', command=submit_act)
submit_btn.place(x=150, y=135, width=55)

root.mainloop()
