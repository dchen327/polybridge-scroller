# Poly Bridge Scroller
![polybridge](https://user-images.githubusercontent.com/37674516/79485082-a83b0c80-7fe2-11ea-99a8-02f1aeb5715d.jpeg)

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

## Demo:
![PB_scrolling_demo](https://user-images.githubusercontent.com/37674516/79485680-a160c980-7fe3-11ea-9af6-a33d1f196eb7.gif)

## Success:
![PB_road_drop_demo](https://user-images.githubusercontent.com/37674516/79485985-0b796e80-7fe4-11ea-9442-70276e90d08c.gif)

