#!/usr/bin/env python3
"""
五子棋双人对战游戏（终端版）
"""

BOARD_SIZE = 15
EMPTY = '.'  # 空位符号


def create_board():
    """创建空棋盘"""
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board):
    """打印棋盘"""
    # 顶部列坐标标注
    print('    ' + ' '.join(str(i) for i in range(BOARD_SIZE)))
    print('   ┌' + '─' * (BOARD_SIZE * 2 - 1) + '┐')
    for i, row in enumerate(board):
        # 左侧行坐标标注
        print(f' {i} │ ' + ' '.join(row) + ' │')
    print('   └' + '─' * (BOARD_SIZE * 2 - 1) + '┘')
    # 底部坐标说明
    print('    x (列) →')
    print('    ↓')
    print('    y (行)')


def is_valid_move(board, x, y):
    """检查落子是否有效"""
    if not (0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE):
        return False
    return board[y][x] == EMPTY


def place_piece(board, x, y, piece):
    """放置棋子"""
    board[y][x] = piece


def check_win(board, x, y, piece):
    """检查是否获胜"""
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for dx, dy in directions:
        count = 1

        # 正向检查
        nx, ny = x + dx, y + dy
        while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == piece:
            count += 1
            nx += dx
            ny += dy

        # 反向检查
        nx, ny = x - dx, y - dy
        while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == piece:
            count += 1
            nx -= dx
            ny -= dy

        if count >= 5:
            return True

    return False


def is_board_full(board):
    """检查棋盘是否已满"""
    for row in board:
        if EMPTY in row:
            return False
    return True


def get_coordinates(player_input):
    """解析玩家输入的坐标"""
    try:
        parts = player_input.strip().split()
        if len(parts) != 2:
            return None
        x, y = int(parts[0]), int(parts[1])
        return x, y
    except ValueError:
        return None


def play_game():
    """开始游戏"""
    board = create_board()
    players = [('●', '黑方'), ('○', '白方')]
    current = 0

    print('=== 五子棋双人对战 ===')
    print(f'棋盘大小: {BOARD_SIZE}x{BOARD_SIZE}')
    print('输入格式: x y (列 行)')
    print('示例: 7 7 表示第7列第7行（天元）')
    print()

    while True:
        print_board(board)
        piece, name = players[current]
        print(f'\n{name} ({piece}) 下棋')

        while True:
            player_input = input('请输入坐标 (x y): ').strip()
            if player_input.lower() == 'q':
                print('游戏结束')
                return

            coords = get_coordinates(player_input)
            if coords is None:
                print('输入无效，请输入两个数字（列 行），如: 7 7')
                continue

            x, y = coords
            if not is_valid_move(board, x, y):
                print('无效位置，该位置已有棋子或超出范围')
                continue

            break

        place_piece(board, x, y, piece)

        if check_win(board, x, y, piece):
            print_board(board)
            print(f'\n🎉 {name} 获胜!')
            break

        # 检查平局
        if is_board_full(board):
            print_board(board)
            print('\n⚖️ 棋盘已满，平局!')
            break

        current = 1 - current

    # 询问是否重新开始
    while True:
        restart = input('\n是否重新开始? (y/n): ').strip().lower()
        if restart == 'y':
            play_game()
            return
        elif restart == 'n':
            print('感谢游玩，再见!')
            return
        else:
            print('请输入 y 或 n')


if __name__ == '__main__':
    play_game()