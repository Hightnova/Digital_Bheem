from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

# Initialize mixer
mixer.init()

def add_music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

def play_music():
    selected_song = playlist.curselection()
    if selected_song:
        song_index = int(selected_song[0])
        song = playlist.get(song_index)
        mixer.music.load(song)
        mixer.music.play()

def stop_music():
    mixer.music.stop()

def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

# Create main window
root = Tk()
root.title('Music Player')
root.geometry("600x400")
root.configure(bg="#0f1a2b")

# Background image
background_image = PhotoImage(file="logo.png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create playlist
playlist_frame = Frame(root, bg="white", bd=5)
playlist_frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.4, anchor="n")

playlist_label = Label(playlist_frame, text="Playlist", fg="black", font=("Arial", 12))
playlist_label.pack()

scrollbar = Scrollbar(playlist_frame)
scrollbar.pack(side=RIGHT, fill=Y)

playlist = Listbox(playlist_frame, bg="lightgray", fg="black", selectbackground="lightblue", bd=0, yscrollcommand=scrollbar.set, font=("Arial", 10))
playlist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=playlist.yview)

# Create control buttons
control_frame = Frame(root, bg="#0f1a2b")
control_frame.place(relx=0.5, rely=0.6, relwidth=0.8, relheight=0.1, anchor="n")

button_add = Button(control_frame, text="Add Music", font=("Arial", 12), fg="white", bg="#21b3de", command=add_music)
button_add.grid(row=0, column=0, padx=10)

button_play = Button(control_frame, text="Play", font=("Arial", 12), fg="white", bg="#21b3de", command=play_music)
button_play.grid(row=0, column=1, padx=10)

button_stop = Button(control_frame, text="Stop", font=("Arial", 12), fg="white", bg="#21b3de", command=stop_music)
button_stop.grid(row=0, column=2, padx=10)

button_pause = Button(control_frame, text="Pause", font=("Arial", 12), fg="white", bg="#21b3de", command=pause_music)
button_pause.grid(row=0, column=3, padx=10)

button_resume = Button(control_frame, text="Resume", font=("Arial", 12), fg="white", bg="#21b3de", command=resume_music)
button_resume.grid(row=0, column=4, padx=10)

root.mainloop()
