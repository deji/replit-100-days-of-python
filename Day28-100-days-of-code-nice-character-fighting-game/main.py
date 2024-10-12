import random, time, os


def rollDice(sides):
    roll = random.randint(1, sides)
    return roll


def healthRollDice():
    health = int((rollDice(6) * rollDice(12)) / 2 + 10)
    return health


def strengthRollDice():
    strength = int((rollDice(6) * rollDice(12)) / 2 + 12)
    return strength


def characterBuilder():
    print("💊 Character Builder 💊")
    print()
    time.sleep(1)
    name = input("Name your Legend: ")
    type = input("Character Type (Human, Elf, Wizard, Orc): ")
    health = healthRollDice()
    strength = strengthRollDice()
    time.sleep(1)
    print()
    print(name)
    print("HEALTH: ", health)
    print("STRENGTH: ", strength)
    print()
    return name, type, health, strength


player1Name, player1Type, player1Health, player1Strength = characterBuilder()
time.sleep(1)
print("Who are they battling?")
print()
player2Name, player2Type, player2Health, player2Strength = characterBuilder()
time.sleep(3)
os.system("clear")

print("⚔️ BATTLE TIME ⚔️")
print()
time.sleep(1)
print("The battle begins!")

round = 1
while True:
    player1Roll = rollDice(6)
    player2Roll = rollDice(6)
    if player1Roll > player2Roll:
        damage = abs(player1Strength - player2Strength) + 1
        player2Health = max(player2Health - damage, 0)
        print(player1Name, "wins the round")
        print(player2Name, "takes a hit, with", damage, "damage")
    elif player2Roll > player1Roll:
        damage = abs(player1Strength - player2Strength) + 1
        player1Health = max(player1Health - damage, 0)
        print(player2Name, "wins the round")
        print(player1Name, "takes a hit, with", damage, "damage")
    else:
        print("It's a tie!")

    print()
    print(player1Name)
    print("HEALTH: ", player1Health)
    print()
    print(player2Name)
    print("HEALTH: ", player2Health)
    print()

    if player1Health <= 0:
        print("Oh no,", player1Name, "has died!")
        print(player2Name, "destroyed", player1Name, "in", round, "rounds!")
        break
    elif player2Health <= 0:
        print("Oh no,", player2Name, "has died!")
        print(player1Name, "destroyed", player2Name, "in", round, "rounds!")
        break
    else:
        print("And they're both standing for the next round!")
        round += 1
        time.sleep(3)
        os.system("clear")
        print("""
⚔️ BATTLE TIME ⚔️

The battle continues!
        """)
        print()
        continue
