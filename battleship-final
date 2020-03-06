import time
import subprocess
import os
import sys
import copy
import random


def cover():
    print(
        '''




        
                                                       ______     ______     ______   ______   __         ______     ______     __  __     __     ______  
                                                      /\  __ \   /\  __ \   /\__  _\ /\__  _\ /\ \       /\  ___\   /\  ___\   /\ \_\ \   /\ \   /\  __ \ 
                                                      \ \  __<   \ \  __ \  \/_/\ \/ \/_/\ \/ \ \ \____  \ \  __\   \ \___  \  \ \  __ \  \ \ \  \ \  __/ 
                                                       \ \_____\  \ \_\ \_\    \ \_\    \ \_\  \ \_____\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_\  \ \_\   
                                                        \/_____/   \/_/\/_/     \/_/     \/_/   \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_/   \/_/   
                                                                                                    
                                                                                                      # #  ( )                                          
                                                                                                   ___#_#___|__                                         
                                                                                               _  |____________|  _                                     
                                                                                        _=====| | |            | | |==== _                              
                                                                                  =====| |.---------------------------. | |====                         
                                                                    <--------------------'   .  .  .  .  .  .  .  .   '--------------/                  
                                                                      \                                                             /                   
                                                                       \___________________________________________________________/                    
                                                                   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                
                                                                 wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww               
                                                                    wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                 
''')


def sound(sound_duration):
    if sound_duration == 'long':
        duration = 0.9
        freq = 300
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    else:
        duration = 0.1
        freq = 460
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))


def print_radars(player, tries_1_list, tries_2_list):

    if player == '1':
        print(
            "                                                    *****IT'S YOUR TURN*****")
    if player == '2':
        print("                                                                                        *****IT'S YOUR TURN*****")
    print('''
                                                        1   2   3   4   5                     1   2   3   4   5

                                                    A   {}   {}   {}   {}   {}                 A   {}   {}   {}   {}   {}

                                                    B   {}   {}   {}   {}   {}                 B   {}   {}   {}   {}   {}

                                                    C   {}   {}   {}   {}   {}                 C   {}   {}   {}   {}   {}

                                                    D   {}   {}   {}   {}   {}                 D   {}   {}   {}   {}   {}

                                                    E   {}   {}   {}   {}   {}                 E   {}   {}   {}   {}   {}

                '''.format(tries_1_list[0][0], tries_1_list[0][1], tries_1_list[0][2], tries_1_list[0][3], tries_1_list[0][4], tries_2_list[0][0], tries_2_list[0][1], tries_2_list[0][2], tries_2_list[0][3], tries_2_list[0][4], tries_1_list[1][0], tries_1_list[1][1], tries_1_list[1][2], tries_1_list[1][3], tries_1_list[1][4], tries_2_list[1][0], tries_2_list[1][1], tries_2_list[1][2], tries_2_list[1][3], tries_2_list[1][4], tries_1_list[2][0], tries_1_list[2][1], tries_1_list[2][2], tries_1_list[2][3], tries_1_list[2][4], tries_2_list[2][0], tries_2_list[2][1], tries_2_list[2][2], tries_2_list[2][3], tries_2_list[2][4], tries_1_list[3][0], tries_1_list[3][1], tries_1_list[3][2], tries_1_list[3][3], tries_1_list[3][4], tries_2_list[3][0], tries_2_list[3][1], tries_2_list[3][2], tries_2_list[3][3], tries_2_list[3][4], tries_1_list[4][0], tries_1_list[4][1], tries_1_list[4][2], tries_1_list[4][3], tries_1_list[4][4], tries_2_list[4][0], tries_2_list[4][1], tries_2_list[4][2], tries_2_list[4][3], tries_2_list[4][4]))


def init_list():

    init_board = [['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], [
        '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.']]
    return init_board


