import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Define colors
background_colour = (0, 0, 0)
circle_colour = (255, 255, 255)
second_circle_colour = (255, 255, 255)

black = (0, 0, 0)
white = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Leaves Alpha 0.0.1")

# Load and set the font
font = pygame.font.Font("minecraft_font.ttf", 32)

text = font.render("Leaves Alpha 0.0.1", False, white)

textRect = text.get_rect()

#list for circles
circles = []


# Set the center of the rectangular object.
textRect.center = (180, 20)

# Set the clock for controlling the frame rate
fps = pygame.time.Clock()

circle_speed = 3
second_circle_speed = 3

running = True

circle_center_x = 400
circle_center_y = 300
circle_radius = 30

second_circle_center_x = 700
second_circle_center_y = 600
second_circle_radius = 30


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current state of the keyboard
    keys = pygame.key.get_pressed()

    # Update circle position based on WASD keys
    if keys[pygame.K_w]:  # Move up
        circle_center_y -= circle_speed
    if keys[pygame.K_s]:  # Move down
        circle_center_y += circle_speed
    if keys[pygame.K_a]:  # Move left
        circle_center_x -= circle_speed
    if keys[pygame.K_d]:  # Move right
        circle_center_x += circle_speed

    # Update second circle position based on arrow keys
    if keys[pygame.K_UP]:
        second_circle_center_y -= second_circle_speed
    if keys[pygame.K_DOWN]:
        second_circle_center_y += second_circle_speed
    if keys[pygame.K_LEFT]:
        second_circle_center_x -= second_circle_speed
    if keys[pygame.K_RIGHT]:
        second_circle_center_x += second_circle_speed

    # Fill the screen with the background color
    screen.fill(background_colour)

    # Draw the circles at the new positions
    pygame.draw.circle(screen, circle_colour, (circle_center_x, circle_center_y), circle_radius)
    pygame.draw.circle(screen, second_circle_colour, (second_circle_center_x, second_circle_center_y),
                       second_circle_radius)

    # Blit the text last to ensure it appears on top
    screen.blit(text, textRect)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    fps.tick(60)

# Quit Pygame
pygame.quit()

