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

#constante
L= 620



plateau= tk.Tk()

canvas = tk.Canvas(plateau,height=L, width=L ,bg='black')
canvas.grid(column=0 ,row=0)

#contourage 
canvas.create_rectangle(10, 10, L-10, L-10, width=5, outline="red")

line_a = canvas.create_line(10, 10, 30, 30,fill='red')
line_b = canvas.create_line(L-10, 10, L-30,30,fill='red')
line_c = canvas.create_line(10, L-10, 30, L-30,fill='red')
line_d = canvas.create_line(L-10,L-10,L-30, L-30,fill='red')

#quadrillage 
line_1 = canvas.create_line(30, 30,L-30, 30,fill='red')
line_2 = canvas.create_line(30,L-30,L-30, L-30,fill='red')
line_3 = canvas.create_line(30, L//2, L-30, L//2,fill='red')
line_4 = canvas.create_line(30, 30, 30, L-30,fill='red')
line_5 = canvas.create_line(L-30, 30, L-30, L-30,fill='red')
line_6 = canvas.create_line(L//2, 30, L//2, L-30,fill='red')
line_7 = canvas.create_line(30, 30, L-30, L-30,fill='red')
line_8 = canvas.create_line(30, L-30, L-30, 30,fill='red')

plateau.mainloop()