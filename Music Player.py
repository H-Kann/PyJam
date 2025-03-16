import pygame
import os

pygame.init()
# --------------------------Path of the music folder--------- #
path = "Music folder path"

obj = os.scandir(path)
musicList = []
for file in obj:
    if file.is_file and file.name.endswith("mp3"):
        musicList.append(file)
print(musicList)



pygame.mixer.music.load(musicList[0])
musicList.pop(0)
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play()

if len(musicList) > 0:

    pygame.mixer.music.queue(musicList[0])
    musicList.pop(0)
    
MUSIC_END = pygame.USEREVENT
pygame.mixer.music.set_endevent(MUSIC_END)

running = True
while running:

    for event in pygame.event.get(): 

        if event.type == MUSIC_END:
            print("Song Finished")

            if len(musicList) > 0:
                pygame.mixer.music.queue(musicList[0])
                musicList.pop(0)

        if not pygame.mixer.music.get_busy(): 
            print("Playlist completed") 
                
            running = False
            break