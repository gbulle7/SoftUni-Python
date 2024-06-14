import tkinter as tk
from canvas import app
from helpers import clean_screen
from products import render_products_screen
import json


def login(username, password):
    with open('db/users_credentials.txt') as file:
        data = file.readlines()
        for line in data:
            name, pwd = line.strip().split(', ')
            if name == username and pwd == password:
                with open('db/current_user.txt', 'w') as f:
                    f.write(name)
                render_products_screen()
                return
    return render_login_screen(error='Invalid username or password!')


def render_login_screen(error=None):
    clean_screen()
    username = tk.Entry()
    username.grid(row=0, column=0, padx=(260, 0), pady=(200, 0))
    password = tk.Entry(show='*')
    password.grid(row=1, column=0, padx=(260, 0), pady=(10, 0))
    tk.Button(app,
              text='Login',
              bg='green',
              fg='black',
              command=lambda: login(username.get(), password.get())
              ).grid(row=2, column=0, padx=(260, 0), pady=(10, 0))
    back_buttons()
    tk.Label(app, text=error, width=25).grid(row=3, column=0, padx=(270, 0), pady=(10, 0))


def register(**user):
    clean_screen()

    user.update({'products': []})
    with open('db/users_credentials.txt', 'a+') as file:
        users = [line.strip().split(', ')[0] for line in file]
        if user['username'] in users:
            render_register_screen(error='User already exists!')
            return
        file.write(f'\n{user['username']}, {user['password']}')
    with open('db/users.txt', 'a') as file:
        file.write('\n' + json.dumps(user))

    render_login_screen()


def render_register_screen(error=None):
    clean_screen()
    username = tk.Entry()
    username.grid(row=0, column=0, padx=(260, 0), pady=(140, 0))
    password = tk.Entry(show='*')
    password.grid(row=1, column=0, padx=(260, 0), pady=(10, 0))
    first_name = tk.Entry()
    first_name.grid(row=2, column=0, padx=(260, 0), pady=(10, 0))
    last_name = tk.Entry()
    last_name.grid(row=3, column=0, padx=(260, 0), pady=(10, 0))
    tk.Button(app,
              text='Register',
              bg='yellow',
              fg='black',
              command=lambda: register(
                  username=username.get(),
                  password=password.get(),
                  first_name=first_name.get(),
                  last_name=last_name.get()
              )
              ).grid(row=4, column=0, padx=(260, 0), pady=(10, 0))
    tk.Label(app, text=error, width=25).grid(row=5, column=0, padx=(270, 0), pady=(10, 0))
    back_buttons()


def render_main_enter_screen():
    clean_screen()
    tk.Button(app,
              text='Login',
              background='green',
              foreground='white',
              command=render_login_screen
              ).grid(row=0, column=0, padx=(300, 0), pady=250)
    tk.Button(app,
              text='Register',
              background='yellow',
              foreground='black',
              command=render_register_screen
              ).grid(row=0, column=1, padx=(10, 0), pady=250)


def back_buttons():
    tk.Button(app, text='Back', command=render_main_enter_screen).grid(row=10, column=0, padx=(230, 10), pady=10)
    tk.Button(app, text='Exit', command=app.destroy).grid(row=10, column=0, padx=(320, 10), pady=10)
