import tkinter as tk
import mysql.connector


def submit_act():
    user = Username.get()
    pass_w = password.get()

    print(f"The name entered by you is {user}")

    login_to_db(user, pass_w)


def login_to_db(user, pass_w):
    # If password is entered by the
    # user
    if pass_w:
        db = mysql.connector.connect(host="localhost",
                                     user=user,
                                     password=pass_w,
                                     db="world")
        cursor = db.cursor()

    # If no password is entered by the
    # user
    else:
        db = mysql.connector.connect(host="localhost",
                                     user=user,
                                     db="sys")
        cursor = db.cursor()

    # A Table in the database
    save_query = "select * from city"

    try:
        cursor.execute(save_query)
        my_result = cursor.fetchall()

        # Printing the result of the
        # query
        for x in my_result:
            print(x)
        print("Query Executed successfully")

    except Exception:
        db.rollback()
        print("Error occurred")
        raise


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
