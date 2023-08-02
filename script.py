import videogameData

def program():
    print("Hello! Welcome to the best videogame recommendation software there is on the whole internet! Here is a list of all the genres of videogames, please introduce the first letter of genre of your choosing.")
    print(videogameData.types)
    letter = input()
    while len(letter) != 1: 
        letter = input("Introduce only the first letter: ")

    first_iteration = []
    for genre in videogameData.types:
        if genre[0] == letter[0]:
            first_iteration.append(genre)

    if len(first_iteration) >= 2:
        print("Here is a list of the searched genres: ") 
        print(first_iteration)
        letter = input("Introduce the first two letters of the genre:")
        second_i = []
        for genre in videogameData.types:
            if genre[:2] == letter[:2]:
                second_i.append(genre)
        print("Here is the only genre found: ")
        print(second_i)
        cont = input("Would you like to continue? (y/n): ")
        if cont == "y":
            search(first_iteration)
        else:
            exit()

    if len(first_iteration) == 1:
        print("Here is the only genre found: ")
        print(first_iteration)
        cont = input("Would you like to continue? (y/n): ")
        if cont == "y":
            search(first_iteration)
        else:
            exit()

    if len(first_iteration) == 0:
        print("No genres found. ")
        exit()

def search(iteration):
    for game in videogameData.games_data :
            if game[0] == iteration[0]:
                print(game[1:])

program()
