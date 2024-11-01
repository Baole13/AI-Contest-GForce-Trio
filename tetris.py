import pygame
from game import Tetris, WIDTH, HEIGHT, TILE_SIZE, COLORS
from ai import best_move, rotate_piece

# Các thông số cài đặt cho game
SCREEN_WIDTH, SCREEN_HEIGHT = WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Tetris()
    running = True

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Tìm vị trí tốt nhất và đặt khối
        position, rotation = best_move(game)
        if position:
            game.place_piece(rotate_piece(game.piece, rotation), position)
            game.piece = game.next_piece
            game.next_piece = game.new_piece()

        # Vẽ game
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if game.grid[y][x]:
                    pygame.draw.rect(screen, COLORS[game.grid[y][x]], pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
