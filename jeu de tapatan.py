# jeu de tapatan
#########################################
# groupe MPCI 6
# OUCHERIF Lounis
# ZAGBAHI Godi
# LIGER Arthur
# MORCOS DOUEIHY Jean-Paul
# ROBINSON Andry
#
# https://github.com/uvsq22011110/jeu_Tapatan
###################################
import tkinter as tk

root = tk.Tk()

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600

intersection_coords = [100, 300, 500]

# Different colors in the game
color_player_one = "white"
color_player_two = "black"

# Different outline colors in the game
outline_selected = "yellow"
outline_white = "white"
outline_black = "black"

# For first turn and counting
nb_tour = 1

# For selection and showing possible moves
selected = 0
free = []

# Lists that will contain the white and black pieces respectively, will be used for the first moves
white_pieces = []
black_pieces = []

# Name of the piece created when selected = 1
selected_piece = 0

# The intersections coordinates, will be used in the mid game
coords_int_1 = [70, 70, 130, 130]
coords_int_2 = [270, 70, 330, 130]
coords_int_3 = [470, 70, 530, 130]

coords_int_4 = [70, 270, 130, 330]
coords_int_5 = [270, 270, 330, 330]
coords_int_6 = [470, 270, 530, 330]

coords_int_7 = [70, 470, 130, 530]
coords_int_8 = [270, 470, 330, 530]
coords_int_9 = [470, 470, 530, 530]

# Values from 1 to 9, corresponding to the place of the move
place = 0

# List to see which intersections are available. Possible values: 0 for available, 1 for white and 2 for black
for i in range(3):
    intersection_availibility = [[0 for i in range(3)] for j in range(3)]

# For the score
sj1=0
sj2=0
winner = 0

# To count games and change sides from game to game
game = 1
joueur_1 = "white pieces"
joueur_2 = "black pieces"

# For a draw
egalite = []


# Functions

def first_moves(event):
    global intersection_availibility, nb_tour, white_pieces, black_pieces, joueur_1, joueur_2, game

    x_event, y_event = event.x, event.y


    if 90 < x_event < 110 and 90 < y_event < 110 and intersection_availibility[0][0] == 0:
        if nb_tour % 2 == 1:
            canvas.coords(white_pieces[0], 70, 70, 130, 130)
            white_pieces.remove(white_pieces[0])
            intersection_availibility[0][0] = 1
            nb_tour += 1
            win()
        elif nb_tour % 2 == 0:
            canvas.coords(black_pieces[0], 70, 70, 130, 130)
            black_pieces.remove(black_pieces[0])
            intersection_availibility[0][0] = 2
            nb_tour += 1
            win()
    if 290 < x_event < 310 and 90 < y_event < 110 and intersection_availibility[0][1] == 0:
        if nb_tour % 2 == 1:
            canvas.coords(white_pieces[0], 270, 70, 330, 130)
            white_pieces.remove(white_pieces[0])
            intersection_availibility[0][1] = 1
            nb_tour += 1
            win()
        elif nb_tour % 2 == 0:
            canvas.coords(black_pieces[0], 270, 70, 330, 130)
            black_pieces.remove(black_pieces[0])
            intersection_availibility[0][1] = 2
            nb_tour += 1
            win()
    if 490 < x_event < 510 and 90 < y_event < 110 and intersection_availibility[0][2] == 0:
        if nb_tour % 2 == 1:
            canvas.coords(white_pieces[0], 470, 70, 530, 130)
            white_pieces.remove(white_pieces[0])
            intersection_availibility[0][2] = 1
            nb_tour += 1
            win()
        elif nb_tour % 2 == 0:
            canvas.coords(black_pieces[0], 470, 70, 530, 130)
            black_pieces.remove(black_pieces[0])
            intersection_availibility[0][2] = 2
            nb_tour += 1
            win()

    if 90 < x_event < 110 and 290 < y_event < 310 and intersection_availibility[1][0] == 0:
        if nb_tour % 2 == 1:
            canvas.coords(white_pieces[0], 70, 270, 130, 330)
            white_pieces.remove(white_pieces[0])
            intersection_availibility[1][0] = 1
            nb_tour += 1
            win()
        elif nb_tour % 2 == 0:
            canvas.coords(black_pieces[0], 70, 270, 130, 330)
            black_pieces.remove(black_pieces[0])
            intersection_availibility[1][0] = 2
            nb_tour += 1
            win()
    if 290 < x_event < 310 and 290 < y_event < 310 and intersection_availibility[1][1] == 0:
        if nb_tour % 2 == 1:
            canvas.coords(white_pieces[0], 270, 270, 330, 330)
            white_pieces.remove(white_pieces[0])
            intersection_availibility[1][1] = 1
            nb_tour += 1
            win()
        elif nb_tour % 2 == 0:
            canvas.coords(black_pieces[0], 270, 270, 330, 330)
            black_pieces.remove(black_pieces[0])
            intersection_availibility[1][1] = 2
            nb_tour += 1
            win()
    if 490 < x_event < 510 and 290 < y_event < 310 and intersection_availibility[1][2] == 0:
        if nb_tour % 2 == 1:
            canvas.coords(white_pieces[0], 470, 270, 530, 330)
            white_pieces.remove(white_pieces[0])
            intersection_availibility[1][2] = 1
            nb_tour += 1
            win()
        elif nb_tour % 2 == 0:
            canvas.coords(black_pieces[0], 470, 270, 530, 330)
            black_pieces.remove(black_pieces[0])
            intersection_availibility[1][2] = 2
            nb_tour += 1
            win()

    if 90 < x_event < 110 and 490 < y_event < 510 and intersection_availibility[2][0] == 0:
        if nb_tour % 2 == 1:
            canvas.coords(white_pieces[0], 70, 470, 130, 530)
            white_pieces.remove(white_pieces[0])
            intersection_availibility[2][0] = 1
            nb_tour += 1
            win()
        elif nb_tour % 2 == 0:
            canvas.coords(black_pieces[0], 70, 470, 130, 530)
            black_pieces.remove(black_pieces[0])
            intersection_availibility[2][0] = 2
            nb_tour += 1
            win()
    if 290 < x_event < 310 and 490 < y_event < 510 and intersection_availibility[2][1] == 0:
        if nb_tour % 2 == 1:
            canvas.coords(white_pieces[0], 270, 470, 330, 530)
            white_pieces.remove(white_pieces[0])
            intersection_availibility[2][1] = 1
            nb_tour += 1
            win()
        elif nb_tour % 2 == 0:
            canvas.coords(black_pieces[0], 270, 470, 330, 530)
            black_pieces.remove(black_pieces[0])
            intersection_availibility[2][1] = 2
            nb_tour += 1
            win()
    if 490 < x_event < 510 and 490 < y_event < 510 and intersection_availibility[2][2] == 0:
        if nb_tour % 2 == 1:
            canvas.coords(white_pieces[0], 470, 470, 530, 530)
            white_pieces.remove(white_pieces[0])
            intersection_availibility[2][2] = 1
            nb_tour += 1
            win()
        elif nb_tour % 2 == 0:
            canvas.coords(black_pieces[0], 470, 470, 530, 530)
            black_pieces.remove(black_pieces[0])
            intersection_availibility[2][2] = 2
            nb_tour += 1
            win()

    if nb_tour == 7:
        canvas.bind('<Button-1>', mid_game)
        white_pieces = [white_piece_1, white_piece_2, white_piece_3]
        black_pieces = [black_piece_1, black_piece_2, black_piece_3]
        win()



