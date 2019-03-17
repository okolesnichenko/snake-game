import tkinter as tk
from tkinter import *
from random import randint
from random import randrange
import time
import keyboard

WIDTH = 600
HEIGHT = 600
SIZE_BLOCK = 20
#tkinter settings + canvas
root = Tk()
canvas = Canvas(root, width = WIDTH, height = HEIGHT, bg = '#2f353b')
canvas.pack()
lastPressed = 'a'
snake = [[WIDTH//2,HEIGHT//2], [WIDTH//2 + SIZE_BLOCK,HEIGHT//2], [WIDTH//2 + 2*SIZE_BLOCK,HEIGHT//2]]
#draw snake and apple
def draw(snake, x, y):
    canvas.delete("all")
    for dot in snake:
        canvas.create_rectangle(dot[0], dot[1], dot[0] + SIZE_BLOCK, dot[1]+SIZE_BLOCK, fill = '#dad871', outline = '#dad871')
    canvas.create_rectangle(x, y, x + SIZE_BLOCK, y+SIZE_BLOCK, fill = '#c51d34', outline = '#c51d34')
#pop element and update picture
def popAndDraw(snake, x, y):
    if(snake[0]!=[x,y]):
        snake.pop()
    time.sleep(0.1)
    draw(snake, x, y)
    root.update()
#move and check eatd apple
def move(snake, lastPressed, x, y):
    if(lastPressed == 'w'):
        snake.insert(0, [snake[0][0], snake[0][1]-SIZE_BLOCK])
        popAndDraw(snake, x, y)
    elif(lastPressed == 'a'):
        snake.insert(0, [snake[0][0]-SIZE_BLOCK, snake[0][1]])
        popAndDraw(snake, x, y)
    elif(lastPressed == 'd'):
        snake.insert(0, [snake[0][0]+SIZE_BLOCK, snake[0][1]])
        popAndDraw(snake, x, y)
    elif(lastPressed == 's'):
        snake.insert(0, [snake[0][0], snake[0][1]+SIZE_BLOCK])
        popAndDraw(snake, x, y)
#fails
def endGame(snake):
    count = 0
    for c in snake:
        if(snake[0] == c):
            count += 1
    if(count == 2):
        return True
    if((snake[0][0] < 0) | (snake[0][0] > 580)):
        return True
    if((snake[0][1] < 0) | (snake[0][1] > 580)):
        return True
#coord of apple
def game():
    lastPressed = 'a'
    snake = [[HEIGHT//2,WIDTH//2], [HEIGHT//2 + SIZE_BLOCK,WIDTH//2], [HEIGHT//2 + 2*SIZE_BLOCK,WIDTH//2]]
    x = randrange(0, 580, 20)
    y = randrange(0, 580, 20)
    draw(snake, x, y)
    root.update()
    while (keyboard.is_pressed('q') == False):
        if(keyboard.is_pressed('w') & (lastPressed != 's')):
            lastPressed = 'w'
        elif(keyboard.is_pressed('a') & (lastPressed != 'd')):
            lastPressed = 'a'
        elif(keyboard.is_pressed('d') & (lastPressed != 'a')):
            lastPressed = 'd'
        elif(keyboard.is_pressed('s') & (lastPressed != 'w')):
            lastPressed = 's'
        move(snake, lastPressed, x, y)
        if(snake[0]==[x,y]):
            x = randrange(0, 580, 20)
            y = randrange(0, 580, 20)
        if(endGame(snake)):
            break
def main():
    #Start game
    game()
    while True:
        if keyboard.is_pressed('f'):
            game()
        if keyboard.is_pressed('q'):
            break

    # canvas.create_text(WIDTH//2 - 10, HEIGHT//2 + 40, text = "Press F to start", font="Arial 15", fill="white")
    # need to start again



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()