import random


def truth_or_action():
    while True:
        print("кто ты по жизни ヾ(•ω•`)o")
        choice = input()

        if choice == "truth":
            print("почему небо зелёное?")
            fear = input()
            print(f"==== {fear}.")
            break

        elif choice == "action":
            print("сделай сальто .")
            # perform funny dance
            break

        else:
            print("делай выбор, делай выбор, ладно.")


truth_or_action()