def mid_game(event):
    global nb_tour, intersection_availibility, selected, free, selected_piece, white_pieces, white_piece_1, white_piece_2, white_piece_3, black_piece_1, black_piece_2, black_piece_3, place, coords_int_1, coords_int_2, coords_int_3, coords_int_4, coords_int_5, coords_int_6, coords_int_7, coords_int_8, coords_int_9, joueur_1, joueur_2, game, egalite

    x_event, y_event = event.x, event.y
   
# Intersection[0][0]
    if intersection_availibility[0][0] != 0 and 70 < x_event < 130 and 70 < y_event < 130 and selected == 0:
        if nb_tour % 2 == 1 and intersection_availibility[0][0] == 1:
            selected_piece = canvas.create_oval(70, 70, 130, 130, fill=color_player_one, outline=outline_selected, width=4)
            place = 1
            selected = 1
        elif nb_tour % 2 == 0 and intersection_availibility[0][0] == 2:
            selected_piece = canvas.create_oval(70, 70, 130, 130, fill=color_player_two, outline=outline_selected, width=4)
            place = 1
            selected = 1
        if selected == 1:
            if intersection_availibility[0][1] == 0:
                free.append(canvas.create_oval(290, 90, 310, 110, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][0] == 0:
                free.append(canvas.create_oval(90, 290, 110, 310, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][1] == 0:
                free.append(canvas.create_oval(290, 290, 310, 310, fill="black", outline=outline_selected, width=4))
    elif intersection_availibility[0][1] == 0 and selected == 1 and 290 < x_event < 310 and 90 < y_event < 110 and place == 1:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_1:
                canvas.coords(white_piece_1, 270, 70, 330, 130)
            if canvas.coords(white_piece_2) == coords_int_1:
                canvas.coords(white_piece_2, 270, 70, 330, 130)
            if canvas.coords(white_piece_3) == coords_int_1:
                canvas.coords(white_piece_3, 270, 70, 330, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][0] = 0
            intersection_availibility[0][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_1:
                canvas.coords(black_piece_1, 270, 70, 330, 130)
            if canvas.coords(black_piece_2) == coords_int_1:
                canvas.coords(black_piece_2, 270, 70, 330, 130)
            if canvas.coords(black_piece_3) == coords_int_1:
                canvas.coords(black_piece_3, 270, 70, 330, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][0] = 0
            intersection_availibility[0][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][0] == 0 and selected == 1 and 90 < x_event < 110 and 290 < y_event < 310 and place == 1:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_1:
                canvas.coords(white_piece_1, 70, 270, 130, 330)
            if canvas.coords(white_piece_2) == coords_int_1:
                canvas.coords(white_piece_2, 70, 270, 130, 330)
            if canvas.coords(white_piece_3) == coords_int_1:
                canvas.coords(white_piece_3, 70, 270, 130, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][0] = 0
            intersection_availibility[1][0] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_1:
                canvas.coords(black_piece_1, 70, 270, 130, 330)
            if canvas.coords(black_piece_2) == coords_int_1:
                canvas.coords(black_piece_2, 70, 270, 130, 330)
            if canvas.coords(black_piece_3) == coords_int_1:
                canvas.coords(black_piece_3, 70, 270, 130, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][0] = 0
            intersection_availibility[1][0] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][1] == 0 and selected == 1 and 290 < x_event < 310 and 290 < y_event < 310 and place == 1:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_1:
                canvas.coords(white_piece_1, 270, 270, 330, 330)
            if canvas.coords(white_piece_2) == coords_int_1:
                canvas.coords(white_piece_2, 270, 270, 330, 330)
            if canvas.coords(white_piece_3) == coords_int_1:
                canvas.coords(white_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][0] = 0
            intersection_availibility[1][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_1:
                canvas.coords(black_piece_1, 270, 270, 330, 330)
            if canvas.coords(black_piece_2) == coords_int_1:
                canvas.coords(black_piece_2, 270, 270, 330, 330)
            if canvas.coords(black_piece_3) == coords_int_1:
                canvas.coords(black_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][0] = 0
            intersection_availibility[1][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[0][0] != 0 and ((x_event < 70 or x_event > 130) or (y_event < 70 or y_event > 130)) and selected == 1 and place == 1:
        canvas.delete(selected_piece)
        for i in range(len(free)):
            canvas.delete(free[i])
        free = []
        selected = 0

# Intersection[0][1]
    elif intersection_availibility[0][1] != 0 and 270 < x_event < 330 and 70 < y_event < 130 and selected == 0:
        if nb_tour % 2 == 1 and intersection_availibility[0][1] == 1:
            selected_piece = canvas.create_oval(270, 70, 330, 130, fill=color_player_one, outline=outline_selected, width=4)
            place = 2
            selected = 1
        elif nb_tour % 2 == 0 and intersection_availibility[0][1] == 2:
            selected_piece = canvas.create_oval(270, 70, 330, 130, fill=color_player_two, outline=outline_selected, width=4)
            place = 2
            selected = 1
        if selected == 1:
            if intersection_availibility[0][0] == 0:
                free.append(canvas.create_oval(90, 90, 110, 110, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[0][2] == 0:
                free.append(canvas.create_oval(490, 90, 510, 110, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][1] == 0:
                free.append(canvas.create_oval(290, 290, 310, 310, fill="black", outline=outline_selected, width=4))
    elif intersection_availibility[0][0] == 0 and selected == 1 and 90 < x_event < 110 and 90 < y_event < 110 and place == 2:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_2:
                canvas.coords(white_piece_1, 70, 70, 130, 130)
            if canvas.coords(white_piece_2) == coords_int_2:
                canvas.coords(white_piece_2, 70, 70, 130, 130)
            if canvas.coords(white_piece_3) == coords_int_2:
                canvas.coords(white_piece_3, 70, 70, 130, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][1] = 0
            intersection_availibility[0][0] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_2:
                canvas.coords(black_piece_1, 70, 70, 130, 130)
            if canvas.coords(black_piece_2) == coords_int_2:
                canvas.coords(black_piece_2, 70, 70, 130, 130)
            if canvas.coords(black_piece_3) == coords_int_2:
                canvas.coords(black_piece_3, 70, 70, 130, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][1] = 0
            intersection_availibility[0][0] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[0][2] == 0 and selected == 1 and 490 < x_event < 510 and 90 < y_event < 110 and place == 2:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_2:
                canvas.coords(white_piece_1, 470, 70, 530, 130)
            if canvas.coords(white_piece_2) == coords_int_2:
                canvas.coords(white_piece_2, 470, 70, 530, 130)
            if canvas.coords(white_piece_3) == coords_int_2:
                canvas.coords(white_piece_3, 470, 70, 530, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][1] = 0
            intersection_availibility[0][2] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_2:
                canvas.coords(black_piece_1, 470, 70, 530, 130)
            if canvas.coords(black_piece_2) == coords_int_2:
                canvas.coords(black_piece_2, 470, 70, 530, 130)
            if canvas.coords(black_piece_3) == coords_int_2:
                canvas.coords(black_piece_3, 470, 70, 530, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][1] = 0
            intersection_availibility[0][2] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][1] == 0 and selected == 1 and 290 < x_event < 310 and 290 < y_event < 310 and place == 2:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_2:
                canvas.coords(white_piece_1, 270, 270, 330, 330)
            if canvas.coords(white_piece_2) == coords_int_2:
                canvas.coords(white_piece_2, 270, 270, 330, 330)
            if canvas.coords(white_piece_3) == coords_int_2:
                canvas.coords(white_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][1] = 0
            intersection_availibility[1][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_2:
                canvas.coords(black_piece_1, 270, 270, 330, 330)
            if canvas.coords(black_piece_2) == coords_int_2:
                canvas.coords(black_piece_2, 270, 270, 330, 330)
            if canvas.coords(black_piece_3) == coords_int_2:
                canvas.coords(black_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][1] = 0
            intersection_availibility[1][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[0][1] != 0 and ((x_event < 270 or x_event > 330) or (y_event < 70 or y_event > 130)) and selected == 1 and place == 2:
        canvas.delete(selected_piece)
        for i in range(len(free)):
            canvas.delete(free[i])
        free = []
        selected = 0

# Intersection[0][2]
    elif intersection_availibility[0][2] != 0 and 470 < x_event < 530 and 70 < y_event < 130 and selected == 0:
        if nb_tour % 2 == 1 and intersection_availibility[0][2] == 1:
            selected_piece = canvas.create_oval(470, 70, 530, 130, fill=color_player_one, outline=outline_selected, width=4)
            place = 3
            selected = 1
        elif nb_tour % 2 == 0 and intersection_availibility[0][2] == 2:
            selected_piece = canvas.create_oval(470, 70, 530, 130, fill=color_player_two, outline=outline_selected, width=4)
            place = 3
            selected = 1
        if selected == 1:
            if intersection_availibility[0][1] == 0:
                free.append(canvas.create_oval(290, 90, 310, 110, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][1] == 0:
                free.append(canvas.create_oval(290, 290, 310, 310, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][2] == 0:
                free.append(canvas.create_oval(490, 290, 510, 310, fill="black", outline=outline_selected, width=4))
    elif intersection_availibility[0][1] == 0 and selected == 1 and 290 < x_event < 310 and 90 < y_event < 110 and place == 3:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_3:
                canvas.coords(white_piece_1, 270, 70, 330, 130)
            if canvas.coords(white_piece_2) == coords_int_3:
                canvas.coords(white_piece_2, 270, 70, 330, 130)
            if canvas.coords(white_piece_3) == coords_int_3:
                canvas.coords(white_piece_3, 270, 70, 330, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][2] = 0
            intersection_availibility[0][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_3:
                canvas.coords(black_piece_1, 270, 70, 330, 130)
            if canvas.coords(black_piece_2) == coords_int_3:
                canvas.coords(black_piece_2, 270, 70, 330, 130)
            if canvas.coords(black_piece_3) == coords_int_3:
                canvas.coords(black_piece_3, 270, 70, 330, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][2] = 0
            intersection_availibility[0][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][1] == 0 and selected == 1 and 290 < x_event < 310 and 290 < y_event < 310 and place == 3:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_3:
                canvas.coords(white_piece_1, 270, 270, 330, 330)
            if canvas.coords(white_piece_2) == coords_int_3:
                canvas.coords(white_piece_2, 270, 270, 330, 330)
            if canvas.coords(white_piece_3) == coords_int_3:
                canvas.coords(white_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][2] = 0
            intersection_availibility[1][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_3:
                canvas.coords(black_piece_1, 270, 270, 330, 330)
            if canvas.coords(black_piece_2) == coords_int_3:
                canvas.coords(black_piece_2, 270, 270, 330, 330)
            if canvas.coords(black_piece_3) == coords_int_3:
                canvas.coords(black_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][2] = 0
            intersection_availibility[1][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][2] == 0 and selected == 1 and 490 < x_event < 510 and 290 < y_event < 310 and place == 3:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_3:
                canvas.coords(white_piece_1, 470, 270, 530, 330)
            if canvas.coords(white_piece_2) == coords_int_3:
                canvas.coords(white_piece_2, 470, 270, 530, 330)
            if canvas.coords(white_piece_3) == coords_int_3:
                canvas.coords(white_piece_3, 470, 270, 530, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][2] = 0
            intersection_availibility[1][2] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_3:
                canvas.coords(black_piece_1, 470, 270, 530, 330)
            if canvas.coords(black_piece_2) == coords_int_3:
                canvas.coords(black_piece_2, 470, 270, 530, 330)
            if canvas.coords(black_piece_3) == coords_int_3:
                canvas.coords(black_piece_3, 470, 270, 530, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[0][2] = 0
            intersection_availibility[1][2] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[0][2] != 0 and ((x_event < 470 or x_event > 530) or (y_event < 70 or y_event > 130)) and selected == 1 and place == 3:
        canvas.delete(selected_piece)
        for i in range(len(free)):
            canvas.delete(free[i])
        free = []
        selected = 0

# Intersection[1][0]
    elif intersection_availibility[1][0] != 0 and 70 < x_event < 130 and 270 < y_event < 330 and selected == 0:
        if nb_tour % 2 == 1 and intersection_availibility[1][0] == 1:
            selected_piece = canvas.create_oval(70, 270, 130, 330, fill=color_player_one, outline=outline_selected, width=4)
            place = 4
            selected = 1
        elif nb_tour % 2 == 0 and intersection_availibility[1][0] == 2:
            selected_piece = canvas.create_oval(70, 270, 130, 330, fill=color_player_two, outline=outline_selected, width=4)
            place = 4
            selected = 1
        if selected == 1:
            if intersection_availibility[0][0] == 0:
                free.append(canvas.create_oval(90, 90, 110, 110, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][1] == 0:
                free.append(canvas.create_oval(290, 290, 310, 310, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][0] == 0:
                free.append(canvas.create_oval(90, 490, 110, 510, fill="black", outline=outline_selected, width=4))
    elif intersection_availibility[0][0] == 0 and selected == 1 and 90 < x_event < 110 and 90 < y_event < 110 and place == 4:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_4:
                canvas.coords(white_piece_1, 70, 70, 130, 130)
            if canvas.coords(white_piece_2) == coords_int_4:
                canvas.coords(white_piece_2, 70, 70, 130, 130)
            if canvas.coords(white_piece_3) == coords_int_4:
                canvas.coords(white_piece_3, 70, 70, 130, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][0] = 0
            intersection_availibility[0][0] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_4:
                canvas.coords(black_piece_1, 70, 70, 130, 130)
            if canvas.coords(black_piece_2) == coords_int_4:
                canvas.coords(black_piece_2, 70, 70, 130, 130)
            if canvas.coords(black_piece_3) == coords_int_4:
                canvas.coords(black_piece_3, 70, 70, 130, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][0] = 0
            intersection_availibility[0][0] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][1] == 0 and selected == 1 and 290 < x_event < 310 and 290 < y_event < 310 and place == 4:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_4:
                canvas.coords(white_piece_1, 270, 270, 330, 330)
            if canvas.coords(white_piece_2) == coords_int_4:
                canvas.coords(white_piece_2, 270, 270, 330, 330)
            if canvas.coords(white_piece_3) == coords_int_4:
                canvas.coords(white_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][0] = 0
            intersection_availibility[1][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_4:
                canvas.coords(black_piece_1, 270, 270, 330, 330)
            if canvas.coords(black_piece_2) == coords_int_4:
                canvas.coords(black_piece_2, 270, 270, 330, 330)
            if canvas.coords(black_piece_3) == coords_int_4:
                canvas.coords(black_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][0] = 0
            intersection_availibility[1][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[2][0] == 0 and selected == 1 and 90 < x_event < 110 and 490 < y_event < 510 and place == 4:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_4:
                canvas.coords(white_piece_1, 70, 470, 130, 530)
            if canvas.coords(white_piece_2) == coords_int_4:
                canvas.coords(white_piece_2, 70, 470, 130, 530)
            if canvas.coords(white_piece_3) == coords_int_4:
                canvas.coords(white_piece_3, 70, 470, 130, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][0] = 0
            intersection_availibility[2][0] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_4:
                canvas.coords(black_piece_1, 70, 470, 130, 530)
            if canvas.coords(black_piece_2) == coords_int_4:
                canvas.coords(black_piece_2, 70, 470, 130, 530)
            if canvas.coords(black_piece_3) == coords_int_4:
                canvas.coords(black_piece_3, 70, 470, 130, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][0] = 0
            intersection_availibility[2][0] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][0] != 0 and ((x_event < 70 or x_event > 130) or (y_event < 270 or y_event > 330)) and selected == 1 and place == 4:
        canvas.delete(selected_piece)
        for i in range(len(free)):
            canvas.delete(free[i])
        free = []
        selected = 0

# Intersection[1][1]
    elif intersection_availibility[1][1] != 0 and 270 < x_event < 330 and 270 < y_event < 330 and selected == 0:
        if nb_tour % 2 == 1 and intersection_availibility[1][1] == 1:
            selected_piece = canvas.create_oval(270, 270, 330, 330, fill=color_player_one, outline=outline_selected, width=4)
            place = 5
            selected = 1
        elif nb_tour % 2 == 0 and intersection_availibility[1][1] == 2:
            selected_piece = canvas.create_oval(270, 270, 330, 330, fill=color_player_two, outline=outline_selected, width=4)
            place = 5
            selected = 1
        if selected == 1:
            if intersection_availibility[0][0] == 0:
                free.append(canvas.create_oval(90, 90, 110, 110, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[0][1] == 0:
                free.append(canvas.create_oval(290, 90, 310, 110, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[0][2] == 0:
                free.append(canvas.create_oval(490, 90, 510, 110, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][0] == 0:
                free.append(canvas.create_oval(90, 290, 110, 310, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][2] == 0:
                free.append(canvas.create_oval(490, 290, 510, 310, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][0] == 0:
                free.append(canvas.create_oval(90, 490, 110, 510, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][1] == 0:
                free.append(canvas.create_oval(290, 490, 310, 510, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][2] == 0:
                free.append(canvas.create_oval(490, 490, 510, 510, fill="black", outline=outline_selected, width=4))
    elif intersection_availibility[0][0] == 0 and selected == 1 and 90 < x_event < 110 and 90 < y_event < 110 and place == 5:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_5:
                canvas.coords(white_piece_1, 70, 70, 130, 130)
            if canvas.coords(white_piece_2) == coords_int_5:
                canvas.coords(white_piece_2, 70, 70, 130, 130)
            if canvas.coords(white_piece_3) == coords_int_5:
                canvas.coords(white_piece_3, 70, 70, 130, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[0][0] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_5:
                canvas.coords(black_piece_1, 70, 70, 130, 130)
            if canvas.coords(black_piece_2) == coords_int_5:
                canvas.coords(black_piece_2, 70, 70, 130, 130)
            if canvas.coords(black_piece_3) == coords_int_5:
                canvas.coords(black_piece_3, 70, 70, 130, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[0][0] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[0][1] == 0 and selected == 1 and 290 < x_event < 310 and 90 < y_event < 110 and place == 5:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_5:
                canvas.coords(white_piece_1, 270, 70, 330, 130)
            if canvas.coords(white_piece_2) == coords_int_5:
                canvas.coords(white_piece_2, 270, 70, 330, 130)
            if canvas.coords(white_piece_3) == coords_int_5:
                canvas.coords(white_piece_3, 270, 70, 330, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[0][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_5:
                canvas.coords(black_piece_1, 270, 70, 330, 130)
            if canvas.coords(black_piece_2) == coords_int_5:
                canvas.coords(black_piece_2, 270, 70, 330, 130)
            if canvas.coords(black_piece_3) == coords_int_5:
                canvas.coords(black_piece_3, 270, 70, 330, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[0][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[0][2] == 0 and selected == 1 and 490 < x_event < 510 and 90 < y_event < 110 and place == 5:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_5:
                canvas.coords(white_piece_1, 470, 70, 530, 130)
            if canvas.coords(white_piece_2) == coords_int_5:
                canvas.coords(white_piece_2, 470, 70, 530, 130)
            if canvas.coords(white_piece_3) == coords_int_5:
                canvas.coords(white_piece_3, 470, 70, 530, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[0][2] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_5:
                canvas.coords(black_piece_1, 470, 70, 530, 130)
            if canvas.coords(black_piece_2) == coords_int_5:
                canvas.coords(black_piece_2, 470, 70, 530, 130)
            if canvas.coords(black_piece_3) == coords_int_5:
                canvas.coords(black_piece_3, 470, 70, 530, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[0][2] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][0] == 0 and selected == 1 and 90 < x_event < 110 and 290 < y_event < 310 and place == 5:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_5:
                canvas.coords(white_piece_1, 70, 270, 130, 330)
            if canvas.coords(white_piece_2) == coords_int_5:
                canvas.coords(white_piece_2, 70, 270, 130, 330)
            if canvas.coords(white_piece_3) == coords_int_5:
                canvas.coords(white_piece_3, 70, 270, 130, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[1][0] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_5:
                canvas.coords(black_piece_1, 70, 270, 130, 330)
            if canvas.coords(black_piece_2) == coords_int_5:
                canvas.coords(black_piece_2, 70, 270, 130, 330)
            if canvas.coords(black_piece_3) == coords_int_5:
                canvas.coords(black_piece_3, 70, 270, 130, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[1][0] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][2] == 0 and selected == 1 and 490 < x_event < 510 and 290 < y_event < 310 and place == 5:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_5:
                canvas.coords(white_piece_1, 470, 270, 530, 330)
            if canvas.coords(white_piece_2) == coords_int_5:
                canvas.coords(white_piece_2, 470, 270, 530, 330)
            if canvas.coords(white_piece_3) == coords_int_5:
                canvas.coords(white_piece_3, 470, 270, 530, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[1][2] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_5:
                canvas.coords(black_piece_1, 470, 270, 530, 330)
            if canvas.coords(black_piece_2) == coords_int_5:
                canvas.coords(black_piece_2, 470, 270, 530, 330)
            if canvas.coords(black_piece_3) == coords_int_5:
                canvas.coords(black_piece_3, 470, 270, 530, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[1][2] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[2][0] == 0 and selected == 1 and 90 < x_event < 110 and 490 < y_event < 510 and place == 5:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_5:
                canvas.coords(white_piece_1, 70, 470, 130, 530)
            if canvas.coords(white_piece_2) == coords_int_5:
                canvas.coords(white_piece_2, 70, 470, 130, 530)
            if canvas.coords(white_piece_3) == coords_int_5:
                canvas.coords(white_piece_3, 70, 470, 130, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[2][0] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_5:
                canvas.coords(black_piece_1, 70, 470, 130, 530)
            if canvas.coords(black_piece_2) == coords_int_5:
                canvas.coords(black_piece_2, 70, 470, 130, 530)
            if canvas.coords(black_piece_3) == coords_int_5:
                canvas.coords(black_piece_3, 70, 470, 130, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[2][0] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[2][1] == 0 and selected == 1 and 290 < x_event < 310 and 490 < y_event < 510 and place == 5:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_5:
                canvas.coords(white_piece_1, 270, 470, 330, 530)
            if canvas.coords(white_piece_2) == coords_int_5:
                canvas.coords(white_piece_2, 270, 470, 330, 530)
            if canvas.coords(white_piece_3) == coords_int_5:
                canvas.coords(white_piece_3, 270, 470, 330, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[2][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_5:
                canvas.coords(black_piece_1, 270, 470, 330, 530)
            if canvas.coords(black_piece_2) == coords_int_5:
                canvas.coords(black_piece_2, 270, 470, 330, 530)
            if canvas.coords(black_piece_3) == coords_int_5:
                canvas.coords(black_piece_3, 270, 470, 330, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[2][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[2][2] == 0 and selected == 1 and 490 < x_event < 510 and 490 < y_event < 510 and place == 5:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_5:
                canvas.coords(white_piece_1, 470, 470, 530, 530)
            if canvas.coords(white_piece_2) == coords_int_5:
                canvas.coords(white_piece_2, 470, 470, 530, 530)
            if canvas.coords(white_piece_3) == coords_int_5:
                canvas.coords(white_piece_3, 470, 470, 530, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[2][2] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_5:
                canvas.coords(black_piece_1, 470, 470, 530, 530)
            if canvas.coords(black_piece_2) == coords_int_5:
                canvas.coords(black_piece_2, 470, 470, 530, 530)
            if canvas.coords(black_piece_3) == coords_int_5:
                canvas.coords(black_piece_3, 470, 470, 530, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][1] = 0
            intersection_availibility[2][2] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][1] != 0 and ((x_event < 270 or x_event > 330) or (y_event < 270 or y_event > 330)) and selected == 1 and place == 5:
        canvas.delete(selected_piece)
        for i in range(len(free)):
            canvas.delete(free[i])
        free = []
        selected = 0

# Intersection[1][2]
    elif intersection_availibility[1][2] != 0 and 470 < x_event < 530 and 270 < y_event < 330 and selected == 0:
        if nb_tour % 2 == 1 and intersection_availibility[1][2] == 1:
            selected_piece = canvas.create_oval(470, 270, 530, 330, fill=color_player_one, outline=outline_selected, width=4)
            place = 6
            selected = 1
        elif nb_tour % 2 == 0 and intersection_availibility[1][2] == 2:
            selected_piece = canvas.create_oval(470, 270, 530, 330, fill=color_player_two, outline=outline_selected, width=4)
            place = 6
            selected = 1
        if selected == 1:
            if intersection_availibility[0][2] == 0:
                free.append(canvas.create_oval(490, 90, 510, 110, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][1] == 0:
                free.append(canvas.create_oval(290, 290, 310, 310, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][2] == 0:
                free.append(canvas.create_oval(490, 490, 510, 510, fill="black", outline=outline_selected, width=4))
    elif intersection_availibility[0][2] == 0 and selected == 1 and 490 < x_event < 510 and 90 < y_event < 110 and place == 6:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_6:
                canvas.coords(white_piece_1, 470, 70, 530, 130)
            if canvas.coords(white_piece_2) == coords_int_6:
                canvas.coords(white_piece_2, 470, 70, 530, 130)
            if canvas.coords(white_piece_3) == coords_int_6:
                canvas.coords(white_piece_3, 470, 70, 530, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][2] = 0
            intersection_availibility[0][2] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_6:
                canvas.coords(black_piece_1, 470, 70, 530, 130)
            if canvas.coords(black_piece_2) == coords_int_6:
                canvas.coords(black_piece_2, 470, 70, 530, 130)
            if canvas.coords(black_piece_3) == coords_int_6:
                canvas.coords(black_piece_3, 470, 70, 530, 130)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][2] = 0
            intersection_availibility[0][2] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][1] == 0 and selected == 1 and 290 < x_event < 310 and 290 < y_event < 310 and place == 6:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_6:
                canvas.coords(white_piece_1, 270, 270, 330, 330)
            if canvas.coords(white_piece_2) == coords_int_6:
                canvas.coords(white_piece_2, 270, 270, 330, 330)
            if canvas.coords(white_piece_3) == coords_int_6:
                canvas.coords(white_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][2] = 0
            intersection_availibility[1][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_6:
                canvas.coords(black_piece_1, 270, 270, 330, 330)
            if canvas.coords(black_piece_2) == coords_int_6:
                canvas.coords(black_piece_2, 270, 270, 330, 330)
            if canvas.coords(black_piece_3) == coords_int_6:
                canvas.coords(black_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][2] = 0
            intersection_availibility[1][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[2][2] == 0 and selected == 1 and 490 < x_event < 510 and 490 < y_event < 510 and place == 6:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_6:
                canvas.coords(white_piece_1, 470, 470, 530, 530)
            if canvas.coords(white_piece_2) == coords_int_6:
                canvas.coords(white_piece_2, 470, 470, 530, 530)
            if canvas.coords(white_piece_3) == coords_int_6:
                canvas.coords(white_piece_3, 470, 470, 530, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][2] = 0
            intersection_availibility[2][2] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_6:
                canvas.coords(black_piece_1, 470, 470, 530, 530)
            if canvas.coords(black_piece_2) == coords_int_6:
                canvas.coords(black_piece_2, 470, 470, 530, 530)
            if canvas.coords(black_piece_3) == coords_int_6:
                canvas.coords(black_piece_3, 470, 470, 530, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[1][2] = 0
            intersection_availibility[2][2] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][2] != 0 and ((x_event < 470 or x_event > 530) or (y_event < 270 or y_event > 330)) and selected == 1 and place == 6:
        canvas.delete(selected_piece)
        for i in range(len(free)):
            canvas.delete(free[i])
        free = []
        selected = 0

# Intersection[2][0]
    elif intersection_availibility[2][0] != 0 and 70 < x_event < 130 and 470 < y_event < 530 and selected == 0:
        if nb_tour % 2 == 1 and intersection_availibility[2][0] == 1:
            selected_piece = canvas.create_oval(70, 470, 130, 530, fill=color_player_one, outline=outline_selected, width=4)
            place = 7
            selected = 1
        elif nb_tour % 2 == 0 and intersection_availibility[2][0] == 2:
            selected_piece = canvas.create_oval(70, 470, 130, 530, fill=color_player_two, outline=outline_selected, width=4)
            place = 7
            selected = 1
        if selected == 1:
            if intersection_availibility[1][0] == 0:
                free.append(canvas.create_oval(90, 290, 110, 310, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][1] == 0:
                free.append(canvas.create_oval(290, 290, 310, 310, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][1] == 0:
                free.append(canvas.create_oval(290, 490, 310, 510, fill="black", outline=outline_selected, width=4))
    elif intersection_availibility[1][0] == 0 and selected == 1 and 90 < x_event < 110 and 290 < y_event < 310 and place == 7:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_7:
                canvas.coords(white_piece_1, 70, 270, 130, 330)
            if canvas.coords(white_piece_2) == coords_int_7:
                canvas.coords(white_piece_2, 70, 270, 130, 330)
            if canvas.coords(white_piece_3) == coords_int_7:
                canvas.coords(white_piece_3, 70, 270, 130, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][0] = 0
            intersection_availibility[1][0] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_7:
                canvas.coords(black_piece_1, 70, 270, 130, 330)
            if canvas.coords(black_piece_2) == coords_int_7:
                canvas.coords(black_piece_2, 70, 270, 130, 330)
            if canvas.coords(black_piece_3) == coords_int_7:
                canvas.coords(black_piece_3, 70, 270, 130, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][0] = 0
            intersection_availibility[1][0] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][1] == 0 and selected == 1 and 290 < x_event < 310 and 290 < y_event < 310 and place == 7:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_7:
                canvas.coords(white_piece_1, 270, 270, 330, 330)
            if canvas.coords(white_piece_2) == coords_int_7:
                canvas.coords(white_piece_2, 270, 270, 330, 330)
            if canvas.coords(white_piece_3) == coords_int_7:
                canvas.coords(white_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][0] = 0
            intersection_availibility[1][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_7:
                canvas.coords(black_piece_1, 270, 270, 330, 330)
            if canvas.coords(black_piece_2) == coords_int_7:
                canvas.coords(black_piece_2, 270, 270, 330, 330)
            if canvas.coords(black_piece_3) == coords_int_7:
                canvas.coords(black_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][0] = 0
            intersection_availibility[1][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[2][1] == 0 and selected == 1 and 290 < x_event < 310 and 490 < y_event < 510 and place == 7:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_7:
                canvas.coords(white_piece_1, 270, 470, 330, 530)
            if canvas.coords(white_piece_2) == coords_int_7:
                canvas.coords(white_piece_2, 270, 470, 330, 530)
            if canvas.coords(white_piece_3) == coords_int_7:
                canvas.coords(white_piece_3, 270, 470, 330, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][0] = 0
            intersection_availibility[2][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_7:
                canvas.coords(black_piece_1, 270, 470, 330, 530)
            if canvas.coords(black_piece_2) == coords_int_7:
                canvas.coords(black_piece_2, 270, 470, 330, 530)
            if canvas.coords(black_piece_3) == coords_int_7:
                canvas.coords(black_piece_3, 270, 470, 330, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][0] = 0
            intersection_availibility[2][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[2][0] != 0 and ((x_event < 70 or x_event > 130) or (y_event < 470 or y_event > 530)) and selected == 1 and place == 7:
        canvas.delete(selected_piece)
        for i in range(len(free)):
            canvas.delete(free[i])
        free = []
        selected = 0

# Intersection[2][1]
    elif intersection_availibility[2][1] != 0 and 270 < x_event < 330 and 470 < y_event < 530 and selected == 0:
        if nb_tour % 2 == 1 and intersection_availibility[2][1] == 1:
            selected_piece = canvas.create_oval(270, 470, 330, 530, fill=color_player_one, outline=outline_selected, width=4)
            place = 8
            selected = 1
        elif nb_tour % 2 == 0 and intersection_availibility[2][1] == 2:
            selected_piece = canvas.create_oval(270, 470, 330, 530, fill=color_player_two, outline=outline_selected, width=4)
            place = 8
            selected = 1
        if selected == 1:
            if intersection_availibility[1][1] == 0:
                free.append(canvas.create_oval(290, 290, 310, 310, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][0] == 0:
                free.append(canvas.create_oval(90, 490, 110, 510, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][2] == 0:
                free.append(canvas.create_oval(490, 490, 510, 510, fill="black", outline=outline_selected, width=4))
    elif intersection_availibility[1][1] == 0 and selected == 1 and 290 < x_event < 310 and 290 < y_event < 310 and place == 8:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_8:
                canvas.coords(white_piece_1, 270, 270, 330, 330)
            if canvas.coords(white_piece_2) == coords_int_8:
                canvas.coords(white_piece_2, 270, 270, 330, 330)
            if canvas.coords(white_piece_3) == coords_int_8:
                canvas.coords(white_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][1] = 0
            intersection_availibility[1][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_8:
                canvas.coords(black_piece_1, 270, 270, 330, 330)
            if canvas.coords(black_piece_2) == coords_int_8:
                canvas.coords(black_piece_2, 270, 270, 330, 330)
            if canvas.coords(black_piece_3) == coords_int_8:
                canvas.coords(black_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][1] = 0
            intersection_availibility[1][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[2][0] == 0 and selected == 1 and 90 < x_event < 110 and 490 < y_event < 510 and place == 8:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_8:
                canvas.coords(white_piece_1, 70, 470, 130, 530)
            if canvas.coords(white_piece_2) == coords_int_8:
                canvas.coords(white_piece_2, 70, 470, 130, 530)
            if canvas.coords(white_piece_3) == coords_int_8:
                canvas.coords(white_piece_3, 70, 470, 130, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][1] = 0
            intersection_availibility[2][0] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_8:
                canvas.coords(black_piece_1, 70, 470, 130, 530)
            if canvas.coords(black_piece_2) == coords_int_8:
                canvas.coords(black_piece_2, 70, 470, 130, 530)
            if canvas.coords(black_piece_3) == coords_int_8:
                canvas.coords(black_piece_3, 70, 470, 130, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][1] = 0
            intersection_availibility[2][0] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[2][2] == 0 and selected == 1 and 490 < x_event < 510 and 490 < y_event < 510 and place == 8:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_8:
                canvas.coords(white_piece_1, 470, 470, 530, 530)
            if canvas.coords(white_piece_2) == coords_int_8:
                canvas.coords(white_piece_2, 470, 470, 530, 530)
            if canvas.coords(white_piece_3) == coords_int_8:
                canvas.coords(white_piece_3, 470, 470, 530, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][1] = 0
            intersection_availibility[2][2] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_8:
                canvas.coords(black_piece_1, 470, 470, 530, 530)
            if canvas.coords(black_piece_2) == coords_int_8:
                canvas.coords(black_piece_2, 470, 470, 530, 530)
            if canvas.coords(black_piece_3) == coords_int_8:
                canvas.coords(black_piece_3, 470, 470, 530, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][1] = 0
            intersection_availibility[2][2] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[2][1] != 0 and ((x_event < 270 or x_event > 330) or (y_event < 470 or y_event > 530)) and selected == 1 and place == 8:
        canvas.delete(selected_piece)
        for i in range(len(free)):
            canvas.delete(free[i])
        free = []
        selected = 0

# Intersection[2][2]
    elif intersection_availibility[2][2] != 0 and 470 < x_event < 530 and 470 < y_event < 530 and selected == 0:
        if nb_tour % 2 == 1 and intersection_availibility[2][2] == 1:
            selected_piece = canvas.create_oval(470, 470, 530, 530, fill=color_player_one, outline=outline_selected, width=4)
            place = 9
            selected = 1
        elif nb_tour % 2 == 0 and intersection_availibility[2][2] == 2:
            selected_piece = canvas.create_oval(470, 470, 530, 530, fill=color_player_two, outline=outline_selected, width=4)
            place = 9
            selected = 1
        if selected == 1:
            if intersection_availibility[1][1] == 0:
                free.append(canvas.create_oval(290, 290, 310, 310, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][2] == 0:
                free.append(canvas.create_oval(490, 290, 510, 310, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][1] == 0:
                free.append(canvas.create_oval(290, 490, 310, 510, fill="black", outline=outline_selected, width=4))
    elif intersection_availibility[1][1] == 0 and selected == 1 and 290 < x_event < 310 and 290 < y_event < 310 and place == 9:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_9:
                canvas.coords(white_piece_1, 270, 270, 330, 330)
            if canvas.coords(white_piece_2) == coords_int_9:
                canvas.coords(white_piece_2, 270, 270, 330, 330)
            if canvas.coords(white_piece_3) == coords_int_9:
                canvas.coords(white_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][2] = 0
            intersection_availibility[1][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_9:
                canvas.coords(black_piece_1, 270, 270, 330, 330)
            if canvas.coords(black_piece_2) == coords_int_9:
                canvas.coords(black_piece_2, 270, 270, 330, 330)
            if canvas.coords(black_piece_3) == coords_int_9:
                canvas.coords(black_piece_3, 270, 270, 330, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][2] = 0
            intersection_availibility[1][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[1][2] == 0 and selected == 1 and 490 < x_event < 510 and 290 < y_event < 310 and place == 9:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_9:
                canvas.coords(white_piece_1, 470, 270, 530, 330)
            if canvas.coords(white_piece_2) == coords_int_9:
                canvas.coords(white_piece_2, 470, 270, 530, 330)
            if canvas.coords(white_piece_3) == coords_int_9:
                canvas.coords(white_piece_3, 470, 270, 530, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][2] = 0
            intersection_availibility[1][2] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_9:
                canvas.coords(black_piece_1, 470, 270, 530, 330)
            if canvas.coords(black_piece_2) == coords_int_9:
                canvas.coords(black_piece_2, 470, 270, 530, 330)
            if canvas.coords(black_piece_3) == coords_int_9:
                canvas.coords(black_piece_3, 470, 270, 530, 330)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][2] = 0
            intersection_availibility[1][2] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[2][1] == 0 and selected == 1 and 290 < x_event < 310 and 490 < y_event < 510 and place == 9:
        canvas.delete(selected_piece)
        if nb_tour % 2 == 1:
            if canvas.coords(white_piece_1) == coords_int_9:
                canvas.coords(white_piece_1, 270, 470, 330, 530)
            if canvas.coords(white_piece_2) == coords_int_9:
                canvas.coords(white_piece_2, 270, 470, 330, 530)
            if canvas.coords(white_piece_3) == coords_int_9:
                canvas.coords(white_piece_3, 270, 470, 330, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][2] = 0
            intersection_availibility[2][1] = 1
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
        elif nb_tour % 2 == 0:
            if canvas.coords(black_piece_1) == coords_int_9:
                canvas.coords(black_piece_1, 270, 470, 330, 530)
            if canvas.coords(black_piece_2) == coords_int_9:
                canvas.coords(black_piece_2, 270, 470, 330, 530)
            if canvas.coords(black_piece_3) == coords_int_9:
                canvas.coords(black_piece_3, 270, 470, 330, 530)
            for i in range(len(free)):
                canvas.delete(free[i])
            free = []
            intersection_availibility[2][2] = 0
            intersection_availibility[2][1] = 2
            selected = 0
            nb_tour += 1
            egalite.append(intersection_availibility)
            draw()
            win()
    elif intersection_availibility[2][2] != 0 and ((x_event < 470 or x_event > 530) or (y_event < 470 or y_event > 530)) and selected == 1 and place == 9:
        canvas.delete(selected_piece)
        for i in range(len(free)):
            canvas.delete(free[i])
        free = []
        selected = 0
 

def win():
    global score, sj1, sj2, intersection_availibility, winner, game, nb_tour, joueur_1, joueur_2, j1, j2

    if (intersection_availibility[0][0] == 1 and intersection_availibility[0][1] == 1 and intersection_availibility[0][2] == 1) or (intersection_availibility[1][0] == 1 and intersection_availibility[1][1] == 1 and intersection_availibility[1][2] == 1) or (intersection_availibility[2][0] == 1 and intersection_availibility[2][1] == 1 and intersection_availibility[2][2] == 1) or (intersection_availibility[0][0] == 1 and intersection_availibility[1][0] == 1 and intersection_availibility[2][0] == 1) or (intersection_availibility[0][1] == 1 and intersection_availibility[1][1] == 1 and intersection_availibility[2][1] == 1) or (intersection_availibility[0][2] == 1 and intersection_availibility[1][2] == 1 and intersection_availibility[2][2] == 1) or (intersection_availibility[0][0] == 1 and intersection_availibility[1][1] == 1 and intersection_availibility[2][2] == 1) or (intersection_availibility[0][2] == 1 and intersection_availibility[1][1] == 1 and intersection_availibility[2][0] == 1):
        if joueur_1 == "white pieces":
            canvas.delete(j1, j2)
            sj1 += 1
            score = tk.Label(root, text="  J1  " + str(sj1) + "  -  " + str(sj2) + "  J2  ", font=("calibri", 30), fg="white", bg="black", padx=185)
            score.grid(row=2, columnspan = 3)
            winner = canvas.create_text(300, 575, text="Joueur 1 a gagné la partie. Cliquez pour continuer", fill="black", font=('Times', 18, "bold"))
            game += 1
            canvas.bind('<Button-1>', next_game)
            nb_tour = 1
        elif joueur_2 == "white pieces":
            canvas.delete(j1, j2)
            sj2 += 1
            score = tk.Label(root, text="  J1  " + str(sj1) + "  -  " + str(sj2) + "  J2  ", font=("calibri", 30), fg="white", bg="black", padx=185)
            score.grid(row=2, columnspan = 3)
            winner = canvas.create_text(300, 575, text="Joueur 2 a gagné la partie. Cliquez pour continuer", fill="black", font=('Times', 18, "bold"))
            game += 1
            canvas.bind('<Button-1>', next_game)
            nb_tour = 1
    if (intersection_availibility[0][0] == 2 and intersection_availibility[0][1] == 2 and intersection_availibility[0][2] == 2) or (intersection_availibility[1][0] == 2 and intersection_availibility[1][1] == 2 and intersection_availibility[1][2] == 2) or (intersection_availibility[2][0] == 2 and intersection_availibility[2][1] == 2 and intersection_availibility[2][2] == 2) or (intersection_availibility[0][0] == 2 and intersection_availibility[1][0] == 2 and intersection_availibility[2][0] == 2) or (intersection_availibility[0][1] == 2 and intersection_availibility[1][1] == 2 and intersection_availibility[2][1] == 2) or (intersection_availibility[0][2] == 2 and intersection_availibility[1][2] == 2 and intersection_availibility[2][2] == 2) or (intersection_availibility[0][0] == 2 and intersection_availibility[1][1] == 2 and intersection_availibility[2][2] == 2) or (intersection_availibility[0][2] == 2 and intersection_availibility[1][1] == 2 and intersection_availibility[2][0] == 2):
        if joueur_1 == "black pieces":
            canvas.delete(j1, j2)
            sj1 += 1
            score = tk.Label(root, text="  J1  " + str(sj1) + "  -  " + str(sj2) + "  J2  ", font=("calibri", 30), fg="white", bg="black", padx=185)
            score.grid(row=2, columnspan = 3)
            winner = canvas.create_text(300, 575, text="Joueur 1 a gagné la partie. Cliquez pour continuer", fill="black", font=('Times', 18, "bold"))
            game += 1
            canvas.bind('<Button-1>', next_game)
            nb_tour = 1
        elif joueur_2 == "black pieces":
            canvas.delete(j1, j2)
            sj2 += 1
            score = tk.Label(root, text="  J1  " + str(sj1) + "  -  " + str(sj2) + "  J2  ", font=("calibri", 30), fg="white", bg="black", padx=185)
            score.grid(row=2, columnspan = 3)
            winner = canvas.create_text(300, 575, text="Joueur 2 a gagné la partie. Cliquez pour continuer", fill="black", font=('Times', 18, "bold"))
            game += 1
            canvas.bind('<Button-1>', next_game)
            nb_tour = 1
    
    if sj1 == 3:
        canvas.delete(winner)
        winner = canvas.create_text(300, 575, text="Vainqueur: Joueur 1! Cliquez pour quitter le jeu.", fill="black", font=('Times', 18, "bold"))
        canvas.bind('<Button-1>', end)
    elif sj2 == 3:
        canvas.delete(winner)
        winner = canvas.create_text(300, 575, text="Vainqueur: Joueur 2! Cliquez pour quitter le jeu.", fill="black", font=('Times', 18, "bold"))
        canvas.bind('<Button-1>', end)

def draw():
    global intersection_availibility, egalite
    pass

def next_game(event):
    global white_piece_1, white_piece_2, white_piece_3, black_piece_1, black_piece_2, black_piece_3, white_pieces, black_pieces, joueur_1, joueur_2, intersection_availibility, nb_tour, selected, free, winner, sj1, sj2, j1, j2
    
    if 0 < event.x < 600 and 0 < event.y < 600:
        canvas.delete(white_piece_1, white_piece_2, white_piece_3, black_piece_1, black_piece_2, black_piece_3, winner, j1, j2)
        # White pieces
        white_piece_1 = canvas.create_oval(600/3-30, 530, 600/3+30, 590, fill=color_player_one, outline=color_player_one, width=4)
        white_piece_2 = canvas.create_oval(600/2-30, 530, 600/2+30, 590, fill=color_player_one, outline=color_player_one, width=4)
        white_piece_3 = canvas.create_oval(2*600/3-30, 530, 2*600/3+30, 590, fill=color_player_one, outline=color_player_one, width=4)
        white_pieces = [white_piece_1, white_piece_2, white_piece_3]

        # Black pieces
        black_piece_1 = canvas.create_oval(600/3-30, 10, 600/3+30, 70, fill=color_player_two, outline=color_player_two, width=4)
        black_piece_2 = canvas.create_oval(600/2-30, 10, 600/2+30, 70, fill=color_player_two, outline=color_player_two, width=4)
        black_piece_3 = canvas.create_oval(2*600/3-30, 10, 2*600/3+30, 70, fill=color_player_two, outline=color_player_two, width=4)
        black_pieces = [black_piece_1, black_piece_2, black_piece_3]
        for i in range(3):
            intersection_availibility = [[0 for i in range(3)] for j in range(3)]
        canvas.bind('<Button-1>', first_moves)
        nb_tour = 1
        selected = 0
        free = []
        if game % 2 == 1:
            joueur_1 = "white pieces"
            joueur_2 = "black pieces"
            j1 = canvas.create_text(540, 580, text="Joueur 1", fill="black", font=('Times', 20, "bold"))
            j2 = canvas.create_text(540, 20, text="Joueur 2", fill="black", font=('Times', 20, "bold"))
        elif game % 2 == 0:
            joueur_1 = "black pieces"
            joueur_2 = "white pieces"
            j1 = canvas.create_text(540, 20, text="Joueur 1", fill="black", font=('Times', 20, "bold"))
            j2 = canvas.create_text(540, 580, text="Joueur 2", fill="black", font=('Times', 20, "bold"))

def end(event):
    if 0 < event.x < 600 and 0 < event.y < 600:
        canvas.quit()

def restart():
    global white_piece_1, white_piece_2, white_piece_3, black_piece_1, black_piece_2, black_piece_3, white_pieces, black_pieces, intersection_availibility, nb_tour, selected, free, sj1, sj2, score, winner, joueur_1, joueur_2, game, j1, j2, egalite
    canvas.delete(white_piece_1, white_piece_2, white_piece_3, black_piece_1, black_piece_2, black_piece_3, winner)
    # White pieces
    white_piece_1 = canvas.create_oval(600/3-30, 530, 600/3+30, 590, fill=color_player_one, outline=color_player_one, width=4)
    white_piece_2 = canvas.create_oval(600/2-30, 530, 600/2+30, 590, fill=color_player_one, outline=color_player_one, width=4)
    white_piece_3 = canvas.create_oval(2*600/3-30, 530, 2*600/3+30, 590, fill=color_player_one, outline=color_player_one, width=4)
    white_pieces = [white_piece_1, white_piece_2, white_piece_3]

    # Black pieces
    black_piece_1 = canvas.create_oval(600/3-30, 10, 600/3+30, 70, fill=color_player_two, outline=color_player_two, width=4)
    black_piece_2 = canvas.create_oval(600/2-30, 10, 600/2+30, 70, fill=color_player_two, outline=color_player_two, width=4)
    black_piece_3 = canvas.create_oval(2*600/3-30, 10, 2*600/3+30, 70, fill=color_player_two, outline=color_player_two, width=4)
    black_pieces = [black_piece_1, black_piece_2, black_piece_3]
    for i in range(3):
        intersection_availibility = [[0 for i in range(3)] for j in range(3)]
    canvas.bind('<Button-1>', first_moves)
    nb_tour = 1
    selected = 0
    free = []
    sj1 = 0
    sj2 = 0
    score = tk.Label(root, text="  J1  " + str(sj1) + "  -  " + str(sj2) + "  J2  ", font=("calibri", 30), fg="white", bg="black", padx=185)
    score.grid(row=2, columnspan = 3)
    game = 1
    joueur_1 = "white pieces"
    joueur_2 = "black pieces"
    j1 = canvas.create_text(540, 580, text="Joueur 1", fill="black", font=('Times', 20, "bold"))
    j2 = canvas.create_text(540, 20, text="Joueur 2", fill="black", font=('Times', 20, "bold"))
    egalite = []

def save(event):
    pass

def charge(event):
    pass

# Canvas

canvas = tk.Canvas(root, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, bg="moccasin")

boardgame = canvas.create_rectangle(100, 100, 500, 500, fill="moccasin", width=4, outline="black")

# Creating the lines for the board
vertical_line = canvas.create_line(600/2, 100, 600/2, 500, fill="black", width=4)
horizontal_line = canvas.create_line(100, 600/2, 500, 600/2, fill="black", width=4)
diag_line_1 = canvas.create_line(500, 100, 100, 500, fill="black", width=4)
diag_line_2 = canvas.create_line(100, 100, 500, 500, fill="black", width=4)

# Creating the intersections of the board
for i in intersection_coords:
    for j in intersection_coords:
        canvas.create_oval(j-10, i-10, j+10, i+10, fill="black", width=4)


j1 = canvas.create_text(540, 580, text="Joueur 1", fill="black", font=('Times', 20, "bold"))
j2 = canvas.create_text(540, 20, text="Joueur 2", fill="black", font=('Times', 20, "bold"))

# White pieces
white_piece_1 = canvas.create_oval(600/3-30, 530, 600/3+30, 590, fill=color_player_one, outline=color_player_one, width=4)
white_piece_2 = canvas.create_oval(600/2-30, 530, 600/2+30, 590, fill=color_player_one, outline=color_player_one, width=4)
white_piece_3 = canvas.create_oval(2*600/3-30, 530, 2*600/3+30, 590, fill=color_player_one, outline=color_player_one, width=4)
white_pieces = [white_piece_1, white_piece_2, white_piece_3]


# Black pieces
black_piece_1 = canvas.create_oval(600/3-30, 10, 600/3+30, 70, fill=color_player_two, outline=color_player_two, width=4)
black_piece_2 = canvas.create_oval(600/2-30, 10, 600/2+30, 70, fill=color_player_two, outline=color_player_two, width=4)
black_piece_3 = canvas.create_oval(2*600/3-30, 10, 2*600/3+30, 70, fill=color_player_two, outline=color_player_two, width=4)
black_pieces = [black_piece_1, black_piece_2, black_piece_3]


canvas.bind('<Button-1>', first_moves)


# Position

canvas.grid(rowspan=2, columnspan=3)


score = tk.Label(root, text="  J1  " + str(sj1) + "  -  " + str(sj2) + "  J2  ", font=("calibri", 30), fg="white", bg="black", padx=185)
score.grid(row=2, columnspan = 3)


redemarer = tk.Button(root, text= "Redémarrer", padx=10, pady= 10, fg="white", bg="black", command=restart)
redemarer.grid(column=3, row=0)

reprendre = tk.Button(root, text= "Reprendre", padx=10, pady= 10, fg="white", bg="black", command=charge)
reprendre.grid(column=3, row=1)

sauvegarder = tk.Button(root, text= "Sauvegarder", padx=10, pady= 10, bg="green", command=save)
sauvegarder.grid(column=3, row=2)

root.mainloop()