def print_board(board):

    print('''
                                                                                1   2   3   4   5

                                                                            A   {}   {}   {}   {}   {}

                                                                            B   {}   {}   {}   {}   {}

                                                                            C   {}   {}   {}   {}   {}

                                                                            D   {}   {}   {}   {}   {}

                                                                            E   {}   {}   {}   {}   {}
        '''.format(board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[1][0], board[1][1], board[1][2],
                   board[1][3], board[1][4], board[2][0], board[2][1], board[2][2], board[2][3], board[2][4],
                   board[3][0], board[3][1], board[3][2], board[3][3], board[3][4],
                   board[4][0], board[4][1], board[4][2], board[4][3], board[4][4]))


def verificare_placement(placement_list, row, col):
    if row == 0 and col == 0:
        if placement_list[1][0] == placement_list[0][1] == placement_list[0][0] == '.':
            return True
        else:
            return False
    if row == 0 and col == 4:
        if placement_list[0][3] == placement_list[1][4] == placement_list[0][4] == '.':
            return True
        else:
            return False
    if row == 4 and col == 4:
        if placement_list[4][3] == placement_list[3][4] == placement_list[4][4] == '.':
            return True
        else:
            return False
    if row == 4 and col == 0:
        if placement_list[3][0] == placement_list[4][1] == placement_list[4][0] == '.':
            return True
        else:
            return False
    if row == 4:
        if placement_list[row-1][col] == placement_list[row][col+1] == placement_list[row][col-1] == placement_list[row][col] == '.':
            return True
        else:
            return False
    elif col == 4:
        if placement_list[row+1][col] == placement_list[row-1][col] == placement_list[row][col-1] == placement_list[row][col] == '.':
            return True
        else:
            return False
    elif row == 0:
        if placement_list[row+1][col] == placement_list[row][col+1] == placement_list[row][col-1] == placement_list[row][col] == '.':
            return True
        else:
            return False
    elif col == 0:
        if placement_list[row+1][col] == placement_list[row-1][col] == placement_list[row][col+1] == placement_list[row][col] == '.':
            return True
        else:
            return False
    elif placement_list[row+1][col] == placement_list[row-1][col] == placement_list[row][col+1] == placement_list[row][col-1] == placement_list[row][col] == '.':
        return True
    else:
        return False


