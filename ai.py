from game import Tetris, WIDTH, HEIGHT

def calculate_heuristic(grid):
    holes = 0
    max_height = 0
    bumpiness = 0
    heights = [0] * WIDTH

    for x in range(WIDTH):
        column_holes = 0
        for y in range(HEIGHT):
            if grid[y][x]:
                heights[x] = HEIGHT - y
                break
        for y in range(HEIGHT):
            if grid[y][x] == 0 and y < heights[x]:
                column_holes += 1
        holes += column_holes

    max_height = max(heights)
    for x in range(WIDTH - 1):
        bumpiness += abs(heights[x] - heights[x + 1])

    return -0.5 * holes - 0.3 * max_height - 0.2 * bumpiness

def best_move(game):
    best_score = float('-inf')
    best_position = None
    best_rotation = None

    for rotation in range(4):
        piece = rotate_piece(game.piece, rotation)
        for x in range(-2, WIDTH):
            offset = (x, 0)
            while game.valid_position(piece, (offset[0], offset[1] + 1)):
                offset = (offset[0], offset[1] + 1)
            game_copy = Tetris()
            game_copy.grid = [row[:] for row in game.grid]
            game_copy.place_piece(piece, offset)
            score = calculate_heuristic(game_copy.grid)
            if score > best_score:
                best_score = score
                best_position = offset
                best_rotation = rotation
    return best_position, best_rotation

def rotate_piece(piece, rotations):
    for _ in range(rotations):
        piece = [list(row) for row in zip(*piece[::-1])]
    return piece
