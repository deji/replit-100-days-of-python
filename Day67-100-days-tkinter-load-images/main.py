import os
import tkinter as tk
from PIL import Image, ImageTk

images = {}

window = tk.Tk()
window.title("Hello World")
window.geometry("600x600")


def changeImage():
  image_name = image_to_load.get().lower()
  if image_name in images:
    image = images[image_name]
    canvas.itemconfig(container, image=image)
    msg["text"] = ""
  else:
    canvas.itemconfig(container, image="")
    msg["text"] = "Image not found"


def load_images():
  for filename in os.listdir("Guess Who"):
    if filename.endswith((".jpg", ".png")):
      # Get the filename without the extension
      name_without_ext = os.path.splitext(filename)[0]

      # Load and resize the image
      image = Image.open(f"Guess Who/{filename}")
      image.thumbnail((300, 400))

      # Store the image in the dictionary using the name without extension
      images[name_without_ext] = ImageTk.PhotoImage(image)


hello = tk.Label(text="Guess Who?")
hello.pack()

image_to_load = tk.Entry(window, width=30)
image_to_load.pack()

button = tk.Button(text="Click me!", command=changeImage)
button.pack()

canvas = tk.Canvas(window, width=300, height=400)
canvas.pack()

msg = tk.Label(text="")
msg.pack()

container = canvas.create_image(150, 200)

load_images()

tk.mainloop()
