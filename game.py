import random

# Cấu hình trò chơi
WIDTH, HEIGHT = 10, 20  # Kích thước lưới Tetris
TILE_SIZE = 30  # Kích thước mỗi ô
COLORS = [
    (0, 0, 0),      # Màu sắc nền
    (255, 85, 85),  # Màu khối I
    (100, 200, 115), # Màu khối T
    (120, 108, 245), # Màu khối Z
    (255, 140, 50), # Màu khối S
    (50, 120, 52),  # Màu khối L
    (146, 202, 73), # Màu khối J
    (150, 161, 218) # Màu khối O
]

SHAPES = [
    [[1, 1, 1, 1]],         # Hình chữ I
    [[1, 1, 1], [0, 1, 0]], # Hình chữ T
    [[1, 1, 0], [0, 1, 1]], # Hình chữ Z
    [[0, 1, 1], [1, 1, 0]], # Hình chữ S
    [[1, 1, 1], [1, 0, 0]], # Hình chữ L
    [[1, 1, 1], [0, 0, 1]], # Hình chữ J
    [[1, 1], [1, 1]]        # Hình chữ O
]

class Tetris:
    def __init__(self):
        self.grid = [[0] * WIDTH for _ in range(HEIGHT)]  # Lưới trò chơi
        self.score = 0  # Điểm số
        self.piece = self.new_piece()  # Khối hiện tại
        self.next_piece = self.new_piece()  # Khối tiếp theo

    def new_piece(self):
        """Tạo một khối mới ngẫu nhiên."""
        return [row[:] for row in random.choice(SHAPES)]

    def valid_position(self, piece, offset):
        """Kiểm tra xem khối có thể đặt vào vị trí mong muốn không."""
        offset_x, offset_y = offset
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell:  # Nếu là ô không rỗng
                    # Kiểm tra biên giới lưới
                    if (x + offset_x < 0 or x + offset_x >= WIDTH or
                        y + offset_y >= HEIGHT or self.grid[y + offset_y][x + offset_x]):
                        return False
        return True

    def place_piece(self, piece, offset):
        """Đặt khối vào lưới."""
        offset_x, offset_y = offset
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell:
                    # Kiểm tra giới hạn của lưới để tránh lỗi vượt chỉ số
                    if 0 <= y + offset_y < HEIGHT and 0 <= x + offset_x < WIDTH:
                        self.grid[y + offset_y][x + offset_x] = cell
        self.clear_lines()

    def clear_lines(self):
        """Xóa các dòng đầy trong lưới."""
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        cleared_lines = HEIGHT - len(new_grid)
        self.score += cleared_lines ** 2
        self.grid = [[0] * WIDTH for _ in range(cleared_lines)] + new_grid
