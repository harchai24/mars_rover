# Define the Command Pattern classes
class Command:
    def execute(self):
        pass

class MoveCommand(Command): # to move the rover 1 unit in diection faced
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.move()

class TurnLeftCommand(Command):# to turn the rover in left direction
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.turn_left()

class TurnRightCommand(Command):# to turn the rover in right direction
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.turn_right()

# Define the Receiver class
class Rover:
    def __init__(self, x, y, direction, grid_width, grid_height):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid_width = grid_width
        self.grid_height = grid_height

        # Define command dictionary for movement
        self.move_commands = {
            'N': lambda: (self.x, self.y + 1),
            'S': lambda: (self.x, self.y - 1),
            'E': lambda: (self.x + 1, self.y),
            'W': lambda: (self.x - 1, self.y)
        }

        # Define command dictionary for turning left
        self.left_commands = {
            'N': 'W',
            'S': 'E',
            'E': 'N',
            'W': 'S'
        }

        # Define command dictionary for turning right
        self.right_commands = {
            'N': 'E',
            'S': 'W',
            'E': 'S',
            'W': 'N'
        }

        self.obstacles = set()

    def move(self):# moving the rover
        new_x, new_y = self.move_commands[self.direction]()
        if self.is_valid_move(new_x, new_y):
            self.x, self.y = new_x, new_y
            if (self.x, self.y) in self.obstacles:
                self.x, self.y = new_x, new_y

    def turn_left(self):
        self.direction = self.left_commands[self.direction]

    def turn_right(self):
        self.direction = self.right_commands[self.direction]

    def is_valid_move(self, x, y):
        return 0 <= x < self.grid_width and 0 <= y < self.grid_height

    def set_obstacles(self, obstacles):
        self.obstacles = set(obstacles)

    def get_status_report(self):
        obstacle_status = "No obstacles detected."
        if (self.x, self.y) in self.obstacles:
            obstacle_status = "Obstacle detected at ({}, {}).".format(self.x, self.y)
        return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. {obstacle_status}"

# Define the CommandInvoker class
class Controller:
    def __init__(self):
        self.command_history = []

    def execute(self, command):
        command.execute()
        self.command_history.append(command)

# Define the Composite Pattern classes for the grid and obstacles
class GridComponent:
    def is_obstacle(self):
        return False

class Obstacle(GridComponent):
    def is_obstacle(self):
        return True

class Grid(GridComponent):
    def __init__(self, width, height):
        self.grid_width = width
        self.grid_height = height

# Get user input
grid_width, grid_height = map(int, input("Enter Grid Size (width x height): ").split())
start_x, start_y, start_direction = map(str, input("Enter Starting Position (x y direction): ").split())
commands = input("Enter Commands (e.g., 'MMLRM'): ")
obstacle_count = int(input("Enter the number of obstacles: "))

obstacles = []
for _ in range(obstacle_count):
    obstacle_x, obstacle_y = map(int, input("Enter Obstacle Position (x y): ").split())
    obstacles.append((obstacle_x, obstacle_y))

# Example usage with user input
mars_grid = Grid(grid_width, grid_height)

mars_rover = Rover(int(start_x), int(start_y), start_direction, grid_width, grid_height)
mars_rover.set_obstacles(obstacles)
controller = Controller()

for command_char in commands:
    if command_char == 'M':
        controller.execute(MoveCommand(mars_rover))
    elif command_char == 'L':
        controller.execute(TurnLeftCommand(mars_rover))
    elif command_char == 'R':
        controller.execute(TurnRightCommand(mars_rover))

status_report = mars_rover.get_status_report()
print(f"Final Position: ({mars_rover.x}, {mars_rover.y}, {mars_rover.direction})")
print(f"Status Report: {status_report}")
