
import sys



file_name = "gamesin.txt"
genre = ""
genre_row = 4
title = ""
year = 0


def count_games(file_name):
    '''
    return counted games from the file text
    '''
    with open("gamesin.txt", "r") as f:
        count = 0
        for line in f:
            count += 1
        return count


def decide(file_name,  year):
    '''
    return the game from a given year if exist else will return false!
    '''
    
    with open("gamesin.txt") as f:
        year = any(str(year) in line for line in f)
        return year



def get_latest(file_name):
    '''
    return latest game by year
    '''
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


def count_by_genre(file_name, genre):
    '''
    return counted genre from file text
    '''
    genre_list = []
    with open("gamesin.txt") as f:
        count = 0
        for i in f:
            item = i.split("\t")
            if item[3] == genre:
                count +=1
        return count
       
       


def get_line_number_by_title(file_name, title):
    '''
    return position of a game
    '''
    with open("gamesin.txt") as f:
        for i, row in enumerate(f, 1):
            if title in row:
                return i
    raise ValueError("This game is not in the file")
    

def sort_abc(file_name):
    '''
    return sorted list
    '''
    element_index = 0
    list_sort = []
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


def get_genres(file_name):
    '''
    return counted genres
    '''
    index_genres = 3
    list_genres = []
    with open("gamesin.txt") as f:
        for line in f:
            item = line.split("\t")
            if item[index_genres] not in list_genres:
                
                list_genres.append(item[index_genres])
        n = len(list_genres)
        for i in range(n):
            for j in range(0, n-i-1):
                if list_genres[j] > list_genres[j+1]:
                    temp = list_genres[j]
                    list_genres[j] = list_genres[j+1]
                    list_genres[j+1] = temp

    return list_genres


def when_was_top_sold_fps(file_name):
    
    '''
    return year of top sold game
    '''
    
    try:
        with open("gamesin.txt") as file:
            file_reader = file.readlines()
        best_sold = 0
        year_best_sold = 0
        for i in range(len(file_reader)):
            if file_reader[i].split("\t")[3].strip() == "First-person shooter":
                if float(file_reader[i].split("\t")[1].strip()) > float(best_sold):
                    best_sold = float(file_reader[i].split("\t")[1].strip())
                    year_best_sold = file_reader[i].split("\t")[2].strip()
    except FileNotFoundError:
     raise ValueError('Non-existing game')

    return int(year_best_sold)
        
       


