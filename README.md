Mars Rover Problem

Problem Description
The Mars Rover problem simulates the operation of a rover on the surface of Mars. The rover is placed on a grid, and it can move forward, turn left, and turn right based on a set of commands. The problem also involves obstacle detection to ensure that the rover does not collide with any obstacles on its path.

Implementation of Mars Rover Problem
Overview
This repository provides a Python implementation of the Mars Rover problem. The problem simulates the operation of a rover on the surface of Mars, where the rover can move forward, turn left, and turn right on a grid-based terrain while avoiding obstacles.

Key Components
Command Pattern: The solution leverages the Command Pattern to encapsulate commands ('M' for move, 'L' for turn left, 'R' for turn right) as objects. This pattern enhances flexibility and extensibility by allowing easy addition of new commands.
Composite Pattern: To represent the grid-based terrain and obstacles, the solution uses the Composite Pattern. The Grid class acts as the composite, while the Obstacle class represents obstacles. This design allows for a structured representation of the grid and obstacle hierarchy.
Object-Oriented Programming (OOP): The implementation adheres to Object-Oriented Programming principles, including encapsulation, inheritance, and polymorphism. Each rover is an instance of the Rover class, which encapsulates its state and behavior.
Usage
Initialize a Rover: Initialize a rover with a starting position (x, y) and direction (N, S, E, W) on the grid.
Set Obstacles: Optionally, set obstacles on the grid using the set_obstacles method.
Execute Commands: Issue a sequence of commands ('M' for move, 'L' for turn left, 'R' for turn right) to the rover.
Status Report: Obtain a status report containing the rover's current position and facing direction. The report also indicates whether obstacles are detected in the path.

Dependencies 
Python 3.x

Contribution 
Contribution issues, and feedback are welcome. Feel free to create a pull request or open an issue if you have any suggestions or encounter any problems.
