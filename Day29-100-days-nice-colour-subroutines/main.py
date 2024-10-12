def colour(word, colour):
    if colour == "red":
        print("\033[31m", word, "\033[0m", sep="", end="")
    elif colour == "green":
        print("\033[32m", word, "\033[0m", sep="", end="")
    elif colour == "blue":
        print("\033[34m", word, "\033[0m", sep="", end="")
    elif colour == "yellow":
        print("\033[33m", word, "\033[0m", sep="", end="")
    else:
        print("\033[0m", word, "\033[0m", sep="", end="")


print("Super Subroutine")
print()
print("With my ", end="")
colour("new program ", "blue")
colour("I can just call red ", "yellow")
colour("and ", "red")
colour("that word will appear in the colour I set it to.", "green")
print()
print()
colour("With no ", "yellow")
colour("weird gaps", "green")
print()
print()
colour("Epic.", "red")
print()
print()
print("Back to normal again.")
