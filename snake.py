import tkinter as tk
from tkinter import *
from random import randint
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
snake = [[300,300], [320, 300], [340, 300], [360, 300], [380, 300]]

def drawSnake(snake):
    canvas.delete("all")
    for dot in snake:
        canvas.create_rectangle(dot[0], dot[1], dot[0] + SIZE_BLOCK, dot[1]+SIZE_BLOCK, fill = '#dad871', outline = '#dad871')
#pop element and update picture
def popAndDraw(snake):
    snake.pop()
    time.sleep(0.1)
    drawSnake(snake)
    root.update()

def move(snake, lastPressed):
    if(lastPressed == 'w'):
        snake.insert(0, [snake[0][0], snake[0][1]-SIZE_BLOCK])
        popAndDraw(snake)
    if(lastPressed == 'a'):
        snake.insert(0, [snake[0][0]-SIZE_BLOCK, snake[0][1]])
        popAndDraw(snake)
    if(lastPressed == 'd'):
        snake.insert(0, [snake[0][0]+SIZE_BLOCK, snake[0][1]])
        popAndDraw(snake)
    if(lastPressed == 's'):
        snake.insert(0, [snake[0][0], snake[0][1]+SIZE_BLOCK])
        popAndDraw(snake)

drawSnake(snake)
root.update()
while (keyboard.is_pressed('q') == False):
    move(snake, lastPressed)
    if(keyboard.is_pressed('w')&(lastPressed != 's')):
        snake.insert(0, [snake[0][0], snake[0][1]-SIZE_BLOCK])
        popAndDraw(snake)
        lastPressed = 'w'
    if(keyboard.is_pressed('a')&(lastPressed != 'd')):
        snake.insert(0, [snake[0][0]-SIZE_BLOCK, snake[0][1]])
        popAndDraw(snake)
        lastPressed = 'a'
    if(keyboard.is_pressed('d')&(lastPressed != 'a')):
        snake.insert(0, [snake[0][0]+SIZE_BLOCK, snake[0][1]])
        popAndDraw(snake)
        lastPressed = 'd'
    if(keyboard.is_pressed('s')&(lastPressed != 'w')):
        snake.insert(0, [snake[0][0], snake[0][1]+SIZE_BLOCK])
        popAndDraw(snake)
        lastPressed = 's'
root.mainloop()
