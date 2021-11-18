# https://www.acmicpc.net/problem/3190

from collections import deque
import sys
input = sys.stdin.readline


def snake_game(N, apple, direction):
    time = 0
    col = 1
    row = 1
    snake.append([row, col])
    l = direction.popleft()

    for _ in range(int(l[0])):  # 디렉션에 적힌 초만큼 이동 오른쪽.(열증가)
        col += 1
        before = snake[-1]
        if not ( [row, col] in apple):
            snake.popleft()
        else:
            apple.remove([row, col])
        snake.append([row, col])
        time += 1
        if col > N :
            return time

    while True:

        if l[1] == 'D':
            try:
                l = direction.popleft()
                if snake[-1][1]-before[1] > 0:  # 열증가중
                    for _ in range(int(l[0])-time):
                        row += 1
                        before = snake[-1]
                        if row > N or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                            snake.popleft()
                        else:
                            apple.remove([row, col])
                            
                        snake.append([row, col])
                        time += 1

                elif snake[-1][1]-before[1] < 0:  # 열감소중

                    for _ in range(int(l[0])-time):
                        row -= 1
                        before = snake[-1]
                        if row < 1 or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                            snake.popleft()
                        else:
                            apple.remove([row, col])
                    
                        snake.append([row, col])
                        time += 1

                elif snake[-1][0]-before[0] > 0:  # 행증가중

                    for _ in range(int(l[0])-time):
                        col -= 1
                        before = snake[-1]
                        if col < 1 or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                            snake.popleft()
                        else:
                            apple.remove([row, col])
                      

                        snake.append([row, col])
                        time += 1

                elif snake[-1][0]-before[0] < 0:  # 행감소중

                    for _ in range(int(l[0])-time):
                        col += 1
                        before = snake[-1]
                        if col > N or [row, col] in snake:
                            time += 1
                            return time

                        if not ([row, col] in apple):
                            snake.popleft()
                        else:
                            apple.remove([row, col])
                   
                        snake.append([row, col])
                        time += 1
            except:
                if snake[-1][1]-before[1] > 0:  # 열증가중
                    while True:
                        row += 1
                        if row > N or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                            snake.popleft()
                        else:
                            apple.remove([row, col])
                   

                        snake.append([row, col])
                        time += 1

                elif snake[-1][1]-before[1] < 0:  # 열감소중

                    while True:
                        row -= 1
                        if row < 1 or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                            snake.popleft()
                        else:
                            apple.remove([row, col])
               

                        snake.append([row, col])
                        time += 1

                elif snake[-1][0]-before[0] > 0:  # 행증가중

                    while True:
                        col -= 1
                        if col < 1 or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                            snake.popleft()
                        else:
                            apple.remove([row, col])
                        

                        snake.append([row, col])
                        time += 1

                elif snake[-1][0]-before[0] < 0:  # 행감소중

                    while True:
                        col += 1
                        if col > N or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                            snake.popleft()
                        else:
                            apple.remove([row, col])

                        

                        snake.append([row, col])
                        time += 1

        elif l[1] == 'L':
            try:
                l = direction.popleft()
                if snake[-1][1]-before[1] > 0:  # 열증가중

                    for _ in range(int(l[0])-time):
                        row -= 1
                        before = snake[-1]
                        if row < 1 or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                            snake.popleft()
                        else:
                            apple.remove([row, col])
                        

                        snake.append([row, col])
                        time += 1

                elif snake[-1][1]-before[1] < 0:  # 열감소중

                    for _ in range(int(l[0])-time):
                        row += 1
                        before = snake[-1]
                        if row > N or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                           snake.popleft()
                        else:
                            apple.remove([row, col])
                        

                        snake.append([row, col])
                        time += 1

                elif snake[-1][0]-before[0] > 0:  # 행증가중

                    for _ in range(int(l[0])-time):
                        col += 1
                        before = snake[-1]
                        if col > N or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                                snake.popleft()
                        else:
                            apple.remove([row, col])
                        

                    snake.append([row, col])
                    time += 1

                elif snake[-1][0]-before[0] < 0:  # 행감소중

                    for _ in range(int(l[0])-time):
                        col -= 1
                        before = snake[-1]
                        if col < 1 or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                            snake.popleft()
                        else:
                            apple.remove([row, col])

                        

                    snake.append([row, col])
                    time += 1
            except:
                if snake[-1][1]-before[1] > 0:  # 열증가중
                    while True:
                        row -= 1
                        if row < 1 or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                           snake.popleft()
                        else:
                            apple.remove([row, col])
                       
                        snake.append([row, col])
                        time += 1

                elif snake[-1][1]-before[1] < 0:  # 열감소중
                    while True:
                        row += 1
                        if row > N or [row, col] in snake:
                            time += 1
                            return time

                        if not ([row, col] in apple):
                           snake.popleft()
                        else:
                            apple.remove([row, col])
                       
                        snake.append([row, col])
                        time += 1

                elif snake[-1][0]-before[0] > 0:  # 행증가중

                    while True:
                        col += 1
                        if col > N or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                          snake.popleft()
                        else:
                            apple.remove([row, col])
                      

                        snake.append([row, col])
                        time += 1

                elif snake[-1][0]-before[0] < 0:  # 행감소중

                    while True:
                        col -= 1
                        if col < 1 or [row, col] in snake:
                            time += 1
                            return time
                        if not ([row, col] in apple):
                            snake.popleft()
                        else:
                            apple.remove(snake[-1])
                       

                        snake.append([row, col])
                        time += 1


N = int(input())

K = int(input())
apple = [list(map(int, input().strip().split()))for _ in range(K)]

L = int(input())
direction = deque(input().strip().split()for _ in range(L))

snake = deque()

print(snake_game(N, apple, direction))