def placement1(placement1_list):
    shipsx1 = 3
    shipsx2 = 2
    while shipsx1 > 0:
        print('\n\n\n\n\n\n\n\n\n\n')
        print_board(placement1_list)
        ships = shipsx1 + shipsx2
        print("Player 1, you have {} ships left to place".format(ships))
        print("Now you should place a 1 block ship")
        place = str(
            input("Choose a position to place your ship: ").lower())
        if len(place) == 2:
            if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"] and len(place) == 2:
                row = ord(place[0])-97
                col = int(place[1])-1
                verificare_placement(placement1_list, row, col)
                if verificare_placement(placement1_list, row, col) == True:
                    placement1_list[row][col] = "X"
                    shipsx1 -= 1
                elif verificare_placement(placement1_list, row, col) == False:
                    os.system("clear")
                    print("\n\n\n\nYour ships are too close")
                    continue
                os.system("clear")
            else:
                os.system("clear")
                print("\n\n\n\nInvalid input!")
                continue
        else:
            os.system("clear")
            print("\n\n\n\nInvalid input!")
            continue
    while shipsx2 > 0:
        print('\n\n\n\n\n\n\n\n\n')
        print_board(placement1_list)
        ships = shipsx1 + shipsx2
        print("Player 1, you have {} ships left to place".format(ships))
        print("Now you should place a 2 blocks ship")
        place = str(
            input("Choose a position to place your ship's head: ").lower())
        if len(place) == 2:
            if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"]:
                row = ord(place[0])-97
                col = int(place[1])-1
                verificare_placement(placement1_list, row, col)
                if verificare_placement(placement1_list, row, col) == True:
                    direction = input(
                        "Choose on which direction you want to place your ship (N,S,E,W) :").lower()
                    if direction in ["n", "s", "e", "w"]:
                        if direction == "n":
                            if row == 0:
                                os.system("clear")
                                print(
                                    "\n\n\n\nIn this case the world is flat and you can't cross the edges")
                                continue
                            verificare_placement(placement1_list, row-1, col)
                            if verificare_placement(placement1_list, row-1, col) == True:
                                placement1_list[row][col] = "X"
                                placement1_list[row-1][col] = "X"
                                shipsx2 -= 1
                                os.system("clear")
                            elif verificare_placement(placement1_list, row-1, col) == False:
                                os.system("clear")
                                print("\n\n\n\nYour ships are too close!")
                                continue
                        if direction == "s":
                            if row == 4:
                                os.system("clear")
                                print(
                                    "\n\n\n\nIn this case the world is flat and you can't cross the edges")
                                continue
                            verificare_placement(placement1_list, row+1, col)
                            if verificare_placement(placement1_list, row+1, col) == True:
                                placement1_list[row][col] = "X"
                                placement1_list[row+1][col] = "X"
                                shipsx2 -= 1
                                os.system("clear")
                            elif verificare_placement(placement1_list, row+1, col) == False:
                                os.system("clear")
                                print("\n\n\n\nYour ships are too close!")
                                continue
                        if direction == "e":
                            if col == 4:
                                os.system("clear")
                                print(
                                    "\n\n\n\nIn this case the world is flat and you can't cross the edges")
                                continue
                            verificare_placement(placement1_list, row, col+1)
                            if verificare_placement(placement1_list, row, col+1) == True:
                                placement1_list[row][col] = "X"
                                placement1_list[row][col+1] = "X"
                                shipsx2 -= 1
                                os.system("clear")
                            elif verificare_placement(placement1_list, row, col+1) == False:
                                os.system("clear")
                                print("\n\n\n\nYour ships are too close!")
                                continue
                        if direction == "w":
                            if col == 0:
                                os.system("clear")
                                print(
                                    "\n\n\n\nIn this case the world is flat and you can't cross the edges")
                                continue
                            verificare_placement(placement1_list, row, col-1)
                            if verificare_placement(placement1_list, row, col-1) == True:
                                placement1_list[row][col] = "X"
                                placement1_list[row][col-1] = "X"
                                shipsx2 -= 1
                                os.system("clear")
                            elif verificare_placement(placement1_list, row, col-1) == False:
                                os.system("clear")
                                print("\n\n\n\nYour ships are too close!")
                                continue
                    else:
                        os.system("clear")
                        print("\n\n\n\nInvalid input!")
                        continue
                elif verificare_placement(placement1_list, row, col) == False:
                    os.system("clear")
                    print("\n\n\n\nYour ships are too close")
                    continue
            else:
                os.system("clear")
                print("\n\n\n\nInvalid input!")
                continue
        else:
            os.system("clear")
            print("\n\n\n\nInvalid input!")
            continue
    return placement1_list


