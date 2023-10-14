Dino Run
Dino Run is a simple game where the player controls a dinosaur, guiding it to jump over obstacles and avoid collisions. The objective is to accumulate as many points as possible before the player loses.

This game was created using the Pygame Zero module.

How to Play
The game begins with a welcoming screen. To start playing, the player should press the spacebar. Once the game commences, the dinosaur automatically starts running. The player must press the spacebar to make the dinosaur jump over obstacles.

To run:
Open the runner.py file

If the player collides with an obstacle, the game ends, and the Game Over screen is displayed. To restart the game, the player should press the 'R' key.

How the Code Works
The code is divided into two main functions: draw() and update().

The draw() function is responsible for rendering the game's graphics on the screen. This function checks if the game has ended and displays the Game Over screen if so. If the game is still running, it draws the sky and ground, the current score, and the dinosaur and obstacles.

The update() function handles the game's logic. It updates the position of the dinosaur and obstacles in each frame, checks if the player has collided with an obstacle, and updates the score. It also manages player input and restarts the game if the 'R' key is pressed.

Additionally, there are some global variables that control the game's state, such as the obstacle list, the score, and the Game Over state.

In summary, Dino Run is a simple yet entertaining game that showcases some of the fundamental concepts of game programming in Python.
