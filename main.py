from classes import *

score = Score(canvas, 'green')
paddle = Paddle(canvas, 'orange')
ball = Ball(canvas, paddle, score, 'red')


while not ball.hit_bottom:
    if paddle.started:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

time.sleep(3)