def placement2(placement2_list):
    shipsx1 = 3
    shipsx2 = 2
    while shipsx1 > 0:
        print('\n\n\n\n\n\n\n\n\n\n')
        print_board(placement2_list)
        ships = shipsx1 + shipsx2
        print("Player 2, you have {} ships left to place".format(ships))
        print("Now you should place a 1 block ship")
        place = str(
            input("Choose a position to place your ship: ").lower())
        if len(place) == 2:
            if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"] and len(place) == 2:
                row = ord(place[0])-97
                col = int(place[1])-1
                verificare_placement(placement2_list, row, col)
                if verificare_placement(placement2_list, row, col) == True:
                    placement2_list[row][col] = "X"
                    shipsx1 -= 1
                elif verificare_placement(placement2_list, row, col) == False:
                    os.system("clear")
                    print("\n\n\n\nYour ships are too close")
                    continue
                os.system("clear")
            else:
                os.system("clear")
                print("\n\n\n\nInvalid input!")
                continue
        else:
            os.system("clear")
            print("\n\n\n\nInvalid input!")
            continue

    while shipsx2 > 0:
        print('\n\n\n\n\n\n\n\n\n\n')
        print_board(placement2_list)
        ships = shipsx1 + shipsx2
        print("Player 2, you have {} ships left to place".format(ships))
        print("Now you should place a 2 blocks ship")
        place = str(
            input("Choose a position to place your ship's head: ").lower())
        if len(place) == 2:
            if place[0] in ["a", "b", "c", "d", "e"] and place[1] in ["1", "2", "3", "4", "5"] and len(place) == 2:
                row = ord(place[0])-97
                col = int(place[1])-1
                verificare_placement(placement2_list, row, col)
                if verificare_placement(placement2_list, row, col) == True:
                    direction = input(
                        "Choose on which direction you want to place your ship (N,S,E,W) :").lower()
                    if direction in ["n", "s", "e", "w"]:
                        if direction == "n":
                            if row == 0:
                                os.system("clear")
                                print(
                                    "\n\n\n\nIn this case the world is flat and you can't cross the edges")
                                continue
                            verificare_placement(placement2_list, row-1, col)
                            if verificare_placement(placement2_list, row-1, col) == True:
                                placement2_list[row][col] = "X"
                                placement2_list[row-1][col] = "X"
                                shipsx2 -= 1
                                os.system("clear")
                            elif verificare_placement(placement2_list, row-1, col) == False:
                                os.system("clear")
                                print("\n\n\n\nYour ships are too close!")
                                continue
                        if direction == "s":
                            if row == 4:
                                os.system("clear")
                                print(
                                    "\n\n\n\nIn this case the world is flat and you can't cross the edges")
                                continue
                            verificare_placement(placement2_list, row+1, col)
                            if verificare_placement(placement2_list, row+1, col) == True:
                                placement2_list[row][col] = "X"
                                placement2_list[row+1][col] = "X"
                                shipsx2 -= 1
                                os.system("clear")
                            elif verificare_placement(placement2_list, row+1, col) == False:
                                os.system("clear")
                                print("\n\n\n\nYour ships are too close!")
                                continue
                        if direction == "e":
                            if col == 4:
                                os.system("clear")
                                print(
                                    "\n\n\n\nIn this case the world is flat and you can't cross the edges")
                                continue
                            verificare_placement(placement2_list, row, col+1)
                            if verificare_placement(placement2_list, row, col+1) == True:
                                placement2_list[row][col] = "X"
                                placement2_list[row][col+1] = "X"
                                shipsx2 -= 1
                                os.system("clear")
                            elif verificare_placement(placement2_list, row, col+1) == False:
                                os.system("clear")
                                print("\n\n\n\nYour ships are too close!")
                                continue
                        if direction == "w":
                            if col == 0:
                                os.system("clear")
                                print(
                                    "\n\n\n\nIn this case the world is flat and you can't cross the edges")
                                continue
                            verificare_placement(placement2_list, row, col-1)
                            if verificare_placement(placement2_list, row, col-1) == True:
                                placement2_list[row][col] = "X"
                                placement2_list[row][col-1] = "X"
                                shipsx2 -= 1
                                os.system("clear")
                            elif verificare_placement(placement2_list, row, col-1) == False:
                                os.system("clear")
                                print("\n\n\n\nYour ships are too close!")
                                continue
                    else:
                        os.system("clear")
                        print("\n\n\n\nInvalid input!")
                        continue
                elif verificare_placement(placement2_list, row, col) == False:
                    os.system("clear")
                    print("\n\n\n\nYour ships are too close")
                    continue
            else:
                os.system("clear")
                print("\n\n\n\nInvalid input!")
                continue
        else:
            os.system("clear")
            print("\n\n\n\nInvalid input!")
            continue
    return placement2_list


