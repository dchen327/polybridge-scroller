# Poly Bridge Scroller

## Introduction:
Poly Bridge is a bridge building simulator with many different techniques. One special technique is the "road drop"
technique, where the player places roads very high in the sky and uses these to launch vehicles to the finish line. This
program facilitates the process of placing these roads by providing easy to use functions which move the screen up or
down a specified amount. In addition, the program can search for yellow joints in a screenshot of the screen, so the
program can move up and stop when it finds already placed roads. This saves a lot of time that would normally be spent
searching for a previously placed road.

## Usage:
The program has three main functions: `move_screen_up()`, `move_screen_down()`, and `find_joints_above()`. Each one of these
functions takes in a parameter num_moves, which specifies how many times to move. These functions preserve the
horizontal location of the mouse, which makes it easier to line up road drops.

Ex) `move_screen_up(20)` -> moves the screen up 20 times

Ex) `find_joints_above(300)` -> moves screen up a maximum of 300 times, stops when it finds a yellow joint

## Demo
