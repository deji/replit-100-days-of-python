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


def create_mokébeast(beast_params_list):
    beast = {}
    beast['name'] = beast_params_list[0].title().strip()
    beast['type'] = beast_params_list[1].title().strip()
    beast['special_move'] = beast_params_list[2].title().strip()
    beast['starting_hp'] = int(beast_params_list[3])
    beast['starting_mp'] = int(beast_params_list[4])
    return beast


def output_mokébeast(beast):
    template = f"""name: {beast['name']} | element: {beast['type']} | special move: {beast['special_move']} | HP: {beast['starting_hp']} | MP: {beast['starting_mp']}"""
    if beast["type"] == "Earth":
        print(colour(template, "green"))
    elif beast["type"] == "Fire":
        print(colour(template, "red"))
    elif beast["type"] == "Air":
        print(colour(template, "blue"))
    elif beast["type"] == "Water":
        print(colour(template, "yellow"))
    else:
        print(template)


def pretty_print(beasts):
    print()
    print("🌟MokeBeast Generator🌟")
    print()
    for beast in beasts:
        output_mokébeast(beasts[beast])
    print()


mokédex = {}

print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")

while True:
    answer = input("""
    Enter your beast's:
      name, 
      type (earth, fire, air, water or spirit), 
      special move, 
      starting HP and 
      starting MP 
    all separated by commas > """)
    answer_list = answer.split(", ")
    mokebeast = create_mokébeast(answer_list)
    mokédex[mokebeast["name"]] = mokebeast

    repeat = input("\n    Again? y/n > ")
    if repeat.lower().strip() == "y":
        continue
    break

pretty_print(mokédex)
