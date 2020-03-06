import os


file_name= "gamesin.txt"
genre = " "
genre_row = 4
title = ""
year = 0


def count_games(file_name):

    file_name = open("gamesin.txt", "r")
    count = 0
    for line in file_name:
        count += 1
    return count


def decide(file_name,  year):

    
        with open(file_name) as f:
            year = any(str(year) in line for line in f)
            return year


# print(decide(file_name, 2002))


def get_latest(file_name):
    
    index_of_year = 2
    index_of_id = 0
    with open("gamesin.txt") as f:
        list1 = f.read().splitlines()
        list2 = []
        year = 0
        for i in list1:
            list2.append(i.split("\t"))
            for i in list2:
                if int(i[index_of_year]) > year:
                    year = int(i[index_of_year])
                    new_game = i[index_of_id]
        return new_game


# print(get_latest(file_name))


def count_by_genre(file_name,  genre):


    genre_list = []
    with open("gamesin.txt") as f:
        for row in f.readlines():
            row = row.split("\t")
            row[genre_row] = row[genre_row][-1]
            if genre in row:
                genre_list.append(genre)
                genre = len(genre_list)
        return genre


# print(count_by_genre(file_name, "Action-adventure"))


def get_line_number_by_title(file_name, title):
   
        with open("gamesin.txt") as f:
            for i, row in enumerate(f, 1):
                if title in row:
                    return i
    
            

# print(get_line_number_by_title(file_name, "a"))


def sort_abc(file_name):

    element_index = 0
    
    list_sort=[]
    with open("gamesin.txt") as f:
        for line in f:
            item = line.split("\t")
            list_sort.append(item[element_index])
        n = len(list_sort)
        for i in range(n):
            for j in range(0, n-i-1):
                if list_sort[j] > list_sort[j+1]:
                    list_sort[j], list_sort[j+1] = list_sort[j+1], list_sort[j]
    return list_sort


# print(sort_abc("gamesin.txt"))


def get_genres(file_name):
    
    index_genres = 3
    list_genres = []
    with open("gamesin.txt") as f:
        for line in f:
            item = line.split("\t")
            list_genres.append(item[index_genres])
        if item[index_genres] not in list_genres:
            list_genres.append(item[index_genres])

        
        n = len(list_genres)
        for i in range(n):
            for j in range(0, n-i-1):
                if list_genres[j] > list_genres[j+1]:
                    list_genres[j], list_genres[j+1] = list_genres[j+1], list_genres[j]
    return set(list_genres)

# print(get_genres(file_name))


def when_was_top_sold_fps(file_name):
    best=0
    title=""
    index_genres = 3
    index_sold = 1
    index_game = 0

    with open (file_name) as f:
        for line in f:
            elem = line.split("\t")
            gen=elem[index_genres]
            item=float(elem[index_sold])
            if gen== "First-person shooter":
                if best < item:
                    best=item
                    title=elem[index_game]

    if best==index_game:
        return "ValueError"

    return title


# print(when_was_top_sold_fps(file_name))


def main():
    while True:
        count_genre = count_games(file_name)
        print(count_genre)
        message = input("Enter a year :")
        game_from_year = decide(file_name,year)
        print(game_from_year )
        continue

main()
