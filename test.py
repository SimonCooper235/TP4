import pygame
import pymunk
import pymunk.pygame_util

# --- Initialize Pygame ---
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pymunk Pause Example")
clock = pygame.time.Clock()

# --- Initialize Pymunk Space ---
space = pymunk.Space()
space.gravity = (0, 900)  # Gravity pointing down

# --- Create a ball ---
body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 30))
body.position = (400, 100)
shape = pymunk.Circle(body, 30)
shape.elasticity = 0.8
space.add(body, shape)

# --- Create a static floor ---
floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
floor_shape = pymunk.Segment(floor_body, (0, 550), (800, 550), 5)
floor_shape.elasticity = 0.8
space.add(floor_body, floor_shape)

# --- Draw options ---
draw_options = pymunk.pygame_util.DrawOptions(screen)

# --- Pause flag ---
paused = False

# --- Main loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Toggle pause with SPACE key
                paused = not paused

    # --- Update physics only if not paused ---
    if not paused:
        space.step(1 / 60.0)  # Advance simulation by 1/60 second

    # --- Drawing ---
    screen.fill((255, 255, 255))
    space.debug_draw(draw_options)

    # Display pause text
    if paused:
        font = pygame.font.SysFont(None, 48)
        text = font.render("PAUSED", True, (255, 0, 0))
        screen.blit(text, (350, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

