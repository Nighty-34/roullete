import tkinter as tk
import random
import time
HEIGHT = 300
WIDTH = 500

root = tk.Tk()
root.title('rullet')
ch1 = 'red'
ch2 = 'black'
ch3 = 'lime green'
logo = tk.PhotoImage(file='gaming.png')
root.call('wm', 'iconphoto', root._w, logo)
 
r1, r2, r3, r4 = 150, 80, 90, 100
y1, y2, y3, y4 = 30, 100, 140, 50
z1, z2, z3, z4 = 150, 220, 210, 200
c1, c2, c3, c4 = 170, 100, 60, 150
def start():
    r1, r2, r3, r4 = 120, 75, 110, 90
    y1, y2, y3, y4 = 35, 130, 160, 65
    z1, z2, z3, z4 = 180, 225, 190, 210
    c1, c2, c3, c4 = 165, 70, 40, 135
    
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='rullet.png')
background_label = tk.Label(canvas, image=background_image)
background_label.place(relwidth=1, relheight=1)
frame = tk.Frame(root, bd=5, background='')
frame.place(relx=0.5, rely=0.02, relwidth=0.75, relheight=6, anchor='n')
label = tk.Label(frame, text='winner color-->')
label.place(relx=0.3, relheight=0.02, relwidth=0.24)
canvas1 = tk.Canvas(root, height=200, width=300)
canvas1.pack(expand=True)
canvas1.place(relx=0.5, rely=0.5, anchor="center")
canvas1.create_oval(80,30,220,170,fill="saddle brown")
canvas1.create_oval(90,40,210,160, width=1.5)
canvas1.create_line(r1, y1, z1, c1, fill='black', width=3)
canvas1.create_line(r2, y2, z2, c2, fill='black', width=3)
canvas1.create_line(r3, y3, z3, c3, fill='black', width=3)
canvas1.create_line(r4, y4, z4, c4, fill='black', width=3)

def redbut(): 
    x = random.randint(0,38)
    if x <= 18:
        start()
        label2 = tk.Label(frame, text='you won')
        label2.place(relx=0.7, relheight=0.02)
        label = tk.Label(frame, background='red') 
        label.place(relx=0.6, relheight=0.02, relwidth=0.1)
        
    elif x >= 19 and x <= 36:
        start()       
        label2 = tk.Label(frame, text='you lost')
        label2.place(relx=0.7, relheight=0.02) 
        label = tk.Label(frame, background='black')
        label.place(relx=0.6, relheight=0.02, relwidth=0.1)
    elif x >= 37:
        start()       
        label2 = tk.Label(frame, text='you lost')
        label2.place(relx=0.7, relheight=0.02) 
        label = tk.Label(frame, background='lime green')
        label.place(relx=0.6, relheight=0.02, relwidth=0.1)  
def blackbut():
    x = random.randint(0,38)
    if x <= 18:
        label2 = tk.Label(frame, text='you lost')
        label2.place(relx=0.7, relheight=0.02)
        label = tk.Label(frame, background='red')
        label.place(relx=0.6, relheight=0.02, relwidth=0.1)        
    elif x >= 19 and x <= 36:
        label2 = tk.Label(frame, text='you won')
        label2.place(relx=0.7, relheight=0.02)
        label = tk.Label(frame, background='black')
        label.place(relx=0.6, relheight=0.02, relwidth=0.1)        
    elif x >= 37:
        label2 = tk.Label(frame, text='you lost')
        label2.place(relx=0.7, relheight=0.02)
        label = tk.Label(frame, background='lime green')
        label.place(relx=0.6, relheight=0.02, relwidth=0.1)
def greenbut():
    x = random.randint(0,38)
    if x <= 18:
        label2 = tk.Label(frame, text='you lost')
        label2.place(relx=0.7, relheight=0.02)
        label = tk.Label(frame, background='red')
        label.place(relx=0.6, relheight=0.02, relwidth=0.1)        
    elif x >= 19 and x <= 36:
        label2 = tk.Label(frame, text='you lost')
        label2.place(relx=0.7, relheight=0.02) 
        label = tk.Label(frame, background='black')
        label.place(relx=0.6, relheight=0.02, relwidth=0.1)        
    elif x >= 37:
        label2 = tk.Label(frame, text='you won')
        label2.place(relx=0.7, relheight=0.02)
        label = tk.Label(frame, background='lime green')
        label.place(relx=0.6, relheight=0.02, relwidth=0.1)        
        

button = tk.Button(frame, font=40, background='red', command=redbut)
button.place(relx=0, rely=0, relheight=0.02, relwidth=0.1)

button1 = tk.Button(frame, font=40, background='black', command=blackbut)
button1.place(relx=0.1, relheight=0.02, relwidth=0.1)

button2 = tk.Button(frame, font=40, background='lime green', command=greenbut)
button2.place(relx=0.2, relheight=0.02, relwidth=0.1)

root.mainloop()