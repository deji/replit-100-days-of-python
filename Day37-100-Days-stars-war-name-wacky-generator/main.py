import random

def generate_name(wordsList):
    firstChunk = wordsList[0][:3]
    secondChunk = wordsList[1][:3]
    thirdChunk = wordsList[2][:2]
    fourthChunk = wordsList[3][-3:]
    return f"{firstChunk.title()}{secondChunk.lower()} {thirdChunk.title()}{fourthChunk.lower()}"

def generate_wacky_name(wordsList):
    firstChunk = wordsList[random.randint(0, len(wordsList)-1)][:3]
    secondChunk = wordsList[random.randint(0, len(wordsList)-1)][:3]
    thirdChunk = wordsList[random.randint(0, len(wordsList)-1)][:2]
    fourthChunk = wordsList[random.randint(0, len(wordsList)-1)][-3:]
    return f"{firstChunk.title()}{secondChunk.lower()} {thirdChunk.title()}{fourthChunk.lower()}"

print("🌟Star Wars Name Generator🌟")
print()
wordsList = input("Enter your first name, last name, mum's maiden name and the city you were born in (separated by spaces): ").split()
print()
print(f"Your Star Wars name is {generate_name(wordsList)} and a wacky variant is {generate_wacky_name(wordsList)}.")
