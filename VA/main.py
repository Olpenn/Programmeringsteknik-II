import tkinter as tk
import numpy as np
import copy
import random

dt = 16 # timestep in ms
HEIGHT = 500
WIDTH = 800

def rand_color():
    colors = ["green", "black", "brown"]
    return random.choice(colors)

class BallPit:
    def __init__(self, canvas):
        self.following = True
        self.is_a_frozen_ball = False
        self.is_a_floating_ball = False
        self.g = 1000
        self.ball_array = []
        self.N_balls = 0
        self.ball_bounce_coeff = 1.
        self.wall_bounce_coeff = 0.95
        self.canvas = canvas
        self.mouse_pos = np.array([WIDTH//2, HEIGHT//2])
    
    def add_ball_on_mouse(self):
        if not self.is_a_frozen_ball and not self.is_a_floating_ball:
            self.is_a_floating_ball = True
            self.ball_array.append(Ball(self.canvas, -100., -100.))


    def stick_ball(self):
        if self.is_a_floating_ball:
            self.is_a_floating_ball = False
            self.is_a_frozen_ball = True
            mouse_pos_snapshot = copy.copy(self.mouse_pos)
            self.ball_array[-1].move_to(np.array(mouse_pos_snapshot))
            self.ball_array[-1].frozen = True
            self.ball_array[-1].floating = False
            self.canvas.itemconfig(self.ball_array[-1].object, fill=rand_color())


    def shoot_ball(self):
        if self.is_a_frozen_ball:
            self.is_a_frozen_ball = False
            self.ball_array[-1].remove_speed_dash()
            self.ball_array[-1].vel = -(self.mouse_pos - self.ball_array[-1].pos)*5
            self.ball_array[-1].frozen = False


    def track_mouse(self, event):
        self.mouse_pos[0], self.mouse_pos[1] = event.x, event.y


class Ball:
    def __init__(self, canvas, x, y):
        self.N_dashes = 10
        self.dash_rad = 5
        self.pos = np.array([x,y])
        self.r = 30
        self.m = self.r ** 2
        self.vel = np.array([0.,0.])
        self.frozen = False  # A frozen ball doesn't feel gravity
        self.floating = True
        self.canvas = canvas
        self.object = self.canvas.create_oval(self.pos[0]-self.r, self.pos[1]-self.r, self.pos[0]+self.r, self.pos[1]+self.r, 
                                              fill="gray", outline="black")
        
        self.speed_dashes = [self.canvas.create_oval(-2*self.dash_rad, -2*self.dash_rad, -self.dash_rad, -self.dash_rad, fill="black") for _ in range(self.N_dashes)]


    def move_to(self, pos):
        self.canvas.coords(self.object, pos[0]-self.r, pos[1]-self.r, pos[0]+self.r, pos[1]+self.r)
        self.pos = pos

    def draw_speed_dash(self, mouse_pos):
        edge_pos = self.pos + (mouse_pos - self.pos)/np.linalg.norm(mouse_pos - self.pos)*self.r
        if np.isnan(edge_pos).any(): edge_pos = self.pos
        for i in range(self.N_dashes):
            coords = edge_pos + (mouse_pos - edge_pos)*(i+1)/self.N_dashes
            self.canvas.coords(self.speed_dashes[i], coords[0]-self.dash_rad, coords[1]- self.dash_rad, coords[0]+self.dash_rad, coords[1]+self.dash_rad)

    def remove_speed_dash(self):
        for i in range(self.N_dashes):
            self.canvas.coords(self.speed_dashes[i], -100., -100., -100, -100.)

root = tk.Tk()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

ballpit = BallPit(canvas)
root.bind("<n>", lambda event: ballpit.add_ball_on_mouse())
root.bind("<Motion>", ballpit.track_mouse)
root.bind("<Button-1>", lambda event: ballpit.stick_ball())
root.bind("<ButtonRelease-1>", lambda event: ballpit.shoot_ball())


def update():
    # Calculate the movement due to gravity
    for ball in ballpit.ball_array:
        # Calculate the preliminary velocity and position
        ball.newvel = ball.vel + np.array([0, ballpit.g]) * dt/1000
        ball.newpos = ball.pos + ball.vel * dt/1000

        # If the preliminary position will hit the wall or floor, the preliminary velocity is inverted in that direction
        if ball.newpos[1] > HEIGHT - ball.r:
            ball.newvel[1] = -1*ballpit.wall_bounce_coeff*ball.newvel[1]
            ball.newpos = ball.pos + ball.newvel * dt/1000
        if ball.newpos[0] > WIDTH - ball.r:
            ball.newvel[0] = -1*ballpit.wall_bounce_coeff*ball.newvel[0]
            ball.newpos = ball.pos + ball.newvel * dt/1000
        if ball.newpos[0] < ball.r:
            ball.newvel[0] = -1*ballpit.wall_bounce_coeff*ball.newvel[0]
            ball.newpos = ball.pos + ball.newvel * dt/1000

    # When the wallcollision detection is passed. Move to new position and change velocity
    for ball in ballpit.ball_array:
        if ball.floating:
            ball.move_to(ballpit.mouse_pos)
        elif ball.frozen: 
            ball.move_to(ball.pos)
        else:
            ball.vel = ball.newvel
            ball.move_to(ball.newpos)


    # Calculate if the balls collide with each other, if so: modify the preliminary velocity
    for ball1 in ballpit.ball_array:
        for ball2 in ballpit.ball_array:
            if ball1 == ball2: continue
            if ball1.floating or ball2.floating: continue
            if ball1.frozen:
                if np.linalg.norm(ball1.pos - ball2.pos) <= ball1.r + ball2.r: # Collision detected
                    vel2_magnitude_after = ball2.vel * ballpit.ball_bounce_coeff
                    vel2_after = np.linalg.norm(vel2_magnitude_after) * (ball2.pos - ball1.pos) / np.linalg.norm(ball2.pos - ball1.pos)
                    ball2.newvel = vel2_after
                    ball2.newpos = ball2.pos + ball2.newvel * dt/1000
                    print(ball2.vel, ball2.newvel)
            if ball2.frozen:
                if np.linalg.norm(ball1.pos - ball2.pos) <= ball1.r + ball2.r: # Collision detected
                    vel1_magnitude_after = ball1.vel * ballpit.ball_bounce_coeff
                    vel1_after = np.linalg.norm(vel1_magnitude_after) * (ball1.pos - ball2.pos) / np.linalg.norm(ball1.pos - ball2.pos)
                    ball1.newvel = vel1_after
                    ball1.newpos = ball1.pos + ball1.newvel * dt/1000
            else:
                if np.linalg.norm(ball1.pos - ball2.pos) <= ball1.r + ball2.r: # Collision detected
                    vel1_magnitude_after = (ball1.m * ball1.vel + ball2.m * ball2.vel - ball2.m * ballpit.ball_bounce_coeff * (ball1.vel - ball2.vel))/(ball1.m + ball2.m)
                    vel2_magnitude_after = (ball1.m * ball1.vel + ball2.m * ball2.vel + ball1.m * ballpit.ball_bounce_coeff * (ball1.vel - ball2.vel))/(ball1.m + ball2.m)
                    vel1_after = np.linalg.norm(vel1_magnitude_after) * (ball1.pos - ball2.pos) / np.linalg.norm(ball1.pos - ball2.pos)
                    vel2_after = np.linalg.norm(vel2_magnitude_after) * (ball2.pos - ball1.pos) / np.linalg.norm(ball2.pos - ball1.pos)
                    ball1.newvel = vel1_after
                    ball1.newpos = ball1.pos + ball1.newvel * dt/1000
                    ball2.newvel = vel2_after
                    ball2.newpos = ball2.pos + ball2.newvel * dt/1000

    # When the collision detection is passed. Move to new position and change velocity
    for ball in ballpit.ball_array:
        if ball.floating:
            ball.move_to(ballpit.mouse_pos)
        elif ball.frozen: 
            ball.move_to(ball.pos)
            ball.draw_speed_dash(ballpit.mouse_pos)
        else:
            ball.vel = ball.newvel
            ball.move_to(ball.newpos)

    root.after(dt, update)


update()
root.mainloop()