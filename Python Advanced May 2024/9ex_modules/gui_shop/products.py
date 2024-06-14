import json
import os
import tkinter as tk
from canvas import app
from helpers import clean_screen
from PIL import Image, ImageTk

base_folder = os.path.dirname(__file__)


def update_current_user(username, product_id):
    with open('db/users.txt', 'r+') as f:
        users = [json.loads(u.strip()) for u in f]
        for user in users:
            if user['username'] == username:
                user['products'].append(product_id)
                f.seek(0)
                f.truncate()
                f.writelines([json.dumps(u) + '\n' for u in users])


def purchase_product(product_id):
    with open('db/products.txt', 'r+') as f:
        products = [json.loads(p.strip()) for p in f]
        for product in products:
            if product['id'] == product_id:
                product['count'] -= 1
                f.seek(0)
                f.truncate()
                f.writelines([json.dumps(p) + '\n' for p in products])
                return


def buy_product(product_id):
    clean_screen()

    with open('db/current_user.txt') as file:
        username = file.read()

    if username:
        update_current_user(username, product_id)
        purchase_product(product_id)

    render_products_screen()


def render_products_screen():
    clean_screen()

    with open('db/products.txt') as file:
        products = [json.loads(p.strip()) for p in file]
        for i, product in enumerate(products):
            row = i // 5 * 4
            col = i % 5
            tk.Label(app, text=product['name']).grid(row=row, column=col, padx=10, pady=(10, 0))

            img = Image.open(os.path.join(base_folder, 'db', 'images', product['img_path'])).resize((100, 100))
            photo_image = ImageTk.PhotoImage(img)
            image_label = tk.Label(image=photo_image)
            image_label.image = photo_image
            image_label.grid(row=row + 1, column=col, padx=10, pady=(10, 0))

            tk.Label(app, text=product['count']).grid(row=row + 2, column=col, padx=10, pady=(10, 0))
            tk.Button(app,
                      text=f'Buy {product['id']}',
                      command=lambda p=product['id']: buy_product(p)
                      ).grid(row=row+3, column=col, padx=10, pady=(10, 25))
        tk.Button(app,
                  text='Exit',
                  command=app.destroy
                  ).grid(row=i*4+2, column=col // 2 + 1, padx=10, pady=35)
