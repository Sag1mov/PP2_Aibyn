import pygame
from tkinter import filedialog
from tkinter import *
import os

root = Tk()
root.title('AIUmusic')
root.geometry("500x290")


pygame.mixer.init()

slist = Listbox(root, bg = "lightgreen", fg="black", width=100, height=15 )
slist.pack()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song = " "
paused = False


def load_music():
    global current_song
    root.directory = filedialog.askdirectory()
    for s in os.listdir(root.directory):
        name, ext  = os.path.splitext(s)
        if ext == '.mp3':
            songs.append(s)
    
    for s in songs:
        slist.insert("end", s)
        
    slist.selection_set(0)
    current_song = songs[slist.curselection()[0]]

def play_music():
    global current_song, paused
    
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False
        
def pause_music():
    global pause
    pygame.mixer.music.pause()
    paused = True
def next_music():
    global current_song, paused
    
    try:
        slist.selection_clear(0, END)
        slist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
    
def prev_music():
    
    global current_song, paused
    
    try:
        slist.selection_clear(0, END)
        slist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
    

    


    

organise_menu = Menu(menubar, tearoff= False)
organise_menu.add_command(label='Select folder', command= load_music)
menubar.add_cascade(label='organise', menu = organise_menu )

play_btn_image = PhotoImage(file='play.png')
pause_btn_image = PhotoImage(file='pause.png')
next_btn_image = PhotoImage(file='next.png')
prev_btn_image = PhotoImage(file='previous.png')

control_frame = Frame(root)
control_frame.pack()


play_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command= play_music)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command= next_music)
prev_btn = Button(control_frame, image=prev_btn_image, borderwidth=0, command= prev_music)

play_btn.grid(row=0, column=2, padx= 7, pady= 10)
pause_btn.grid(row=0, column=1, padx= 7, pady= 10)
next_btn.grid(row=0, column=4, padx= 7, pady= 10)
prev_btn.grid(row=0, column=3, padx= 7, pady= 10)



root.mainloop() 