import random
import string

# 그리드 초기화
grid_size = 10
grid = [["" for _ in range(grid_size)] for _ in range(grid_size)]

# 사전 단어 목록
dictionary = {"PYTHON", "JAVA", "PUZZLE", "CODING", "SEARCH"}
words = ["PYTHON", "JAVA", "PUZZLE", "CODING", "SEARCH"]

# 단어를 무작위한 위치와 방향으로 배치하는 함수
def place_word(grid, word):
    directions = [
        (0, 1),   # 수평 (좌에서 우로)
        (1, 0),   # 수직 (상에서 하로)
        (1, 1),   # 대각선 (좌상에서 우하)
        (-1, 1)   # 대각선 (우상에서 좌하)
    ]
    grid_size = len(grid)

    for _ in range(100):  # 최대 100번 시도
        direction = random.choice(directions)
        start_row = random.randint(0, grid_size - 1)
        start_col = random.randint(0, grid_size - 1)

        end_row = start_row + (len(word) - 1) * direction[0]
        end_col = start_col + (len(word) - 1) * direction[1]

        if 0 <= end_row < grid_size and 0 <= end_col < grid_size:
            overlap = False
            for i in range(len(word)):
                row = start_row + i * direction[0]
                col = start_col + i * direction[1]
                if grid[row][col] != "" and grid[row][col] != word[i]:
                    overlap = True
                    break
            
            if not overlap:
                for i in range(len(word)):
                    row = start_row + i * direction[0]
                    col = start_col + i * direction[1]
                    grid[row][col] = word[i]
                return True  # 단어 배치 성공
    return False  # 단어 배치 실패

# 무작위 문자로 빈 공간 채우기
def fill_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "":
                grid[row][col] = random.choice(string.ascii_uppercase)

# 그리드의 모든 단어를 추출하여 검증
def check_grid(grid):
    words = set()
    
    # 행 검사
    for row in grid:
        words.add("".join(row))
    
    # 열 검사
    for col in range(len(grid[0])):
        column_word = "".join([grid[row][col] for row in range(len(grid))])
        words.add(column_word)
    
    # 대각선 검사
    # 좌상에서 우하
    words.add("".join([grid[i][i] for i in range(len(grid))]))
    # 우상에서 좌하
    words.add("".join([grid[i][len(grid) - 1 - i] for i in range(len(grid))]))
    
    # 사전 단어와 비교
    matching_words = words & dictionary
    return matching_words

# 단어를 무작위한 방향으로 배치하기
for word in words:
    place_word(grid, word)

# 무작위 문자로 그리드 채우기
fill_grid(grid)

# 그리드 검사
matches = check_grid(grid)

if matches:
    print("Unexpected words found:", matches)
else:
    print("No unexpected words found")

# 퍼즐 출력
for row in grid:
    print(' '.join(row))