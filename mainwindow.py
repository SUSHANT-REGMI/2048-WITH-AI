from tkinter import *
import tkinter as ttk

from PIL import ImageTk, Image
import game_2048

import game_display

root = ttk.Tk()
root.iconbitmap('images/2048.ico')
root.title('2048')
root.resizable(width=False, height=False)


class mainwindow():
    def __init__(self):
        bg = ImageTk.PhotoImage(Image.open("images/welcome.png"))

        my_canvas = Canvas(root, width=700, height=550)
        my_canvas.grid()

        my_canvas.create_image(0, 0, image=bg, anchor=NW)

        button1 = Button(root, text="New Game", fg="black", bg="#ddf0d0", padx=3,
                         command=lambda: game_2048.main(root),
                         pady=3, font=('Helvetica', '12', 'bold'), activebackground="#94d3c3",
                         )
        button2 = Button(root, text="AI Mode", fg="black", bg="#ddf0d0",
                         padx=3, command=lambda: game_display.main(root), 
                         pady=3, font=('Helveica', '12', 'bold'), activebackground="#94d3c3")
                         
        button1_window = my_canvas.create_window(
            10, 10, anchor=NW, window=button1)
        button2_window = my_canvas.create_window(
            120, 10, anchor=NW, window=button2)

        FactsTexts = my_canvas.create_text(
            10, 350, anchor=NW, text="How to play the game", font=(
                'Comic Sans MS', '20', 'bold'))

        Facts_1 = my_canvas.create_text(
            10, 400, anchor=NW, text="- For New Game Mode:\n  Use left, right, up and down arrow key for respective moves.", font=(
                'Comic Sans MS', '15'))

        
        Facts_3 = my_canvas.create_text(
            10, 460, anchor=NW, text="- For AI mode:\n  Use 'a','s','d','w' for left, down, right up,", font=(
                'Comic Sans MS', '15'))
        Facts_4 = my_canvas.create_text(
            10, 513, anchor=NW, text="  'p' for Full AI mode & 'q' for Hint.", font=(
                'Comic Sans MS', '15'))
        root.mainloop()


win1 = mainwindow()

