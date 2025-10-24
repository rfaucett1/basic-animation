import pygame

def main():
    pygame.init()

    #Display settings
    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Fairy!")

    #Entities
    #image background
    background = pygame.Surface(screen.get_size())
    background_image = pygame.image.load("background_full.png").convert()
    background_image = pygame.transform.scale(background_image, (640, 480))
      
    #load an image
    fairy = pygame.image.load("fairy1.png")
    fairy = fairy.convert_alpha()
    fairy = pygame.transform.scale(fairy, (100, 100))
    fairy_rect = fairy.get_rect()
    
    #fairy variables
    fairy_x = 0
    fairy_y = 200

    #ACTION

        #Assign
    clock = pygame.time.Clock()
    keepGoing = True

        #Loop
    while keepGoing:

        #Time
        clock.tick(30)

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        #modify fairy value
        fairy_x -= 5
        #check boundaries
        if fairy_x < fairy.get_width():
            fairy_x = screen_width

        #Refresh screen
        screen.blit(background_image, (0, 0))
        screen.blit(fairy, (fairy_x, fairy_y))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()