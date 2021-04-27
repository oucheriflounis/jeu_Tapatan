from tkinter import*
import subprocess


fenetre=Tk()
fenetre.title("jeu")
fond=Canvas(fenetre,width=800,height=600,bg="white")

def run_Tapatan():
    subprocess.run("py ./HvH_Jeu.py")

#Menu déroulant
menuBar = Menu(fenetre)
fenetre['menu'] = menuBar
sousMenu = Menu(menuBar,tearoff = 0)
menuBar.add_cascade(label='Menu', menu=sousMenu)
sousMenu.add_command(label='Quitter', command=fenetre.destroy)
sousMenu.add_command(label="Tapatan", command = run_Tapatan)

Img_IAvsH = PhotoImage(file = "IA_VS_Humain.PNG")
background = fond.create_image(200,150, image = Img_IAvsH)
Img_HvsH = PhotoImage(file = "Humain_VS_Humain.PNG")
background = fond.create_image(600,150, image = Img_HvsH)
Img_IAvsIA = PhotoImage(file = "IA_VS_IA.PNG")
background = fond.create_image(400,320, image = Img_IAvsIA)

#replacer le nom dans subprocess en fonction des différents programmes
def clic_gauche(event):
    if (50<event.x<350)  and (65<event.y<233):
        subprocess.run("py ./HvH_Jeu.py")
    if (450<event.x<750)  and (65<event.y<233):
        subprocess.run("py ./HvH_Jeu.py")
    if (250<event.x<550)  and (240<event.y<400):
        subprocess.run("py ./HvH_Jeu.py")
    

fond.bind("<Button-1>", clic_gauche)
fond.pack()
fond.mainloop()
