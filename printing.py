
def main():
    file_name = "gamesin.txt"
    genre = ""
    genre_row = 4
    title = ""
    year = 0
    print("Hi Judy!\nChoose a option bellow!")
    print("")
    print("1.Do you know how many games are in the fille?")
    print("2.Is there a game from a given year?")
    print("3.Which is the latest game?")
    print("4.How many games are in the file by genre?")
    print("5.What is the line number of a given title?")
    print("6.Can you give me the alphabetically ordered list of the titles?")
    print("7.Which genres occur in the data file?")
    print("8.What is the release year of the top sold first-person shooter game?")
    print("")
    while True:
        question = input("What do you want to know? ")
        if question == "1":
            print(count_games(file_name))
        if question == "2":
            year = input("Enter a year: ")
            print(decide(file_name,  year))
        if question == "3":
            print(get_latest(file_name))
        if question == "4":
            genre = input("Enter a genre:")
            print(count_by_genre(file_name, genre))
        if question == "5":
            title = input("Enter a title: ")
            print(get_line_number_by_title(file_name, title))
        if question == "6":
            print(sort_abc(file_name))
        if question == "7":
            print(get_genres(file_name))
        if question == "8":
            print(when_was_top_sold_fps(file_name))
        


if __name__ == "__main__":
    main()