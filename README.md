# Python Pong Game 🏓🎮

Welcome to the Python Pong Game, a classic game built using the Turtle module.

## Project Structure

The Python Pong Game consists of several key components:

### 1. **ball.py**

This module defines the `Ball` class, responsible for controlling the game's ball. It includes methods such as:

- `move`: Controls the ball's movement.
- `bounce_y`: Changes the ball's direction when it hits the upper or lower wall.
- `bounce_x`: Changes the ball's direction when it hits the right or left paddle.
- `reset_right`: Resets the ball's position and direction of movement when the right paddle misses the ball.
- `reset_left`: Resets the ball's position and direction of movement when the left paddle misses the ball.

### 2. **paddle.py**

The `Paddle` class is defined in this module, which manages the paddles' behavior. It includes methods like:

- `up`: Moves the paddle up.
- `down`: Moves the paddle down.

### 3. **scoreboard.py**

The `Scoreboard` class, defined in this module, is responsible for tracking and displaying the players' scores. It includes methods like:

- `l_point`: Increases, updates, and displays the score for the left paddle.
- `r_point`: Increases, updates, and displays the score for the right paddle.

### 4. **main.py**

This is the main program file where the game's logic comes together. It imports the required modules, creates the game screen, paddle objects, ball object, and scoreboard object. The main program starts the ball's movement and monitors ball collisions with walls and paddles. It increases the score based on the players' behavior during the game.

## How to Play

- Use the 'W' and 'S' keys to control the left paddle, moving it up and down.
- Use the 'Up' and 'Down' arrow keys to control the right paddle.
- The objective is to prevent the ball from passing your paddle while trying to get it past your opponent's paddle.
- Each time the ball passes a paddle, the opposing player scores a point.
- The game continues until one player reaches a predefined score limit, which you can adjust as desired.

## Purpose

**Learning Python**: object-oriented programming (OOP) with Turtle, and basic game development.

Have a great time playing Python Pong Game!
