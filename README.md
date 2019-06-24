# TINWIS01-7-Puck-Game
A game that features math solutions to simulate air puck.
![Screenshot of Air puck](http://puu.sh/DJiGh/20cc58f140.gif)

## Prerequisites
To use this program, clone the repository
```
https://github.com/pietjanssen/TINWIS01-7-Puck-Game.git
```
And install the modules required using:
```
pip install -r requirements.txt
```

### How to use it:
In order to run the program, you will need run main.py
```
python main.py
```

You can add an amount (default=2) using the parameter -amount
```
python main.py -amount 10
```

## How it works:
In order to move and let the pucks interact with eachother, every puck has it's own position, velocity, force, mass and Kinetic Energy.

### Position
A list consisting of an x coordinate and y coordinate. This position is always smaller than the screen size, so it fits the screen.

Example:
[960, 100]

### Velocity
```
v = m/s
```
A list consisting of a x velocity and y velocity.

Example:
[1, -1]

![Screenshot of Velocity](https://puu.sh/DJiRT/df8f5a1f9c.gif)

### Force
```
F = N
```
A starting power that accelerates the pucks by it's amount.

The user can input the following buttons to apply a force to a puck:

![Screenshot of keyup](https://d1nhio0ox7pgb.cloudfront.net/_img/v_collection_png/48x48/shadow/keyboard_key_up.png)
Apply a force up to the white puck

![Screenshot of keyleft](https://d1nhio0ox7pgb.cloudfront.net/_img/v_collection_png/48x48/shadow/keyboard_key_left.png)
Apply a force to the left to the white puck

![Screenshot of keyright](https://d1nhio0ox7pgb.cloudfront.net/_img/v_collection_png/48x48/shadow/keyboard_key_right.png)
Apply a force to the right to the white puck

![Screenshot of keydown](https://d1nhio0ox7pgb.cloudfront.net/_img/v_collection_png/48x48/shadow/keyboard_key_down.png)
Apply a force down to the white puck

![Screenshot of spacebardown](https://d1nhio0ox7pgb.cloudfront.net/_img/v_collection_png/48x48/shadow/keyboard_key_empty.png)
Apply a random force in a random direction to all pucks

### Mass
```
m = kg
```
The mass of a puck. The mass of each puck determines how "heavy" a puck is.
The heavier the puck, the more force it needs to accelerate

### Energy
```
E = J
```
The energy of a puck determines how much each puck impacts the other puck in movement.

![Screenshot of Kinetic energy](http://puu.sh/DJj5K/deb4380784.png)
*Taken from https://en.wikipedia.org/wiki/Elastic_collision
