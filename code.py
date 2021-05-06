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
turn = "white"
nb_tour = 1

# For selection and showing possible moves
selected = 0
free = []

# List to see which intersections are available. Possible values: 0 for available, 1 for white and 2 for black
for i in range(3):
    intersection_availibility = [[0 for i in range(3)] for j in range(3)]

# For the score
sj1=0
sj2=0


# Functions

def restart(event):
    pass


def white_move(event):
    global turn, nb_tour, moving_piece, intersection_availibility, intersection_coords
    x = event.x
    y = event.y

    # To move the three white pieces to the board
    if nb_tour == 1:
        moving_piece = white_piece_1
    elif nb_tour == 3:
        moving_piece = white_piece_2
    elif nb_tour == 5:
        moving_piece = white_piece_3

    for i in intersection_coords:
        for j in intersection_coords:
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 100 and j == 100 and intersection_availibility[0][0] == 0:
                intersection_availibility[0][0] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 100 and j == 300 and intersection_availibility[0][1] == 0:
                intersection_availibility[0][1] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 100 and j == 500 and intersection_availibility[0][2] == 0:
                intersection_availibility[0][2] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1

            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 300 and j == 100 and intersection_availibility[1][0] == 0:
                intersection_availibility[1][0] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 300 and j == 300 and intersection_availibility[1][1] == 0:
                intersection_availibility[1][1] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 300 and j == 500 and intersection_availibility[1][2] == 0:
                intersection_availibility[1][2] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1

            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 500 and j == 100 and intersection_availibility[2][0] == 0:
                intersection_availibility[2][0] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 500 and j == 300 and intersection_availibility[2][1] == 0:
                intersection_availibility[2][1] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 500 and j == 500 and intersection_availibility[2][2] == 0:
                intersection_availibility[2][2] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
    
        
