from jokes import get_joke

def main():
    name = input("Введіть Ваше ім'я: ")
    print(f"Привіт, {name}!")

    while True:
        question = input(f"{name}, бажаєте прочитати анекдот? (так/ні)").lower()
        if question == "так":
            print(get_joke())
        elif question == "ні":
            print(f"До побачення, {name}!")
            break

main()