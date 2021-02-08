print('Aplikacja do symulowania gier liczbowych')

def show_menu():
    print("")
    print("1 - Duży lotek")
    print("2 - Mini lotto")
    print("3 - Multi Multi")
    print("4 - Zakończ program")

def big_lotto():
    print("Duzy lotek")

def mini_lotto():
    print("Mini lotto")

def multi_multi():
    print("Multi multi")

def exit():
    print("Do zobaczenia ")
    
def error():
    print("Błąd")

while True:
    show_menu()
    user_choice = int(input("Wybierz pozycję z menu: "))
    print()
    if user_choice == 1:
        big_lotto()
    elif user_choice == 2:
        mini_lotto()
    elif user_choice == 3:
        multi_multi()
    elif user_choice == 4:
        exit()
        break
    else:
        error()

