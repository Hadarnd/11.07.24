x: str = str(input("what is the opposite of bad?"))
y: str = str(input("what part of the day is in 8am?"))


while True:
    if x == y:
        break
    else:
        print(f"{x} {y}")

print("finish")
