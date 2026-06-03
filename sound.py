import pygame
import keyboard

# Initialize audio
pygame.mixer.init()

# Load your sound
sound = pygame.mixer.Sound("anime-ahh.mp3")

# Function to play sound
def play_sound(event):
    sound.play()

# Listen for key press
keyboard.on_press_key("a", play_sound)

print("Press 'a' to play sound")

keyboard.wait()