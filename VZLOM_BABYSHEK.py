import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def replace_with_photo():
    global photo

    image = Image.open("grandbabulya.png")

    width, height = image.size
    new_width = 200
    aspect_ratio = width / height
    new_height = int(new_width / aspect_ratio)

    image = image.resize((new_width, new_height), Image.BICUBIC)
    photo = ImageTk.PhotoImage(image)
    image_placeholder.config(image=photo, text="")
    image_placeholder.image = photo
    image_placeholder.pack(fill="both", expand=True)

def submit_grandma():
    submit_button.config(text="ВЫ УСПЕШНО СДАЛИ СВОЮ БАБУШКУ")

    # Open a new window for credit card input
    credit_window = tk.Toplevel(root)
    credit_window.title("Введите номер кредитной карты")

    credit_label = tk.Label(credit_window, text="Номер кредитной карты:")
    credit_label.pack()

    credit_entry = tk.Entry(credit_window)
    credit_entry.pack()

    payout_button = tk.Button(credit_window, text="ПОЛУЧИТЬ ВЫПЛАТУ", command=notify_arrest)
    payout_button.pack()

def notify_arrest():
    messagebox.showinfo("Уведомление", "ВЫ БЫЛИ АРЕСТОВАНЫ ЗА НЕЗАКОННУЮ ПРОДАЖУ ПЕНСИОНЕРОВ И ВЗЛОМА КАЗИНО НА 78%")
    root.destroy()

cost = random.randint(100, 5000)

root = tk.Tk()
root.title("Пенсионеро-приемник")

main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack()

title = tk.Label(main_frame, text="пенсионеро-приемник", font=("Arial", 14))
title.pack()

instruction = tk.Label(main_frame, text="закиньте сюда свою бабушку", font=("Arial", 12))
instruction.pack()

arrow_label = tk.Label(main_frame, text="⬇️", font=("Arial", 24))
arrow_label.pack()

image_placeholder = tk.Label(main_frame, text="ФОТО БАБУШКИ", width=322, height=276, relief="solid")
image_placeholder.pack(pady=10)

submit_button = tk.Button(main_frame, text="Сдать свою бабушку", command=submit_grandma)
submit_button.pack(pady=10)

cost_label = tk.Label(main_frame, text=f"Стоимость бабушки: {cost} рублей", font=("Arial", 12))
cost_label.pack(pady=10)

red_button = tk.Button(root, text="", bg="red", width=2, height=1, command=replace_with_photo)
red_button.place(x=280, y=200) 

root.mainloop()