def black_move(event):
    global turn, nb_tour, moving_piece, intersection_availibility, intersection_coords
    x = event.x
    y = event.y

    # To move the three black pieces to the board
    if nb_tour == 2:
        moving_piece = black_piece_1
    elif nb_tour == 4:
        moving_piece = black_piece_2
    elif nb_tour == 6:
        moving_piece = black_piece_3
    
    
    for i in intersection_coords:
        for j in intersection_coords:
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 100 and j == 100 and intersection_availibility[0][0] == 0:
                intersection_availibility[0][0] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 100 and j == 300 and intersection_availibility[0][1] == 0:
                intersection_availibility[0][1] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 100 and j == 500 and intersection_availibility[0][2] == 0:
                intersection_availibility[0][2] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1

            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 300 and j == 100 and intersection_availibility[1][0] == 0:
                intersection_availibility[1][0] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 300 and j == 300 and intersection_availibility[1][1] == 0:
                intersection_availibility[1][1] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 300 and j == 500 and intersection_availibility[1][2] == 0:
                intersection_availibility[1][2] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1

            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 500 and j == 100 and intersection_availibility[2][0] == 0:
                intersection_availibility[2][0] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 500 and j == 300 and intersection_availibility[2][1] == 0:
                intersection_availibility[2][1] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
            if (j-10 < x < j+10 and i-10 < y < i+10) and i == 500 and j == 500 and intersection_availibility[2][2] == 0:
                intersection_availibility[2][2] = 1
                canvas.coords(moving_piece, j-30, i-30, j+30, i+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1


    if nb_tour == 7:
        canvas.bind('<Button-1>', selection)


def selection(event): 
    global moving_piece, white_piece_1, white_piece_2, white_piece_3, outline_selected, outline_white, outline_black, selected, intersection_availibility, free, nb_tour

    x_event, y_event = event.x, event.y

    # To change the coords of the moving piece
    x1_moving_piece, y1_moving_piece, x2_moving_piece, y2_moving_piece = canvas.coords(moving_piece)

    # To change the coords of the white pieces moving to another intersection
    x1_white1, y1_white1, x2_white1, y2_white1 = canvas.coords(white_piece_1)
    x1_white2, y1_white2, x2_white2, y2_white2 = canvas.coords(white_piece_2)
    x1_white3, y1_white3, x2_white3, y2_white3 = canvas.coords(white_piece_3)

    # To change the moving piece when selected and its' coords when moved
    if nb_tour % 2 == 1 and selected == 0:
        if x1_white1 < x_event < x2_white1 and y1_white1 < y_event < y2_white1:
            moving_piece = white_piece_1
            x1_moving_piece, y1_moving_piece, x2_moving_piece, y2_moving_piece = canvas.coords(white_piece_1)
            white_piece_1 = canvas.create_oval(canvas.coords(moving_piece), fill=color_player_one, outline=outline_selected, width=4)
        if x1_white2 < x_event < x2_white2 and y1_white2 < y_event < y2_white2:
            moving_piece = white_piece_2
            x1_moving_piece, y1_moving_piece, x2_moving_piece, y2_moving_piece = canvas.coords(white_piece_2)
            white_piece_2 = canvas.create_oval(canvas.coords(moving_piece), fill=color_player_one, outline=outline_selected, width=4)
        if x1_white3 < x_event < x2_white3 and y1_white3 < y_event < y2_white3:
            moving_piece = white_piece_3
            x1_moving_piece, y1_moving_piece, x2_moving_piece, y2_moving_piece = canvas.coords(white_piece_3)
            white_piece_3 = canvas.create_oval(canvas.coords(moving_piece), fill=color_player_one, outline=outline_selected, width=4)

    # To show the available intersections --> possible moves
    if x1_moving_piece < x_event < x2_moving_piece and y1_moving_piece < y_event < y2_moving_piece and selected == 0:
        selected = 1
        if y1_moving_piece + 30 == 100:
            if intersection_availibility[0][0] == 0 and x1_moving_piece - 170 == 100:
                free.append(canvas.create_oval(100-10, 100-10, 100+10, 100+10, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[0][1] == 0 and (x1_moving_piece + 230 == 300 or x1_moving_piece - 170 == 300):
                free.append(canvas.create_oval(300-10, 100-10, 300+10, 100+10, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[0][2] == 0 and x1_moving_piece + 230 == 500:
                free.append(canvas.create_oval(500-10, 100-10, 500+10, 100+10, fill="black", outline=outline_selected, width=4))

        if y1_moving_piece + 30 == 300:
            if intersection_availibility[1][0] == 0 and x1_moving_piece - 170 == 100:
                free.append(canvas.create_oval(100-10, 300-10, 100+10, 300+10, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][1] == 0 and (x1_moving_piece + 230 == 300 or x1_moving_piece - 170 == 300):
                free.append(canvas.create_oval(300-10, 300-10, 300+10, 300+10, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][2] == 0 and x1_moving_piece + 230 == 500:
                free.append(canvas.create_oval(500-10, 300-10, 500+10, 300+10, fill="black", outline=outline_selected, width=4))

        if y1_moving_piece + 30 == 500:
            if intersection_availibility[2][0] == 0 and x1_moving_piece - 170 == 100:
                free.append(canvas.create_oval(100-10, 500-10, 100+10, 500+10, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][1] == 0 and (x1_moving_piece+ 230 == 300 or x1_moving_piece - 170 == 300):
                free.append(canvas.create_oval(300-10, 500-10, 300+10, 500+10, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][2] == 0 and x1_moving_piece + 230 == 500:
                free.append(canvas.create_oval(500-10, 500-10, 500+10, 500+10, fill="black", outline=outline_selected, width=4))
        
        if x1_moving_piece + 30 == 100:
            if intersection_availibility[0][0] == 0 and y1_moving_piece - 170 == 100:
                free.append(canvas.create_oval(100-10, 100-10, 100+10, 100+10, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][0] == 0 and (y1_moving_piece + 230 == 300 or y1_moving_piece - 170 == 300):
                free.append(canvas.create_oval(100-10, 300-10, 100+10, 300+10, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][0] == 0 and y1_moving_piece + 230 == 500:
                free.append(canvas.create_oval(100-10, 500-10, 100+10, 500+10, fill="black", outline=outline_selected, width=4))
        
        if x1_moving_piece + 30 == 300:
            if intersection_availibility[0][1] == 0 and y1_moving_piece - 170 == 100:
                free.append(canvas.create_oval(300-10, 100-10, 300+10, 100+10, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][1] == 0 and (y1_moving_piece + 230 == 300 or y1_moving_piece - 170 == 300):
                free.append(canvas.create_oval(300-10, 300-10, 300+10, 300+10, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][1] == 0 and y1_moving_piece + 230 == 500:
                free.append(canvas.create_oval(300-10, 500-10, 300+10, 500+10, fill="black", outline=outline_selected, width=4))
        
        if x1_moving_piece + 30 == 500:
            if intersection_availibility[0][2] == 0 and y1_moving_piece - 170 == 100:
                free.append(canvas.create_oval(500-10, 100-10, 500+10, 100+10, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[1][2] == 0 and (y1_moving_piece + 230 == 300 or y1_moving_piece - 170 == 300):
                free.append(canvas.create_oval(500-10, 300-10, 500+10, 300+10, fill="black", outline=outline_selected, width=4))
            if intersection_availibility[2][2] == 0 and y1_moving_piece + 230 == 500:
                free.append(canvas.create_oval(500-10, 500-10, 500+10, 500+10, fill="black", outline=outline_selected, width=4))
        
        if intersection_availibility[0][0] == 0 and x1_moving_piece - 170 == 100 and y1_moving_piece - 170 == 100:
            free.append(canvas.create_oval(100-10, 100-10, 100+10, 100+10, fill="black", outline=outline_selected, width=4))

        if intersection_availibility[0][2] == 0 and x1_moving_piece + 230 == 500 and y1_moving_piece - 170 == 100:
            free.append(canvas.create_oval(500-10, 100-10, 500+10, 100+10, fill="black", outline=outline_selected, width=4))

        if intersection_availibility[2][0] == 0 and x1_moving_piece - 170 == 100 and y1_moving_piece + 230 == 500:
            free.append(canvas.create_oval(100-10, 500-10, 100+10, 500+10, fill="black", outline=outline_selected, width=4))
        
        if intersection_availibility[2][2] == 0 and x1_moving_piece + 230 == 500 and y1_moving_piece + 230 == 500:
            free.append(canvas.create_oval(500-10, 500-10, 500+10, 500+10, fill="black", outline=outline_selected, width=4))

        if intersection_availibility[1][1] == 0 and ((x1_moving_piece + 230 == 300 and y1_moving_piece + 230 == 300) or (x1_moving_piece - 170 == 300 and y1_moving_piece + 230 == 300) or (x1_moving_piece + 230 == 300 and y1_moving_piece - 170 == 300) or (x1_moving_piece - 170 == 300 and y1_moving_piece - 170 == 300)):
            free.append(canvas.create_oval(300-10, 300-10, 300+10, 300+10, fill="black", outline=outline_selected, width=4))
            
    else:
        moving_piece = canvas.create_oval(canvas.coords(moving_piece), fill=color_player_one, outline=outline_white, width=4)
        for i in range(len(free)):
            canvas.delete(free[i])
        free = []
        selected = 0
   
   


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


# White pieces
white_piece_1 = canvas.create_oval(600/3-30, 530, 600/3+30, 590, fill=color_player_one, outline=color_player_one, width=4)
white_piece_2 = canvas.create_oval(600/2-30, 530, 600/2+30, 590, fill=color_player_one, outline=color_player_one, width=4)
white_piece_3 = canvas.create_oval(2*600/3-30, 530, 2*600/3+30, 590, fill=color_player_one, outline=color_player_one, width=4)

# Black pieces
black_piece_1 = canvas.create_oval(600/3-30, 10, 600/3+30, 70, fill=color_player_two, outline=color_player_two, width=4)
black_piece_2 = canvas.create_oval(600/2-30, 10, 600/2+30, 70, fill=color_player_two, outline=color_player_two, width=4)
black_piece_3 = canvas.create_oval(2*600/3-30, 10, 2*600/3+30, 70, fill=color_player_two, outline=color_player_two, width=4)


moving_piece = white_piece_1
canvas.bind('<Button-1>', white_move)


# Position

canvas.grid(rowspan=2, columnspan=3)


score = tk.Label(root, text="  J1  " + str(sj1) + "  -  " + str(sj2)+ "  J2  ", font=("calibri", 30), fg="white", bg="black", padx=185)
score.grid(row=2, columnspan = 3)


redemarer = tk.Button(root, text= "redemarer", padx=10, pady= 10, fg="white", bg="black", command=restart)
redemarer.grid(column=0, row=3)

reprendre = tk.Button(root, text= "reprendre", padx=10, pady= 10, fg="white", bg="black", command=restart)
reprendre.grid(column=1, row=3)

sauvgarder = tk.Button(root, text= "sauvgarder", padx=10, pady= 10, bg="green", command=restart)
sauvgarder.grid(column=2, row=3)

h_vs_h = tk.Button(root, text= " J1 vs J2 ", padx=10, pady= 10, fg="white", bg="black", command=restart)
h_vs_h.grid(column=3, row=0)

h_vs_IA = tk.Button(root, text= " J1 vs IA ", padx=10, pady= 10, fg="white", bg="black", command=restart)
h_vs_IA.grid(column=3, row=1)

IA_vs_IA = tk.Button(root, text= " IA vs IA ", padx=10, pady= 10, fg="white", bg="black", command=restart)
IA_vs_IA.grid(column=3, row=2)






root.mainloop()