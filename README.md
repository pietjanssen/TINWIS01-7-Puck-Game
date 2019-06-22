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

## How it works:
In order to move and let the pucks interact with eachother, every puck has it's own position, velocity, force, mass and Kinetic Energy.

### Position
A list consisting of an x coordinate and y coordinate. This position is always smaller than the screen size, so it fits the screen.

Example:
[960, 100]

### Velocity
A list consisting of a x velocity and y velocity.

Example:
[1, -1]

![Screenshot of Velocity](https://puu.sh/DJiRT/df8f5a1f9c.gif)

### Force
A starting power that accelerates the pucks by it's amount.

The user can input the following buttons to apply a force to a puck:

![Screenshot of keyup](https://d1nhio0ox7pgb.cloudfront.net/_img/v_collection_png/48x48/shadow/keyboard_key_up.png)
Apply a force up

![Screenshot of keyleft](https://d1nhio0ox7pgb.cloudfront.net/_img/v_collection_png/48x48/shadow/keyboard_key_left.png)
Apply a force to the left

![Screenshot of keyright](https://d1nhio0ox7pgb.cloudfront.net/_img/v_collection_png/48x48/shadow/keyboard_key_right.png)
Apply a force to the right

![Screenshot of keydown](https://d1nhio0ox7pgb.cloudfront.net/_img/v_collection_png/48x48/shadow/keyboard_key_down.png)
Apply a force down

![Screenshot of spacebardown](https://d1nhio0ox7pgb.cloudfront.net/_img/v_collection_png/48x48/shadow/keyboard_key_empty.png)
Apply a random force in a random direction to all pucks

### Mass

### Kinetic Energy
