import numpy as np
class Node:
	def __init__(self, value, location):
		self.location = location
		self.visited = 0

	def set_neighbors(self, value):
		v = value
		self.neighbors = [0, 0, 0, 0] #left, bottom, right, top
		for i in range(3, -1, -1):
			temp = v%2**i
			if temp < v:
				self.neighbors[i] = 1
			v = temp
			

	def get_neighbors(self):
		return self.neighbors

	def mark_visited(self):
		self.visited += 1

	def is_visited(self):
		return self.visited
	
class Robot(object):
    def __init__(self, maze_dim):
        '''
        Use the initialization function to set up attributes that your robot
        will use to learn and navigate the maze. Some initial attributes are
        provided based on common information, including the size of the maze
        the robot is placed in.
        '''

        self.location = [0, 0]
        self.heading = 'up'
        self.maze_dim = maze_dim
	self.maze = {}
	
    def next_move(self, sensors):
        '''
        Use this function to determine the next move the robot should make,
        based on the input from the sensors after its previous move. Sensor
        inputs are a list of three distances from the robot's left, front, and
        right-facing sensors, in that order.

        Outputs should be a tuple of two values. The first value indicates
        robot rotation (if any), as a number: 0 for no rotation, +90 for a
        90-degree rotation clockwise, and -90 for a 90-degree rotation
        counterclockwise. Other values will result in no rotation. The second
        value indicates robot movement, and the robot will attempt to move the
        number of indicated squares: a positive number indicates forwards
        movement, while a negative number indicates backwards movement. The
        robot may move a maximum of three units per turn. Any excess movement
        is ignored.

        If the robot wants to end a run (e.g. during the first training run in
        the maze) then returing the tuple ('Reset', 'Reset') will indicate to
        the tester to end the run and return the robot to the start.
        '''
	left = sensors[0]
	front = sensors[1]
	right = sensors[2]

	if left > 0:
		rotation = -90
		movement = 1
	elif front > 0:
		rotation = 0
		movement = 1
	elif right > 0:
		rotation = 90
		movement = 1
	else:
		rotation = 0
		movement = -1
	
	if self.heading == 'up':
		if rotation == 90 and movement >= 0:
			h = 'right'
		elif rotation == -90 and movement >= 0:
			h = 'left'
		elif movement >= 0:
			h = 'up'
		elif movement < 0:
			h = 'down'
	elif self.heading == 'down':
		if rotation == 90 and movement >= 0:
			h = 'left'
		elif rotation == -90 and movement >= 0:
			h = 'right'
		elif movement >= 0:
			h = 'down'
		elif movement < 0:
			h = 'up'
	elif self.heading == 'left':
		if rotation == 90 and movement >= 0:
			h = 'up'
		elif rotation == -90 and movement >= 0:
			h = 'down'
		elif movement >= 0:
			h = 'left'
		elif movement < 0:
			h = 'right'
	elif self.heading == 'right':
		if rotation == 90 and movement >= 0:
			h = 'down'
		elif rotation == -90 and movement >= 0:
			h = 'up'
		elif movement >= 0:
			h = 'right'
		elif movement < 0:
			h = 'left'
        self.heading = h

	return rotation, movement
