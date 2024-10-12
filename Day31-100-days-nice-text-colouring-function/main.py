def colour(word, colour):
    if colour == "red":
        text = "\033[31m" + word + "\033[0m"
    elif colour == "green":
        text = "\033[32m" + word + "\033[0m"
    elif colour == "blue":
        text = "\033[34m" + word + "\033[0m"
    elif colour == "yellow":
        text = "\033[33m" + word + "\033[0m"
    else:
        text = "\033[0m" + word + "\033[0m"

    return text


title = colour('=', 'red') + colour('=', 'white') + colour(
    '=', 'blue') + colour(' Music App ', 'yellow') + colour(
        '=', 'blue') + colour('=', 'white') + colour('=', 'red')
print(f"{title:^120}")
print()
print(f"🔥▶️\t\t{colour('Radio Gaga', 'white')}")
print(f"\t\t{colour('Queen', 'yellow')}")
print()
print()
print(f"{colour('PREV', 'white')}")
print(f"\t\t{colour('NEXT', 'green')}")
print(f"\t\t\t\t{colour('PAUSE', 'red')}")

print()
print(f"{'WELCOME TO':^80}")
print(f"{colour('--- ARMBOOK ---', 'blue'):^89}")

print()
print(f"{colour('Definitely not a rip off of', 'yellow'):>89}")
print(f"{colour('a certain other social', 'yellow'):>89}")
print(f"{colour('networking site.', 'yellow'):>89}")

print()
print(f"{colour('Honest.', 'red'):^89}")
print()
print(f"{colour('Username: ', 'white'):^89}")
print(f"{colour('Password: ', 'white'):^89}")
