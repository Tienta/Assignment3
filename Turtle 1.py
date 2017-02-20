from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range (3, 8):
    for j in range (i):
        color(colors[i-3])
        fd(100)
        lt(360/i)
        
