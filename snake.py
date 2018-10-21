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
snake = [[300,300], [320, 300], [340, 300], [360, 300], [380, 300]]
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
    if(lastPressed == 'a'):
        snake.insert(0, [snake[0][0]-SIZE_BLOCK, snake[0][1]])
        popAndDraw(snake, x, y)
    if(lastPressed == 'd'):
        snake.insert(0, [snake[0][0]+SIZE_BLOCK, snake[0][1]])
        popAndDraw(snake, x, y)
    if(lastPressed == 's'):
        snake.insert(0, [snake[0][0], snake[0][1]+SIZE_BLOCK])
        popAndDraw(snake, x, y)
#coord of apple
x = randrange(0, 580, 20)
y = randrange(0, 580, 20)
draw(snake, x, y)
root.update()
while (keyboard.is_pressed('q') == False):
    if(keyboard.is_pressed('w')&(lastPressed != 's')):
        lastPressed = 'w'
    if(keyboard.is_pressed('a')&(lastPressed != 'd')):
        lastPressed = 'a'
    if(keyboard.is_pressed('d')&(lastPressed != 'a')):
        lastPressed = 'd'
    if(keyboard.is_pressed('s')&(lastPressed != 'w')):
        lastPressed = 's'
    move(snake, lastPressed, x, y)
    if(snake[0]==[x,y]):
        x = randrange(0, 580, 20)
        y = randrange(0, 580, 20)

root.mainloop()

def insertDot(snake, ud, rl):
    snake.insert(0, [snake[0][0]+ud, snake[0][1]+rl])
