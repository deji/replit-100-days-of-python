import contextlib, os
import tkinter as tk
from PIL import Image, ImageTk

images = {}
buttons = {}

text = {
    'drive': 'always a good and comfortable way to travel 🚗',
    'crash': 'you meet an untimely end due to your indecision 💥',
    'decision': 'how do you want to travel? Pick wisely 😇',
    'fly': 'inconvenient and what'
    's with all the drama ✈️',
}

window = tk.Tk()
window.title("My visual novel")
window.geometry("600x600")


def clear_buttons():
  for button in buttons:
    buttons[button].pack_forget()


def startover():
  clear_buttons()
  canvas.itemconfig(container, image=images["decision"])
  msg["text"] = text["decision"] + '\n'
  buttons["option_fly"].pack()
  buttons["option_drive"].pack()
  buttons["option_indecision"].pack()


def option_fly():
  clear_buttons()
  canvas.itemconfig(container, image=images["jet"])
  msg["text"] = text["fly"] + '\n'
  buttons["startover"].pack()


def option_drive():
  clear_buttons()
  canvas.itemconfig(container, image=images["car"])
  msg["text"] = text["drive"] + '\n'
  buttons["startover"].pack()


def option_indecision():
  clear_buttons()
  canvas.itemconfig(container, image=images["crash"])
  msg["text"] = text["crash"] + '\n'
  buttons["startover"].pack()


def load_images():
  for filename in os.listdir():
    if filename.endswith((".jpg", ".png")):
      # Get the filename without the extension
      name_without_ext = os.path.splitext(filename)[0]

      # Load and resize the image
      image = Image.open(f"{filename}")
      image.thumbnail((300, 400))

      # Store the image in the dictionary using the name without extension
      images[name_without_ext] = ImageTk.PhotoImage(image)


canvas = tk.Canvas(window, width=300, height=400)
canvas.pack()

container = canvas.create_image(150, 200)

load_images()

msg = tk.Label(text="")
msg.pack()

buttons["startover"] = tk.Button(text="Try again 🔃", command=startover)
buttons["option_fly"] = tk.Button(text="Fly", command=option_fly)
buttons["option_drive"] = tk.Button(text="Drive", command=option_drive)
buttons["option_indecision"] = tk.Button(text="I don't know",
                                         command=option_indecision)

startover()

tk.mainloop()
