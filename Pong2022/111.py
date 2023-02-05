import pygame
#print(pygame.font.get_fonts())

pygame.init()
sc = pygame.display.set_mode((300, 200))
sc.fill((255, 255, 255))

f2 = pygame.font.SysFont('algerian', 48)
left_score = 0

score_left_text = f2.render(str(left_score), True,
                  (255, 180, 0))
 
sc.blit(score_left_text, (100, 10))

pygame.display.update()
