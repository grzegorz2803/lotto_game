print('Aplikacja do symulowania gier liczbowych')

def show_menu():
    print("")
    print("1 - Duży lotek")
    print("2 - Mini lotto")
    print("3 - Multi Multi")
    print("4 - Zakończ program")

while True:
    show_menu()
    user_choice = int(input("Wybierz pozycję z menu: "))
    print()
    if user_choice == 1:
        print("Duzy lotek")
    elif user_choice == 2:
        print("Mini lotto")
    elif user_choice == 3:
        print("Multi multi")
    elif user_choice == 4:
        break
    else:
        print("Błąd")

