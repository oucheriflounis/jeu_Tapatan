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
L= 600


def restart(event):
    pass



sj1=0
sj2=0


plateau= tk.Tk()

canvas = tk.Canvas(plateau,height=L, width=L ,bg='black')
canvas.grid(columnspan =3 ,rowspan = 2 )






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

score = tk.Label(plateau, text="  J1  " + str(sj1) + "  -  " + str(sj2)+ "  J2  ", font=("calibri", 30), bg="red", padx=185)
score.grid(row=2, columnspan = 3)


redemarer = tk.Button(plateau, text= "redemarer", padx=10, pady= 10, bg="white", command=restart)
redemarer.grid(column=0, row=3)

reprendre = tk.Button(plateau, text= "reprendre", padx=10, pady= 10, bg="white", command=restart)
reprendre.grid(column=1, row=3)

sauvgarder = tk.Button(plateau, text= "sauvgarder", padx=10, pady= 10, bg="green", command=restart)
sauvgarder.grid(column=2, row=3)

h_vs_h = tk.Button(plateau, text= " J1 vs J2 ", padx=10, pady= 10, bg="red", command=restart)
h_vs_h.grid(column=3, row=0)

h_vs_IA = tk.Button(plateau, text= " J1 vs IA ", padx=10, pady= 10, bg="red", command=restart)
h_vs_IA.grid(column=3, row=1)

IA_vs_IA = tk.Button(plateau, text= " IA vs IA ", padx=10, pady= 10, bg="red", command=restart)
IA_vs_IA.grid(column=3, row=2)



plateau.mainloop()
