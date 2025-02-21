import pygame

# Pygame initialisieren
pygame.mixer.init()

# MP3-Datei laden
pygame.mixer.music.load('./viking-toms-loop-240499.mp3')  # Ersetze 'dein_sound.mp3' durch den Namen deiner MP3-Datei

# Sound abspielen
pygame.mixer.music.play()

# Warten, bis der Sound beendet ist
while pygame.mixer.music.get_busy():
    pass

pygame.quit()