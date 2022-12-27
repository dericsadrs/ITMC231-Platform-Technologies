from emmet import Emmet

rawStringInput = input()
w = Emmet(rawStringInput)
print(w)
while rawStringInput != "quit":
    rawStringInput = input()
    if rawStringInput == "quit":
        break
    else:
        w = Emmet(rawStringInput)
    print(w)