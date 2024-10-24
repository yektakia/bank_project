import sqlite3
from tkinter import Tk, Label, Button, Entry
from tkinter.ttk import Combobox

login_list = []


def create_login():
    for entry in login_list:
        entry.destory()
    login_list.clear()
    loging_form = Tk()
    loging_form.title("login")
    username_label = Label(loging_form, text="Username")
    username_label.grid(row=0, column=0, pady=10, padx=0, sticky="w")

    password_label = Label(loging_form, text="Password")
    password_label.grid(row=1, column=0, pady=10, padx=0, sticky="w")

    check_label = Label(loging_form, text="")
    check_label.grid(row=3, column=1)

    username_entry = Entry(loging_form, width=20)
    username_entry.grid(row=0, column=1)
    login_list.append(username_entry)

    password_entry = Entry(loging_form, width=20)
    password_entry.grid(row=1, column=1)
    login_list.append(password_entry)

    def user_name_list():

        username_list = []
        password_list = []
        with sqlite3.connect("bankdatabase1.db") as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
               SELECT username, 
                      password
               FROM User;
               """).fetchall()
            for username in data:
                username_list.append(username[0])
                password_list.append(username[1])
            # for i in range(0,4):
            if username_entry.get() in username_list and password_entry.get() in password_list:
                check_label.config(text="welcome", fg="green")
                loging_form.destroy()

            else:
                check_label.config(text="you are wrong", fg="red")

    submit_buttom = Button(loging_form, text="Submit", command=user_name_list)
    submit_buttom.grid(row=2, column=1, pady=10, padx=0, sticky="w")


create_login()

window = Tk()
window.title("Management bank account")


def add_new_account(id=None, first_name="", last_name="", nationalcode="", Account_number="", balance="", user_id="",
                    active=""):
    for entry in new_account_list:
        entry.destroy()
    new_account_list.clear()
    new_account = Tk()
    if not id:
        new_account.title("New account")
    else:
        new_account.title("update account")
    firstname_label = Label(new_account, text="First name")
    firstname_label.grid(row=1, column=1)

    lastname_label = Label(new_account, text="Last name")
    lastname_label.grid(row=1, column=2)

    nationalcode_label = Label(new_account, text="Nationalcode")
    nationalcode_label.grid(row=1, column=3)

    account_number_label = Label(new_account, text="Account number")
    account_number_label.grid(row=1, column=4)

    balance_label = Label(new_account, text="Balance")
    balance_label.grid(row=1, column=5)

    userinformation_label = Label(new_account, text="User Full name")
    userinformation_label.grid(row=1, column=6)

    status_label = Label(new_account, text="status")
    status_label.grid(row=1, column=7)

    entry_list = []

    for entry in entry_list:
        entry.destroy()
    entry_list.clear()

    first_name_entry = Entry(new_account, width=20)
    first_name_entry.grid(row=2, column=1)
    entry_list.append(first_name_entry)

    last_name_entry = Entry(new_account, width=20)
    last_name_entry.grid(row=2, column=2)
    entry_list.append(last_name_entry)

    nationalcode_entry = Entry(new_account, width=20)
    nationalcode_entry.grid(row=2, column=3)
    entry_list.append(nationalcode_entry)

    account_number_entry = Entry(new_account, width=20)
    account_number_entry.grid(row=2, column=4)
    entry_list.append(account_number_entry)

    balance_entry = Entry(new_account, width=20)
    balance_entry.grid(row=2, column=5)
    entry_list.append(balance_entry)

    def get_user_list():
        user_list = []

        with sqlite3.connect("bankdatabase1.db") as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
             Select  id,
                     first_name,
                     last_name
             From    User""").fetchall()

            for user in data:
                user_list.append(f"{user[0]}-{user[1]} {user[2]} ")

        return user_list

    userinformation_combobox = Combobox(new_account, values=get_user_list())
    userinformation_combobox.grid(row=2, column=6)

    status_entry = Entry(new_account, width=20)
    status_entry.grid(row=2, column=7)
    entry_list.append(status_entry)

    def submit_new_account():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        nationalcode = nationalcode_entry.get()
        account_number = account_number_entry.get()
        balance = balance_entry.get()
        user_id = userinformation_combobox.get().split("-")[0]
        with sqlite3.connect("bankdatabase1.db") as connection:
            cursor = connection.cursor()
            if not id:
                cursor.execute(f"""
                      INSERT INTO Account (
                                  first_name,
                                  last_name,
                                  nationalcode,
                                  Account_number,
                                  balance,
                                  user_id
                              )
                              VALUES (
                                  '{first_name}',
                                  '{last_name}',
                                  '{nationalcode}',
                                  '{account_number}',
                                   {balance},
                                   '{user_id}'     
                              ); 
    """)
            else:
                cursor.execute(f"""
                            UPDATE Account
                            SET first_name       = '{first_name}',
                               last_name        =  '{last_name}',
                               nationalcode    =  '{nationalcode}',
                               Account_number =  '{account_number}',
                               balance =     {balance},
                               user_id =  '{user_id}'
                               WHERE id = {id}""")

            connection.commit()
            create_table_body()
            new_account.destroy()

    submit_button = Button(new_account, text="Subimt", command=submit_new_account)
    submit_button.grid(row=4, column=1, pady=(0, 10), sticky="w")

def deactive_account(active="active"):
     pass

