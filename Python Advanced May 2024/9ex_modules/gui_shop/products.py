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


def add_product(name, img, count):
    with open('db/products.txt', 'r+') as file:
        if name == '' or img == '' or count == '' or not count.isdigit():
            render_add_product_screen(error='Invalid data input.\nAll fields required.')
            return
        file.write('\n' + json.dumps({
            'id': len(file.readlines()) + 1,
            'name': name,
            'img_path': img,
            'count': int(count)
        }))

    render_products_screen()


def render_add_product_screen(error=None):
    clean_screen()

    tk.Label(app, text='Name: ').grid(row=0, column=0)
    name = tk.Entry(app)
    name.grid(row=0, column=1)

    tk.Label(app, text='Image: ').grid(row=1, column=0)
    img = tk.Entry(app)
    img.grid(row=1, column=1)

    tk.Label(app, text='Count: ').grid(row=2, column=0)
    count = tk.Entry(app)
    count.grid(row=2, column=1)

    tk.Button(app,
              text='Add',
              command=lambda: add_product(name.get(), img.get(), count.get())
              ).grid(row=3, column=0)

    tk.Label(app, text=error, height=3, width=20).grid(row=4, column=0)

    tk.Button(app,
              text='Exit',
              command=app.destroy
              ).grid(row=5, column=3, padx=10, pady=25)


def render_products_screen():
    clean_screen()

    with open('db/current_user.txt') as file:
        username = file.read()
    with open('db/users.txt') as f:
        users = [json.loads(u.strip()) for u in f]
        for user in users:
            if user['username'] == username:
                try:
                    u = user['is_admin']
                except KeyError:
                    pass
                else:
                    tk.Button(app,
                              text='Add product',
                              command=lambda: render_add_product_screen()
                              ).grid(row=0, column=0)

    with open('db/products.txt') as file:
        products = [json.loads(p.strip()) for p in file]
        for i, product in enumerate(products):
            row = i // 5 * 4 + 1
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
                  ).grid(row=i*4+2, column=2, padx=10, pady=35)