def surroundings_forging_list(other_player_board, row, column, marked_board):
    if 0 < row < 4 and 0 < column < 4:
        surroundings_other_player_board = [other_player_board[row - 1][column], other_player_board[row + 1]
                                           [column], other_player_board[row][column + 1], other_player_board[row][column - 1]]
        surroundings_marked_board = [marked_board[row - 1][column], marked_board[row + 1]
                                     [column], marked_board[row][column + 1], marked_board[row][column - 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif 0 < row < 4 and column == 0:
        surroundings_other_player_board = [other_player_board[row - 1][column],
                                           other_player_board[row + 1][column], other_player_board[row][column + 1]]
        surroundings_marked_board = [marked_board[row - 1][column],
                                     marked_board[row + 1][column], marked_board[row][column + 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif 0 < row < 4 and column == 4:
        surroundings_other_player_board = [other_player_board[row - 1][column],
                                           other_player_board[row + 1][column], other_player_board[row][column - 1]]
        surroundings_marked_board = [marked_board[row - 1][column],
                                     marked_board[row + 1][column], marked_board[row][column - 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif row == 0 and 0 < column < 4:
        surroundings_other_player_board = [other_player_board[row + 1][column],
                                           other_player_board[row][column + 1], other_player_board[row][column - 1]]
        surroundings_marked_board = [marked_board[row + 1][column],
                                     marked_board[row][column + 1], marked_board[row][column - 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif row == 4 and 0 < column < 4:
        surroundings_other_player_board = [other_player_board[row - 1][column],
                                           other_player_board[row][column + 1], other_player_board[row][column - 1]]
        surroundings_marked_board = [marked_board[row - 1][column],
                                     marked_board[row][column + 1], marked_board[row][column - 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif row == 0 and column == 0:
        surroundings_other_player_board = [
            other_player_board[row + 1][column], other_player_board[row][column + 1]]
        surroundings_marked_board = [
            marked_board[row + 1][column], marked_board[row][column + 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif row == 0 and column == 4:
        surroundings_other_player_board = [
            other_player_board[row + 1][column], other_player_board[row][column - 1]]
        surroundings_marked_board = [
            marked_board[row + 1][column], marked_board[row][column - 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif row == 4 and column == 0:
        surroundings_other_player_board = [
            other_player_board[row - 1][column], other_player_board[row][column + 1]]
        surroundings_marked_board = [
            marked_board[row - 1][column], marked_board[row][column + 1]]
        return surroundings_other_player_board, surroundings_marked_board

    elif row == 4 and column == 4:
        surroundings_other_player_board = [
            other_player_board[row - 1][column], other_player_board[row][column - 1]]
        surroundings_marked_board = [
            marked_board[row - 1][column], marked_board[row][column - 1]]
        return surroundings_other_player_board, surroundings_marked_board


def changing_first_h_for_2xship(row, column, marked_board):
    if 0 < row < 4 and 0 < column < 4:
        surroundings_marked_board = [marked_board[row - 1][column], marked_board[row + 1]
                                     [column], marked_board[row][column + 1], marked_board[row][column - 1]]
        if surroundings_marked_board[0] == 'H':
            return (row - 1, column)

        elif surroundings_marked_board[1] == 'H':
            return (row + 1, column)

        elif surroundings_marked_board[2] == 'H':
            return (row, column + 1)

        else:
            return (row, column - 1)

    elif 0 < row < 4 and column == 0:
        surroundings_marked_board = [marked_board[row - 1][column],
                                     marked_board[row + 1][column], marked_board[row][column + 1]]
        if surroundings_marked_board[0] == 'H':
            return (row - 1, column)

        elif surroundings_marked_board[1] == 'H':
            return (row + 1, column)

        else:
            return (row, column + 1)

    elif 0 < row < 4 and column == 4:
        surroundings_marked_board = [marked_board[row - 1][column],
                                     marked_board[row + 1][column], marked_board[row][column - 1]]
        if surroundings_marked_board[0] == 'H':
            return (row - 1, column)

        elif surroundings_marked_board[1] == 'H':
            return (row + 1, column)

        else:
            return (row, column - 1)

    elif row == 0 and 0 < column < 4:
        surroundings_marked_board = [marked_board[row + 1][column],
                                     marked_board[row][column + 1], marked_board[row][column - 1]]
        if surroundings_marked_board[0] == 'H':
            return (row + 1, column)

        elif surroundings_marked_board[1] == 'H':
            return (row, column+1)

        else:
            return (row, column - 1)

    elif row == 4 and 0 < column < 4:
        surroundings_marked_board = [marked_board[row - 1][column],
                                     marked_board[row][column + 1], marked_board[row][column - 1]]
        if surroundings_marked_board[0] == 'H':
            return (row - 1, column)

        elif surroundings_marked_board[1] == 'H':
            return (row, column+1)

        else:
            return (row, column - 1)

    elif row == 0 and column == 0:
        surroundings_marked_board = [
            marked_board[row + 1][column], marked_board[row][column + 1]]
        if surroundings_marked_board[0] == 'H':
            return (row + 1, column)

        else:
            return (row, column + 1)

    elif row == 0 and column == 4:
        surroundings_marked_board = [
            marked_board[row + 1][column], marked_board[row][column - 1]]
        if surroundings_marked_board[0] == 'H':
            return (row + 1, column)

        else:
            return (row, column - 1)

    elif row == 4 and column == 0:
        surroundings_marked_board = [
            marked_board[row - 1][column], marked_board[row][column + 1]]
        if surroundings_marked_board[0] == 'H':
            return (row - 1, column)

        else:
            return (row, column + 1)

    elif row == 4 and column == 4:
        surroundings_marked_board = [
            marked_board[row - 1][column], marked_board[row][column - 1]]
        if surroundings_marked_board[0] == 'H':
            return (row - 1, column)

        else:
            return (row, column - 1)


def mark(other_player_board, row, column, marked_board):
    new_row = 9
    new_col = 9
    surroundings_other_player_board, surroundings_marked_board = surroundings_forging_list(
        other_player_board, row, column, marked_board)
    if other_player_board[row][column] == '.':
        marked_board[row][column] = 'M'
        print("\n\n\n\nYou've missed!")
        subprocess.call(['speech-dispatcher'])
        subprocess.call(['spd-say', '"you missed "'])
        time.sleep(1)

    elif marked_board[row][column] in ['M', 'S', 'H']:
        print("\n\n\n\nOops! Already tried this position. Choose a diferent one next time.")
        subprocess.call(['speech-dispatcher'])
        subprocess.call(['spd-say', '"oops"'])
        time.sleep(1)

    elif other_player_board[row][column] == 'X' and surroundings_other_player_board.count("X") == 0:
        marked_board[row][column] = "S"
        print("\n\n\n\nYou've sunk a ship")
        sound('long')
        subprocess.call(['speech-dispatcher'])
        subprocess.call(['spd-say', '"ship sunk"'])
        time.sleep(1)

    elif other_player_board[row][column] == 'X' and surroundings_marked_board.count("H") == 1:
        marked_board[row][column] = "S"
        new_row = changing_first_h_for_2xship(row, column, marked_board)[0]
        new_col = changing_first_h_for_2xship(row, column, marked_board)[1]
        marked_board[new_row][new_col] = "S"
        print("\n\n\n\nYou've sunk a ship")
        sound('long')
        subprocess.call(['speech-dispatcher'])
        subprocess.call(['spd-say', '"ship sunk"'])
        time.sleep(1)

    elif other_player_board[row][column] == 'X' and surroundings_other_player_board.count("X") == 1:
        marked_board[row][column] = "H"
        print("You've hit a ship!")
        sound('short')
        subprocess.call(['speech-dispatcher'])
        subprocess.call(['spd-say', '"ship hit"'])
        time.sleep(1)

    return marked_board


def get_shot_input(player):
    while True:
        shot = str(input("Player " + player +
                         " choose a position to shot: ").lower())
        if len(shot) == 2:
            if shot[0] in ["a", "b", "c", "d", "e"] and shot[1] in ["1", "2", "3", "4", "5"]:
                row = ord(shot[0])-97
                col = int(shot[1])-1
                return (row, col)
            else:
                print("Invalid input. Try again.")
                continue
        else:
            print("\n\n\n\nInvalid input!")
            continue


def get_ai_move(tries_2_list):
    while True:
        row = random.choice([0, 1, 2, 3, 4])
        col = random.choice([0, 1, 2, 3, 4])
        if tries_2_list[row][col] == ".":
            return (row, col)
        else:
            continue


def follow_the_H(tries_2_list, row, col):
    ai_row = 9
    ai_col = 9
    for i in range(len(tries_2_list)):
        for j in range(len(tries_2_list[i])):
            for h in tries_2_list[i][j]:
                if h == "H":
                    ai_row = i
                    ai_col = j
                    key = 1
                    return (ai_row, ai_col, key)
                else:
                    key = 2
                    return (row, col, key)


def shoot_H_ai(placement_list, row, col):
    if row == 0 and col == 0:
        if placement_list[1][0] == '.':
            airow = 1
            aicol = 0
            return (airow, aicol)
        elif placement_list[0][1] == ".":
            airow = 0
            aicol = 1
            return (airow, aicol)
    if row == 0 and col == 4:
        if placement_list[0][3] == '.':
            airow = 0
            aicol = 3
            return (airow, aicol)
        elif placement_list[1][4] == '.':
            airow = 1
            aicol = 4
            return (airow, aicol)
    if row == 4 and col == 4:
        if placement_list[4][3] == '.':
            airow = 4
            aicol = 3
            return (airow, aicol)
        elif placement_list[3][4] == '.':
            airow = 3
            aicol = 4
            return (airow, aicol)
    if row == 4 and col == 0:
        if placement_list[3][0] == '.':
            airow = 3
            aicol = 0
            return (airow, aicol)
        if placement_list[4][1] == '.':
            airow = 4
            aicol = 1
            return (airow, aicol)
    if row == 4:
        if placement_list[row-1][col] == '.':
            airow = row - 1
            aicol = col
            return (airow, aicol)
        if placement_list[row][col+1] == '.':
            aicol = col + 1
            airow = row
            return (airow, aicol)
        if placement_list[row][col-1] == '.':
            aicol = col-1
            airow = row
            return (airow, aicol)

    elif col == 4:
        if placement_list[row+1][col] == '.':
            airow = row + 1
            aicol = col
            return (airow, aicol)
        if placement_list[row-1][col] == '.':
            airow = row - 1
            aicol = col
            return (airow, aicol)
        if placement_list[row][col-1] == '.':
            aicol = col - 1
            airow = row
            return (airow, aicol)
    elif row == 0:
        if placement_list[row+1][col] == '.':
            airow = row + 1
            aicol = col
            return (airow, aicol)

        if placement_list[row][col+1] == '.':
            aicol = col+1
            airow = row
            return (airow, aicol)

        if placement_list[row][col-1] == '.':
            aicol = col - 1
            airow = row
            return (airow, aicol)

    elif col == 0:
        if placement_list[row+1][col] == '.':
            airow = row + 1
            aicol = col
            return (airow, aicol)

        if placement_list[row-1][col] == '.':
            airow = row - 1
            aicol = col
            return (airow, aicol)

        if placement_list[row][col+1] == '.':
            aicol = col + 1
            airow = row
            return (airow, aicol)

    else:
        if placement_list[row+1][col] == ".":
            airow = row + 1
            aicol = col
            return (airow, aicol)

        if placement_list[row-1][col] == ".":
            airow = row - 1
            aicol = col
            return (airow, aicol)

        if placement_list[row][col+1] == ".":
            aicol = col + 1
            airow = row
            return (airow, aicol)

        if placement_list[row][col-1] == ".":
            aicol = col - 1
            airow = row
            return (airow, aicol)


def has_won(board, player):
    count = 0
    for i in board:
        for j in i:
            if j == "S":
                count += 1
            else:
                continue
    if count == 7:
        return True
    else:
        return False


def battleship(type_of_game):

    os.system("clear")
    board = init_list()
    tries_1_list = copy.deepcopy(board)
    tries_2_list = copy.deepcopy(board)
    player = ""
    count = 0
    placement1_list = copy.deepcopy(board)
    placement2_list = copy.deepcopy(board)
    print("\n\n\n\n\n\t\t\t\t\t\t\t\tPlayer2, go away and let player1 place his ships\n")
    placement1(placement1_list)
    if type_of_game == '1':
        print(
            "\n\n\n\n\n\t\t\t\t\t\t\t\tPlayer1, go away and let player2 place his ships\n")
        input("Player 2 when you are ready press Enter...")
        placement2(placement2_list)
    elif type_of_game == '2':
        placement2_list = [["X", ".", ".", ".", "X"], [".", ".", ".", ".", "X"], [".", ".", "X", ".", "."], [
            "X", ".", ".", ".", "."], [".", "X", "X", ".", "."]]  # de facut functie cu random
    while True:
        if count % 2 == 0:
            player = "1"
            subprocess.call(['speech-dispatcher'])
            subprocess.call(['spd-say', '"player one"'])
            print('\n\n\n\n\n\n\n\n\n\n')
            print_radars(player, tries_1_list, tries_2_list)
            (row, col) = get_shot_input(player)
            tries_1_list = mark(placement2_list, row, col, tries_1_list)
            print_radars(player, tries_1_list, tries_2_list)
            if has_won(tries_1_list, player) == True:
                os.system("clear")
                print('\n\n\n\n\n\n\n\n\n\n')
                print('\t\t\t\t\t\t\t\t**************************************')
                print("\t\t\t\t\t\t\t\t\t***** Player " + player + " won! *****")
                print('\t\t\t\t\t\t\t\t**************************************')
                print('\n\n\n\n\n\n\n\n\n\n')
                subprocess.call(['speech-dispatcher'])
                subprocess.call(['spd-say', '"game won"'])
                time.sleep(1)
                break
            os.system("clear")
        else:
            player = "2"
            subprocess.call(['speech-dispatcher'])
            subprocess.call(['spd-say', '"player two"'])
            print('\n\n\n\n\n\t\t\t\t\t\t\t\t')
            print_radars(player, tries_1_list, tries_2_list)
            if type_of_game == '1':
                (row, col) = get_shot_input(player)
            elif type_of_game == '2':
                follow_the_H(tries_2_list, row, col)
                if follow_the_H(tries_2_list, row, col)[2] == 1:
                    # print('intra in 852')
                    # (row, col) = (follow_the_H(tries_2_list, row, col)
                    #               [0], follow_the_H(tries_2_list, row, col)[1])
                    (row, col) = shoot_H_ai(tries_2_list,
                                            follow_the_H(
                                                tries_2_list, row, col)
                                            [0], follow_the_H(tries_2_list, row, col)[1])  # de verificat row si col
                    # (row, col) = get_ai_move(tries_2_list)
                    time.sleep(1)
                elif follow_the_H(tries_2_list, row, col)[2] == 2:
                    # print('intra in elif')
                    (row, col) = get_ai_move(tries_2_list)
                    time.sleep(2)
            tries_2_list = mark(placement1_list, row, col, tries_2_list)
            print_radars(player, tries_1_list, tries_2_list)
            if has_won(tries_2_list, player) == True:
                os.system("clear")
                print('\n\n\n\n\n\n\n\n\n\n')
                print('\t\t\t\t\t\t\t\t**************************************')
                print("\t\t\t\t\t\t\t\t\t***** Player " + player + " won! *****")
                print('\t\t\t\t\t\t\t\t**************************************')
                print('\n\n\n\n\n\n\n\n\n\n')
                subprocess.call(['speech-dispatcher'])
                subprocess.call(['spd-say', '"game won"'])
                time.sleep(1)
                break
            os.system("clear")
        count += 1


def main():
    os.system("clear")
    cover()
    subprocess.call(['speech-dispatcher'])
    subprocess.call(['spd-say', '"team team brings you battleship"'])
    time.sleep(2)
    os.system("clear")
    while True:
        print('\n\n\n\n\n\n\n\n\n\n')
        print("\t1. Player vs Player")
        print("\t2. Player vs AI")
        print("\t3. 'quit' for quitting")

        game = input("What type of game?: ")
        sound('short')
        if game == "1":
            print("\n Player vs Player game!")
            battleship(game)
        elif game == "2":
            print("\n Player vs AI!")
            battleship(game)
        elif game == "quit":
            break


if __name__ == "__main__":
    main()
