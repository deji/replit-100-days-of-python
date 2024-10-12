import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("600x300")

label = 0
last_number = 0
ops = None


def updateLabel(key_pressed):
  global label
  global ops
  global last_number

  if key_pressed.isdigit():
    if label == 0:
      label = key_pressed
    else:
      label += key_pressed
  elif key_pressed in ["+", "-", "*", "÷"]:
    if ops is None:
      ops = key_pressed
      last_number = label
    else:
      last_number = eval(f"{last_number}{ops}{label}")
    label = 0
  elif key_pressed == "=" and ops is not None:
    last_number = eval(f"{last_number}{ops}{label}")
    label = str(last_number)
    ops = None
  else:
    pass

  hello["text"] = label


def key_1():
  updateLabel("1")


def key_2():
  updateLabel("2")


def key_3():
  updateLabel("3")


def key_plus():
  updateLabel("+")


def key_minus():
  updateLabel("-")


def key_4():
  updateLabel("4")


def key_5():
  updateLabel("5")


def key_6():
  updateLabel("6")


def key_multiply():
  updateLabel("*")


def key_divide():
  updateLabel("÷")


def key_7():
  updateLabel("7")


def key_8():
  updateLabel("8")


def key_9():
  updateLabel("9")


def key_equals():
  updateLabel("=")


def key_0():
  updateLabel("0")


hello = tk.Label(text=label)
hello.grid(row=0, column=1)

button = tk.Button(text="1", command=key_1)
button.grid(row=1, column=0)
button = tk.Button(text="2", command=key_2)
button.grid(row=1, column=1)
button = tk.Button(text="3", command=key_3)
button.grid(row=1, column=2)
button = tk.Button(text="+", command=key_plus)
button.grid(row=1, column=3)
button = tk.Button(text="-", command=key_minus)
button.grid(row=1, column=4)
button = tk.Button(text="4", command=key_4)
button.grid(row=2, column=0)
button = tk.Button(text="5", command=key_5)
button.grid(row=2, column=1)
button = tk.Button(text="6", command=key_6)
button.grid(row=2, column=2)
button = tk.Button(text="*", command=key_multiply)
button.grid(row=2, column=3)
button = tk.Button(text="÷", command=key_divide)
button.grid(row=2, column=4)
button = tk.Button(text="7", command=key_7)
button.grid(row=3, column=0)
button = tk.Button(text="8", command=key_8)
button.grid(row=3, column=1)
button = tk.Button(text="9", command=key_9)
button.grid(row=3, column=2)
button = tk.Button(text="=", command=key_equals)
button.grid(row=3, column=3)
button = tk.Button(text="0", command=key_0)
button.grid(row=4, column=1)

tk.mainloop()