def create_table_header():
    row_label = Label(window, text="NO")
    row_label.grid(row=1, column=0)

    firstname_label = Label(window, text="First name")
    firstname_label.grid(row=1, column=1)

    lastname_label = Label(window, text="Last name")
    lastname_label.grid(row=1, column=2)

    nationalcode_label = Label(window, text="Nationalcode")
    nationalcode_label.grid(row=1, column=3)

    account_number_label = Label(window, text="Account number")
    account_number_label.grid(row=1, column=4)

    balance_label = Label(window, text="Balance")
    balance_label.grid(row=1, column=5)

    user_label = Label(window, text="User")
    user_label.grid(row=1, column=6)

    user_status_label = Label(window, text="Status")
    user_status_label.grid(row=1, column=7)


create_table_header()
entry_list = []


def create_table_body():
    for entry in entry_list:
        entry.destroy()
    entry_list.clear()

    with sqlite3.connect("bankdatabase1.db") as connection:
        cursor = connection.cursor()
        data = cursor.execute("""
SELECT Account.id,
       Account.first_name,
       Account.last_name,
       Account.nationalcode,
       Account.Account_number,
       Account.balance,
       User.first_name  AS user_firstname,
       User.last_name  AS user_lastname,
       User.active     As user_status
FROM Account
Inner join
        User
ON      Account.user_id = User.id """).fetchall()
        row_number = 1
        for account in data:
            row_entry = Entry(window, width=5)
            row_entry.insert(0, row_number)
            row_entry.grid(row=row_number + 1, column=0)
            entry_list.append(row_entry)

            first_name_entry = Entry(window, width=20)
            first_name_entry.insert(0, account[1])
            first_name_entry.grid(row=row_number + 1, column=1)
            entry_list.append(first_name_entry)

            last_name_entry = Entry(window, width=20)
            last_name_entry.insert(0, account[2])
            last_name_entry.grid(row=row_number + 1, column=2)
            entry_list.append(last_name_entry)

            nationalcode_entry = Entry(window, width=20)
            nationalcode_entry.insert(0, account[3])
            nationalcode_entry.grid(row=row_number + 1, column=3)
            entry_list.append(nationalcode_entry)

            account_number_entry = Entry(window, width=20)
            account_number_entry.insert(0, account[4])
            account_number_entry.grid(row=row_number + 1, column=4)
            entry_list.append(account_number_entry)

            balance_entry = Entry(window, width=20)
            balance_entry.insert(0, account[5])
            balance_entry.grid(row=row_number + 1, column=5)
            entry_list.append(balance_entry)

            userinformation_entry = Entry(window, width=20)
            userinformation_entry.insert(0, f"{account[6]} {account[7]} ")
            userinformation_entry.grid(row=row_number + 1, column=6)
            entry_list.append(userinformation_entry)

            status_entry = Entry(window, width=20)
            status_entry.insert(0, account[8])
            status_entry.grid(row=row_number + 1, column=7)
            entry_list.append(status_entry)

            update_button = Button(window, text="Update", command=lambda user_id=account[0],
                                                                         first_name=account[1],
                                                                         last_name=account[2],
                                                                         natinalcode=account[3],
                                                                         account_number=account[4],
                                                                         balance=account[5],
                                                                         user_info=f"{account[6]} {account[7]} ",
                                                                         active=account[8]: add_new_account(user_id,
                                                                                                            first_name,
                                                                                                            last_name,
                                                                                                            natinalcode,
                                                                                                            account_number,
                                                                                                            balance,
                                                                                                            user_info,
                                                                                                            active))
            update_button.grid(row=row_number + 1, column=8, sticky="w")
            deactive_button = Button(window , text="Deactive",command=deactive_account)
            deactive_button.grid(row=row_number + 1,column=9, sticky="w")
            row_number += 1


create_table_body()

search_list = []


def search_on_list_account():
    for entry in search_list:
        entry.destory()
    search_list.clear()
    search = Tk()
    search.title("Search")

    nationalcode_label = Label(search, text="National code")
    nationalcode_label.grid(row=0, column=0)

    account_number_label = Label(search, text="Account number")
    account_number_label.grid(row=1, column=0)

    nationalcode_entry = Entry(search, width=20)
    nationalcode_entry.grid(row=0, column=1)
    login_list.append(nationalcode_entry)

    account_number_entry = Entry(search, width=20)
    account_number_entry.grid(row=1, column=1)
    login_list.append(account_number_entry)

    check_label = Label(search, text="")
    check_label.grid(row=2, column=1)

    def nationalcode_account_number_list():
        nationalcode_list = []
        account_number_list = []
        with sqlite3.connect("bankdatabase1.db") as connection:
            cursor = connection.cursor()
            data = cursor.execute("""
        SELECT first_name,
                last_name,
                nationalcode,
                Account_number,
                 balance
        FROM Account;
                 """).fetchall()
            for account in data:
                nationalcode_list.append(account[2])
                account_number_list.append(account[3])
            if nationalcode_entry.get() in nationalcode_list and account_number_entry.get() in account_number_list:
                index = nationalcode_list.index(nationalcode_entry.get())
                if account_number_list[index] == account_number_entry.get():
                    account = data[index]
                    check_label.config(
                        text=f"account fullname is {account[0]},{account[1]} and balance is equal to {account[4]}",
                        fg="black")
            else:
                check_label.config(text="Can't find account with this information", fg="red")

    submit_buttom = Button(search, text="Search", command=nationalcode_account_number_list)
    submit_buttom.grid(row=3, column=1, pady=10, padx=0, sticky="w")


new_account_list = []


add_new_account_buttom = Button(window, text="add new account", command=add_new_account)
add_new_account_buttom.grid(row=0, column=1, pady=10, padx=0, sticky="w")

search_on_account_list_buttom = Button(window, text="Search", command=search_on_list_account)
search_on_account_list_buttom.grid(row=0, column=2, pady=10, padx=0, sticky="w")

window.mainloop()
