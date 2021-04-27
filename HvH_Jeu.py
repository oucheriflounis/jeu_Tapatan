import tkinter as tk

root = tk.Tk()

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600

color_player_one = "white"
color_player_two = "black"

outline_selected = "yellow"
outline_white = "white"
outline_black = "black"

turn = "white"
nb_tour = 1

selection_clic = 0
selected = 0


top_left = 0
top_mid = 0
top_right = 0

mid_left = 0
mid = 0
mid_right = 0

lower_left = 0
lower_mid = 0
lower_right = 0

# Functions

def white_move(event):
    global turn, nb_tour, moving_piece, top_left, top_mid, top_right, mid_left, mid, mid_right, lower_left, lower_mid, lower_right
    x = event.x
    y = event.y

    if nb_tour == 1:
        moving_piece = white_piece_1
    elif nb_tour == 3:
        moving_piece = white_piece_2
    elif nb_tour == 5:
        moving_piece = white_piece_3
    
    if turn == "white":
        if top_left == 0:
            if 100-10 < x < 100+10 and 100-10 < y < 100+10:
                canvas.coords(moving_piece, 100-30, 100-30, 100+30, 100+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
                top_left += 1
        if top_mid == 0:
            if 600/2-10 < x < 600/2+10 and 100-10 < y < 100+10:
                canvas.coords(moving_piece, 600/2-30, 100-30, 600/2+30, 100+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
                top_mid += 1
        if top_right == 0:
            if 500-10 < x < 500+10 and 100-10 < y < 100+10:
                canvas.coords(moving_piece, 500-30, 100-30, 500+30, 100+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
                top_right += 1

        if mid_left == 0:
            if 100-10 < x < 100+10 and 600/2-10 < y < 600/2+10:
                canvas.coords(moving_piece, 100-30, 600/2-30, 100+30, 600/2+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
                mid_left += 1
        if mid == 0:
            if 600/2-10 < x < 600/2+10 and 600/2-10 < y < 600/2+10:
                canvas.coords(moving_piece, 600/2-30, 600/2-30, 600/2+30, 600/2+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
                mid += 1
        if mid_right == 0:
            if 500-10 < x < 500+10 and 600/2-10 < y < 600/2+10:
                canvas.coords(moving_piece, 500-30, 600/2-30, 500+30, 600/2+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
                mid_right += 1

        if lower_left == 0:
            if 100-10 < x < 100+10 and 500-10 < y < 500+10:
                canvas.coords(moving_piece, 100-30, 500-30, 100+30, 500+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
                lower_left += 1
        if lower_mid == 0:
            if 600/2-10 < x < 600/2+10 and 500-10 < y < 500+10:
                canvas.coords(moving_piece, 600/2-30, 500-30, 600/2+30, 500+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
                lower_mid += 1
        if lower_right == 0:
            if 500-10 < x < 500+10 and 500-10 < y < 500+10:
                canvas.coords(moving_piece, 500-30, 500-30, 500+30, 500+30)
                turn = "black"
                canvas.bind('<Button-1>', black_move)
                nb_tour += 1
                lower_right += 1
        
        


def black_move(event):
    global turn, nb_tour, moving_piece, top_left, top_mid, top_right, mid_left, mid, mid_right, lower_left, lower_mid, lower_right
    x = event.x
    y = event.y

    if nb_tour == 2:
        moving_piece = black_piece_1
    elif nb_tour == 4:
        moving_piece = black_piece_2
    elif nb_tour == 6:
        moving_piece = black_piece_3
    
    if turn == "black":
        if top_left == 0:
            if 100-10 < x < 100+10 and 100-10 < y < 100+10:
                canvas.coords(moving_piece, 100-30, 100-30, 100+30, 100+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
                top_left += 1
        if top_mid == 0:
            if 600/2-10 < x < 600/2+10 and 100-10 < y < 100+10:
                canvas.coords(moving_piece, 600/2-30, 100-30, 600/2+30, 100+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
                top_mid += 1
        if top_right == 0:
            if 500-10 < x < 500+10 and 100-10 < y < 100+10:
                canvas.coords(moving_piece, 500-30, 100-30, 500+30, 100+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
                top_right += 1

        if mid_left == 0:
            if 100-10 < x < 100+10 and 600/2-10 < y < 600/2+10:
                canvas.coords(moving_piece, 100-30, 600/2-30, 100+30, 600/2+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
                mid_left += 1
        if mid == 0:
            if 600/2-10 < x < 600/2+10 and 600/2-10 < y < 600/2+10:
                canvas.coords(moving_piece, 600/2-30, 600/2-30, 600/2+30, 600/2+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
                mid += 1
        if mid_right == 0:
            if 500-10 < x < 500+10 and 600/2-10 < y < 600/2+10:
                canvas.coords(moving_piece, 500-30, 600/2-30, 500+30, 600/2+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
                mid_right += 1

        if lower_left == 0:
            if 100-10 < x < 100+10 and 500-10 < y < 500+10:
                canvas.coords(moving_piece, 100-30, 500-30, 100+30, 500+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
                lower_left += 1
        if lower_mid == 0:
            if 600/2-10 < x < 600/2+10 and 500-10 < y < 500+10:
                canvas.coords(moving_piece, 600/2-30, 500-30, 600/2+30, 500+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
                lower_mid += 1
        if lower_right == 0:
            if 500-10 < x < 500+10 and 500-10 < y < 500+10:
                canvas.coords(moving_piece, 500-30, 500-30, 500+30, 500+30)
                turn = "white"
                canvas.bind('<Button-1>', white_move)
                nb_tour += 1
                lower_right += 1

    if nb_tour == 7:
        canvas.bind('<Button-1>', selection)

def selection(event):
    global white_piece_1, white_piece_2, outline_black, outline_selected, outline_white, selection_clic, selected

    x_event, y_event = event.x, event.y

    x1_white1, y1_white1, x2_white1, y2_white1 = canvas.coords(white_piece_1)
    x1_white2, y1_white2, x2_white2, y2_white2 = canvas.coords(white_piece_2)

    if x1_white1 < x_event < x2_white1 and y1_white1 < y_event < y2_white1 and selection_clic == 0 and selected == 0:
        white_piece_1 = canvas.create_oval(x1_white1, y1_white1, x2_white1, y2_white1, fill=color_player_one, outline=outline_selected, width=4)
        selection_clic = 1
        selected = 1
        print(selection_clic, selected)
    elif (x1_white1 < x_event < x2_white1 and y1_white1 < y_event < y2_white1) and selection_clic == 1 and selected == 1: 
        white_piece_1 = canvas.create_oval(x1_white1, y1_white1, x2_white1, y2_white1, fill=color_player_one, outline=outline_white, width=4)
        selection_clic = 0
        selected = 0
        print(selection_clic, selected)
   
    
    if x1_white2 < x_event < x2_white2 and y1_white2 < y_event < y2_white2 and selection_clic == 0 and selected == 0:
        white_piece_1 = canvas.create_oval(x1_white1, y1_white1, x2_white1, y2_white1, fill=color_player_one, outline=outline_white, width=4)
        white_piece_2 = canvas.create_oval(x1_white2, y1_white2, x2_white2, y2_white2, fill=color_player_one, outline=outline_selected, width=4)
        selection_clic = 1
        selected = 1
        print(selection_clic, selected)
    elif x1_white2 < x_event < x2_white2 and y1_white2 < y_event < y2_white2 and selection_clic == 1 and selected == 1:
        white_piece_2 = canvas.create_oval(x1_white2, y1_white2, x2_white2, y2_white2, fill=color_player_one, outline=outline_white, width=4)
        selection_clic = 0
        selected = 0
        print(selection_clic, selected)


    # print(x1_white1, x2_white1, y1_white1, y2_white1)
    # print(canvas.coords(white_piece_1))
    # print(canvas.coords(white_piece_2))
    # print(canvas.coords(white_piece_3))

    # print(canvas.coords(black_piece_1))
    # print(canvas.coords(black_piece_2))
    # print(canvas.coords(black_piece_3))
     
    
    


def white_pieces(event):
    x = event.x
    y = event.y
    canvas.create_oval(x-30, y-30, x+30, y+30, fill="white", outline="white")

# Canvas

canvas = tk.Canvas(root, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, bg="moccasin")

boardgame = canvas.create_rectangle(100, 100, 500, 500, fill="moccasin", width=4, outline="black")
# boardgame = canvas.create_rectangle(100, 100, 500, 500, fill="pale goldenrod", width=4, outline="black")
# boardgame = tk.Canvas(root, height=500, width=500, bg="pale goldenrod", highlightbackground="black", highlightthickness=4)


vertical_line = canvas.create_line(600/2, 100, 600/2, 500, fill="black", width=4)
horizontal_line = canvas.create_line(100, 600/2, 500, 600/2, fill="black", width=4)
diag_line_1 = canvas.create_line(500, 100, 100, 500, fill="black", width=4)
diag_line_2 = canvas.create_line(100, 100, 500, 500, fill="black", width=4)

canvas.create_oval(100-10, 100-10, 100+10, 100+10, fill="black")
canvas.create_oval(600/2-10, 100-10, 600/2+10, 100+10, fill="black")
canvas.create_oval(500-10, 100-10, 500+10, 100+10, fill="black")

canvas.create_oval(100-10, 600/2-10, 100+10, 600/2+10, fill="black")
canvas.create_oval(600/2-10, 600/2-10, 600/2+10, 600/2+10, fill="black")
canvas.create_oval(500-10, 600/2-10, 500+10, 600/2+10, fill="black")

canvas.create_oval(100-10, 500-10, 100+10, 500+10, fill="black")
canvas.create_oval(600/2-10, 500-10, 600/2+10, 500+10, fill="black")
canvas.create_oval(500-10, 500-10, 500+10, 500+10, fill="black")

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

canvas.grid(row=0, column=0)

root.mainloop()
