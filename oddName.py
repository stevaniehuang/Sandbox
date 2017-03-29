"""Stevanie"""

while True:
    try:
        name = input("Please enter your name: ")
        print(name[1])
        print(len(name))
        break

    except ValueError:
        print("error")
        continue



