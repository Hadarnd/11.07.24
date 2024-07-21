#question 1:

a: float = float(input("what is the current temperature?"))

print("hot" if a > 30 else "normal")

#question 1 bonus:

a: float = float(input("what is the current temperature?"))

print("freez" if a < 0 else "normal" if a < 20 else "hot")


