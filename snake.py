import pygame
import sys  
from pygame.image import load
from pygame.draw import rect
from pygame.font import Font
from pygame.math import Vector2
from pygame import Rect
from random import randint
import cProfile


EASY = (27, 206, 25)
MED = (27, 30, 25)
HARD = (254, 6, 0)
BOUND = (0,0,155)
BOUND_TEXT = "BOUNDRIES OFF"


class SNAKE:  #creates a class called 'SNAKE'
	# @nb.jit()
	def __init__(self): 
		self.body : list = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]  ##Array of snakes body parts/segments
		self.direction : list = Vector2(0,0)  #set's direction to (0,0)
		self.new_block : bool = False #set's new_block to False
  
		#set's the different oriented images of the head and tail in variables

		self.head_up : int = load('Graphics/head_up.png').convert_alpha()
		self.head_down : int = load('Graphics/head_down.png').convert_alpha()
		self.head_right : int = load('Graphics/head_right.png').convert_alpha()
		self.head_left : int = load('Graphics/head_left.png').convert_alpha()
		
		self.tail_up : int = load('Graphics/tail_up.png').convert_alpha()
		self.tail_down : int = load('Graphics/tail_down.png').convert_alpha()
		self.tail_right : int = load('Graphics/tail_right.png').convert_alpha()
		self.tail_left : int = load('Graphics/tail_left.png').convert_alpha()

		#set's the different orientations for body as variables

		self.body_vertical : int = load('Graphics/body_vertical.png').convert_alpha()
		self.body_horizontal : int = load('Graphics/body_horizontal.png').convert_alpha()

		#set's the different corners for the body as variables 
  
		self.body_tr : int = load('Graphics/body_tr.png').convert_alpha()
		self.body_tl : int = load('Graphics/body_tl.png').convert_alpha()
		self.body_br : int = load('Graphics/body_br.png').convert_alpha()
		self.body_bl : int = load('Graphics/body_bl.png').convert_alpha()

	def draw_snake(self):
		self.update_head_graphics() #call upon the function update_head_graphics to update the heads roattion position
		self.update_tail_graphics() #call upon the function update_tail_graphics to update the tail roattion position

		for index,block in enumerate(self.body):  #for every element in self.body (snake's body) create a dictionary with all elements in array with a corresponding index]
			x_pos : int = int(block.x * cell_size) # set's the x position of the snake to the integer of the multiplication of the x value of block and the cell_size
			y_pos : int = int(block.y * cell_size) # set's the y position of the snake to the integer of the multiplication of the y value of block and the cell_size
			block_rect : list = Rect(x_pos,y_pos,cell_size,cell_size) #creats a rectangle with the parameters of the x,y values and the dimensions of each cell (block)

			if index == 0: #finds the head of the snake
				screen.blit(self.head,block_rect) # draw the head of the snake
			elif index == len(self.body) - 1: # finds the tail of the snake (the last part/segment)
				screen.blit(self.tail,block_rect) # draws the tail of the snake
			else: #for every other body part 
				previous_block : list = self.body[index + 1] - block # set's a previous block by adding to the current index in the loop and subtracting the block to get the last block
				next_block : list = self.body[index - 1] - block # set's the previous block by subtracting 1 from the current index and subracting the block
				if previous_block.x == next_block.x: # if thev x value of the previous block is equal to the x value next block 
					screen.blit(self.body_vertical,block_rect) # then the snake is moving up or down as the x value is the same so display a vertical body part/segment
				elif previous_block.y == next_block.y: #if thev y value of the previous block is equal to the y value next block 
					screen.blit(self.body_horizontal,block_rect) # then the snake is moving left or right as the y value is remaining the same so display a horizontal body part/segment
				else: #else if the snake is not moving up,down,left or right it must have turned (as the x and y values are not consistant) so display a corner / turning body part/segment
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1: # if the snake is going right and turns left/up or if the snake is going down and turns right (in proportion to snakes direction (left if looking at screen)) 
						screen.blit(self.body_tl,block_rect) #display the corner segment that relates to the turn (also refered to as a top left turn as reference in a vector dimentions graph)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1: #if the snake is going right and turns right/down or if the snake is going up and turns left 
						screen.blit(self.body_bl,block_rect) #display the corner segment that relates to the turn (also refered to as a bottom left turn as reference in a vector dimentions graph)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1: #if the snake is going in the left direction and turns right/up or if the snake is going down and turns left (in proportion to snakes direction (right if looking at screen)) 
						screen.blit(self.body_tr,block_rect) #display the corner segment that relates to the turn (also refered to as a top right turn as reference in a vector dimentions graph)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1: #if the snake is going left and turns left/down or if the snake is going up and turns right 
						screen.blit(self.body_br,block_rect) #displat the corner segment that relates to the turn (also refered to as a bottom right turn as reference in a vector dimentions graph)

	def update_head_graphics(self):
		head_relation : list = self.body[1] - self.body[0] #set the variable head_relation to the second element in the array - the first elemnt 
		if head_relation == Vector2(1,0):self.head : int = self.head_left #if head realtion is equal to vector(1,0) or moving left in accordance to typical vector dimentions hen set the head to head_left
		elif head_relation == Vector2(-1,0):self.head : int = self.head_right #if the head relation is equal to vector(-1,0) or moving right then set the head to head_right
		elif head_relation == Vector2(0,1):self.head : int = self.head_up #if the head relation is equal to vector(0,1) or moving up then set the head to head_up
		elif head_relation == Vector2(0,-1):self.head : int = self.head_down #if the head relation is equal to vector(0,1) or moving down then set the head to head_down


	def update_tail_graphics(self):
		tail_relation : list = self.body[-2] - self.body[-1] #set the variable tail_relation to the second last element in the array - the last elemnt 
		if tail_relation == Vector2(1,0):self.tail : int = self.tail_left #if the tails relation is equal to vector(1,0) or moving left in accordance to vector dimentions then set the tail to tail_left
		elif tail_relation == Vector2(-1,0):self.tail : int = self.tail_right #if the tails relation is equal to vector(-1,0) or moving right then set the tail to tail_right
		elif tail_relation == Vector2(0,1):self.tail : int = self.tail_up #if the tails relation is equal to vector(0,1) or moving up then set the tail to tail_up
		elif tail_relation == Vector2(0,-1):self.tail : int = self.tail_down #if the tails relation is equal to vector(0,1) or moving down then set the tail to tail_down
  
	def move_snake(self):
		self.body : int = [self.body[0] + self.direction] + (
            self.body[:] if self.new_block else self.body[:-1]
        )
		self.new_block : bool = False

	def add_block(self):
		self.new_block : bool = True  #if the snake gets an apple then new_block is set to True 

	def reset(self):
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]  #Array of snakes body parts
		self.direction = Vector2(0,0) #set's the direction of the snake
		self.new_block = False

class FRUIT:
	def __init__(self):
		self.snake = SNAKE()
		self.randomize() #call upon the randomise function
		
	def draw_fruit(self):
		fruit_rect : list = Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)  #apple's demensions 
		screen.blit(apple,fruit_rect) #visually inputs the apple on the sceen

	def check_apple(self,temp_food):
		if temp_food in self.snake.body: self.randomize()
		else: return temp_food
	
	def randomize(self):
		self.x : int = randint(0,cell_number - 1) #get the new x position by picking a random number between 0 and 15 (the max width)
		self.y : int = randint(0,cell_number - 1) #get the new y position by picking a random number between 0 and 15 (the max width)
		self.pos : list = Vector2(self.x,self.y) #uses vector2 to creat a 2 demensional vector using the two new positions and set's it as the new position of the apple
		self.check_apple(self.pos)
  
class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbours = []
        self.camefrom = []
        self.obstacle = False
        self.main = MAIN()
        
    def add_neighbours(self, grid): #working
        if self.x > 0:
            self.neighbours.append(grid[self.x - 1][self.y])
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y - 1])
        if self.x < cell_number - 1:
            self.neighbours.append(grid[self.x + 1][self.y])
        if self.y < cell_number - 1:
            self.neighbours.append(grid[self.x][self.y + 1])
        if bound == False:
            if self.x == 0:
                self.neighbours.append(grid[cell_number-1][self.y]) 
            if self.y == 0:
                self.neighbours.append(grid[self.x][cell_number-1])	
            if self.x == cell_number - 1:
                self.neighbours.append(grid[0][self.y])
            if self.y == cell_number - 1:
                self.neighbours.append(grid[self.x][0])
            if self.x == 0 and self.y == cell_number - 1:
                self.neighbours.append(grid[cell_number-1][self.y])
                self.neighbours.append(grid[self.x][0])
            if self.x == cell_number - 1 and self.y == cell_number - 1:
                self.neighbours.append(grid[0][self.y])
                self.neighbours.append(grid[self.x][0])
            if self.x == cell_number - 1 and self.y == 0:
                self.neighbours.append(grid[0][self.y])
                self.neighbours.append(grid[self.x][cell_number-1])	     
            if self.x == 0 and self.y == 0:
                 self.neighbours.append(grid[cell_number-1][self.y])
                 self.neighbours.append(grid[self.x][cell_number-1])	
                
		

class MAIN:
	def __init__(self):
		self.snake = SNAKE()  #set's snake to the class SNAKE
		self.fruit = FRUIT() #set's fruit to the class FRUIT
		self.machine = False
		
	def start_screen(self):
		self.begin = False
		
		screen.fill((15, 92, 0))
		title_font = Font('Font/PoetsenOne-Regular.ttf', 60) #declairs the font used in the game

		title_surface = title_font.render("WELCOME TO SNAKE!",True,(27, 30, 25))
		easy_surface = game_font.render("EASY",True,EASY)
		machine_surface = game_font.render("MACHINE LEARNING",True,(50,100,205))
		med_surface = game_font.render("MED",True,MED)
		hard_surface = game_font.render("HARD",True,HARD)
		play_surface = game_font.render("PLAY",True,(27, 30, 25))
		quit_surface = game_font.render("QUIT",True,(27, 30, 25))
		bound_surface = game_font.render(BOUND_TEXT,True,BOUND)
  
		title_x = int(cell_size * cell_number/2) 
		title_y = int(cell_size * cell_number - (cell_size * cell_number - 100)) 
		machine_x = int(cell_size * cell_number/2) 
		machine_y = int(cell_size * cell_number - (cell_size * cell_number - 200)) 
		easy_x = int(cell_size * cell_number/5)
		med_x = int((cell_size * cell_number/5)*2.5)
		hard_x = int((cell_size * cell_number/5)*4)
		second_y = int(cell_size * cell_number - (cell_size * cell_number - 300))
		play_x = int(cell_size * cell_number/3)
		quit_x = int(cell_size * cell_number/3 + cell_size * cell_number/3)
		third_y = int(cell_size * cell_number - (cell_size * cell_number - 500))
		bound_x = int(cell_size * cell_number/2)
		fourth_y = int(cell_size * cell_number - (cell_size * cell_number - 400))
  
		title_rect = title_surface.get_rect(center = (title_x,title_y))
		machine_rect = machine_surface.get_rect(center = (machine_x,machine_y))
		easy_rect = play_surface.get_rect(center = (easy_x,second_y))
		med_rect = play_surface.get_rect(center = (med_x,second_y))
		hard_rect = play_surface.get_rect(center = (hard_x,second_y))
		play_rect = play_surface.get_rect(center = (play_x,third_y))
		quit_rect = quit_surface.get_rect(center = (quit_x,third_y))
		if bound == False:
			bound_rect = quit_surface.get_rect(center = (bound_x-62,fourth_y))
		else:
			bound_rect = quit_surface.get_rect(center = (bound_x-60,fourth_y))

		screen.blit(title_surface,title_rect)
		screen.blit(machine_surface, machine_rect)
		screen.blit(easy_surface, easy_rect)
		screen.blit(med_surface, med_rect)
		screen.blit(hard_surface, hard_rect)
		screen.blit(play_surface, play_rect)
		screen.blit(quit_surface, quit_rect)
		screen.blit(bound_surface, bound_rect)

		machine_rect = machine_surface.get_rect(size =(250,50), center=(machine_x,machine_y))
		easy_rect = play_surface.get_rect(size =(100,50), center=(easy_x,second_y))
		med_rect = play_surface.get_rect(size =(100,50), center=(med_x,second_y))
		hard_rect = play_surface.get_rect(size =(100,50), center=(hard_x,second_y))
		play_rect = play_surface.get_rect(size =(100,50), center=(play_x,third_y))
		quit_rect = quit_surface.get_rect(size =(100,50), center=(quit_x,third_y))
		bound_rect = quit_surface.get_rect(size =(200,50), center=(bound_x,fourth_y))
		
		rect(screen,(27, 30, 25),machine_rect,3)
		rect(screen,(27, 30, 25),easy_rect,3)
		rect(screen,(27, 30, 25),med_rect,3)
		rect(screen,(27, 30, 25),hard_rect,3)
		rect(screen,(27, 30, 25),play_rect,3)
		rect(screen,(27, 30, 25),quit_rect,3)
		rect(screen,(27, 30, 25),bound_rect,3)
  
		
	def end_screen(self):
		screen.fill((27, 30, 25))
		title_font = Font('Font/PoetsenOne-Regular.ttf', 60)

		title_surface = title_font.render("YOU DIED!",True,(155,0,0))
		play_surface = game_font.render("PLAY",True,(155,0,0))
		quit_surface = game_font.render("QUIT",True,(155,0,0))
  
		title_x = int(cell_size * cell_number/2) 
		title_y = int(cell_size * cell_number - (cell_size * cell_number - 200)) 
		play_x = int(cell_size * cell_number/3)
		quit_x = int(cell_size * cell_number/3 + cell_size * cell_number/3)
		third_y = int(cell_size * cell_number - (cell_size * cell_number - 450))

		title_rect = title_surface.get_rect(center = (title_x,title_y))
		play_rect = play_surface.get_rect(center = (play_x,third_y))
		quit_rect = quit_surface.get_rect(center = (quit_x,third_y))
  
		screen.blit(title_surface,title_rect)
		screen.blit(play_surface, play_rect)
		screen.blit(quit_surface, quit_rect)
  
		play_rect = play_surface.get_rect(size=(100,50), center=(play_x,third_y))
		quit_rect = quit_surface.get_rect(size=(100,50), center=(quit_x,third_y))
  
		rect(screen,(155,0,0),play_rect,3)
		rect(screen,(155,0,0),quit_rect,3)


	def pause(self): 
		loop = 1
		title_font = Font('Font/PoetsenOne-Regular.ttf', 70)
  
		screen.fill((27, 30, 25))
  
		pause_surface = title_font.render('PAUSED', True, (65, 65, 255))
		play_surface = game_font.render("PLAY",True,(65, 65, 255))
		quit_surface = game_font.render("QUIT",True,(65, 65, 255))

		pause_x = int(cell_size * cell_number/2) 
		pause_y = int(cell_size * cell_number - (cell_size * cell_number - 200)) 
		play_x = int(cell_size * cell_number/3)
		quit_x = int(cell_size * cell_number/3 + cell_size * cell_number/3)
		third_y = int(cell_size * cell_number - (cell_size * cell_number - 450))

		pause_rect = pause_surface.get_rect(center = (pause_x,pause_y))
		play_rect = play_surface.get_rect(center = (play_x,third_y))
		quit_rect = quit_surface.get_rect(center = (quit_x,third_y))
  
		screen.blit(pause_surface, pause_rect)
		screen.blit(play_surface, play_rect)
		screen.blit(quit_surface, quit_rect)
  
		play_rect = play_surface.get_rect(size=(100,50), center=(play_x,third_y))
		quit_rect = quit_surface.get_rect(size=(100,50), center=(quit_x,third_y))
  
		rect(screen,(65, 65, 255),play_rect,3)
		rect(screen,(65, 65, 255),quit_rect,3)
  
		while loop:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					loop = 0
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						loop = 0
					if event.key == pygame.K_SPACE:
						loop = 0
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					if (abs(pos[0] - 214) <= 50) and (abs(pos[1] - 450) <= 25):
						loop = 0
					elif (abs(pos[0] - 426) <= 50) and (abs(pos[1] - 450) <= 25):
						pygame.quit()
						sys.exit()
					else: continue
      
			pygame.display.update()
			clock.tick(100)
   
	#The function reset_ai is used to reset the AI grid, snake, and direction.
	def reset_ai(self):
		# The AI grid is a 2D list of Spot objects with dimensions cell_number x cell_number
		self.ai_grid = [[Spot(i, j) for j in range(0, cell_number)] for i in range(0,cell_number)]
		# The initial AI snake is a list of three Spot objects, starting from (3,10), (4,10), and (5,10).
		self.ai_snake = [self.ai_grid[3][10], self.ai_grid[4][10], self.ai_grid[5][10]]
		# The initial AI direction is a Vector2 object with values (1,0).
		self.ai_direction = Vector2(1,0)
		# The current AI position is set to the last element of the AI snake.
		self.ai_current = self.ai_snake[-1]

	#The function update is used to update the AI game state.
	def update(self):
		# If the AI has died, the score is printed and the AI is reset using the reset_ai function.
		if self.died:
			print('SCORE:', len(self.snake.body) - 3)
			self.reset_ai()
		else:
			# The main snake's movement is updated.
			self.snake.move_snake() 
			# The function check_collision is called to check for any collisions.
			self.check_collision()  
			# The function check_fail is called to check if the snake has run into a wall or itself.
			self.check_fail()	
			
			# If the machine is turned on and the AI has not died, the following code runs:
			if self.machine == True and self.died == False:
				# The current food is set to a `Spot` object.
				food = self.ai_grid[self.fruit.x][self.fruit.y]
				
				[[self.ai_grid[i][j].add_neighbours(self.ai_grid) for j in range(cell_number)] for i in range(cell_number)] # For every cell in the grid Add the neighboring cells to the current cell
				# The function `getpath` is called to get the AI snake's path to the food.
				try: 
					dir_array, food = self.getpath(food, self.ai_snake)
					# The last element of the path is set as the AI direction.
					self.ai_direction = dir_array.pop(-1) 

				# If there is an exception
				except:
					# Select a random cell in the grid that is not part of the snake 
					temp = self.ai_grid[randint(2,cell_number-3)][randint(2,cell_number-3)]
					food = (temp if temp not in self.ai_snake else self.ai_grid[randint(2,cell_number-3)][randint(2,cell_number-3)])
					# Set the AI direction to be the same as the direction of the snake 
					self.ai_direction = self.snake.direction
					print('FORCED MOVEMENT')			
				food_array = [food] 
				# self.ai_current = self.ai_snake[-1]

				if self.ai_direction.y == 1:   
					self.ai_snake.append(self.ai_grid[self.ai_current.x][((self.ai_current.y + 1) if self.ai_current.y < (cell_number - 1) else 0)]) # if bound == False else self.ai_current.y + 1
					self.snake.direction = Vector2(0,1)
				if self.ai_direction.x == 1: 
					self.ai_snake.append(self.ai_grid[(((self.ai_current.x + 1) if self.ai_current.x < (cell_number - 1) else 0))][self.ai_current.y])
					self.snake.direction = Vector2(1,0)
				if self.ai_direction.y == -1: 
					self.ai_snake.append(self.ai_grid[self.ai_current.x][((self.ai_current.y - 1) if self.ai_current.y > 0 else (cell_number - 1))])
					self.snake.direction = Vector2(0,-1)
				if self.ai_direction.x == -1: 
					self.ai_snake.append(self.ai_grid[((self.ai_current.x - 1) if self.ai_current.x > 0 else (cell_number - 1))][self.ai_current.y])
					self.snake.direction = Vector2(-1,0)
				self.ai_current = self.ai_snake[-1] 
				print(int(food.x), int(self.fruit.pos.x))
				if self.ai_current == food and (int(food.x) == int(self.fruit.pos.x) and int(food.y) == int(self.fruit.pos.y)): 
					food_array.append(food)
				else:
					self.ai_snake.pop(0)
			

 
	def heuristic(self, current, food, neighbour):
		# Calculate distance from current node to food
		_abs = abs
		dx1 = current.x - food.x
		dy1 = current.y - food.y
		dx2 = self.ai_current.x - food.x
		dy2 = self.ai_current.y - food.y
		cross = _abs(dx1*dy2 - dx2*dy1)
		h = _abs(neighbour.x - food.x) + _abs(neighbour.y - food.y)
		return h + cross*0.001
  
	

	def new_food(self, blocked, closed_set, snake1, attempts):
		temp_food = self.ai_grid[randint(2,(cell_number-3))][randint(2,(cell_number-3))]
		if temp_food in blocked or temp_food in closed_set or temp_food in snake1: 
			if attempts >= 3: return self.ai_grid[randint(1,(cell_number-2))][randint(1,(cell_number-2))]
			else:
				attempts += 1
				return self.new_food(blocked, closed_set, snake1, attempts)		
		else: return temp_food
 

	def getpath(self,food1, snake1):   
		openset = [snake1[-1]]
		closedset = []
		blocked = []
		for segments in snake1:
			if segments == snake1[-1]: continue
			else: 
				[blocked.append(neighbour) for neighbour in segments.neighbours if neighbour not in snake1]
		# for i in range(0,10):
		# 	self.ai_grid[randint(0,15)][randint(0,15)].obstacle = True
	
		if food1 in blocked or food1 in closedset:
			attempts = 0
			food1 = self.new_food(blocked, closedset, snake1, attempts)
		print('============================================================')
		for y in range(cell_number):
			for x in range(cell_number):
				print(('O' if self.ai_grid[x][y] == food1 else ('8' if self.ai_grid[x][y] in self.ai_snake else (('X' if (self.ai_grid[x][y] in blocked and self.ai_grid[x][y] not in self.ai_snake) or self.ai_grid[x][y] in closedset else ' ')))), end= ("" if x < 15 else "."))
			print()
		print('============================================================')
		max_iterations = 15
		counter = 0
		while 1:
			print('couner',counter)
			if counter >= max_iterations:
				break
			current1 = min(openset, key=lambda x: x.f)   
			openset = [openset[i] for i in range(len(openset)) if not openset[i] == current1]
			closedset.append(current1)
			for neighbour in current1.neighbours:
				if neighbour not in closedset and neighbour not in self.ai_snake: #add obsticles here (numbers and other)	
					tempg = neighbour.g + 1 
					if neighbour in openset:
						if tempg < neighbour.g:
							neighbour.g = tempg
					else:
						neighbour.g = tempg
						openset.append(neighbour)
					neighbour.h = self.heuristic(current1, food1, neighbour)
					neighbour.f = neighbour.g + neighbour.h
					neighbour.camefrom = current1
				else: continue
			if current1 == food1: break
			counter += 1
		blocked = []
		return self.retrace_path(current1, food1, snake1)


	def retrace_path(self, current1, food1, snake1):
		dir_array1 = []
		while current1.camefrom: 
			current1_next = self.ai_grid[(int(current1.x + self.snake.direction.x) if 0 <= int(current1.x + self.snake.direction.x) <= cell_number - 1 else (cell_number - 1 if int(current1.x + self.snake.direction.x) == 16 else (0))) if bound == True else (int(current1.x + self.snake.direction.x) if 0 <= int(current1.x + self.snake.direction.x) <= (cell_number - 1) else (cell_number - 1 if int(current1.x + self.snake.direction.x) < 0 else (cell_number - 1)))][(int(current1.y + self.snake.direction.y) if 0 <= int(current1.y + self.snake.direction.y) <= (cell_number - 1) else ((cell_number - 1) if int(current1.y + self.snake.direction.y) == 16 else (0))) if bound == True else (int(current1.y + self.snake.direction.y) if 0 <= int(current1.y + self.snake.direction.y) <= cell_number -1 else (cell_number - 1 if int(current1.y + self.snake.direction.y) < 0 else (cell_number -1)))]
			for neighbour in current1_next.neighbours: continue
			if current1.x == current1.camefrom.x and current1.y < current1.camefrom.y:
				dir_array1.append(Vector2(0,-1) if int(self.snake.direction.y) != 1 else (self.snake.direction if (current1_next not in snake1) else (Vector2((current1_next.x - neighbour.x), (current1_next.y - neighbour.y)) if (neighbour not in snake1 for neighbour in current1_next.neighbours) else (Vector2(0, 1))))) # test
			elif current1.x == current1.camefrom.x and current1.y > current1.camefrom.y:
				dir_array1.append(Vector2(0,1) if int(self.snake.direction.y) != -1 else (self.snake.direction if (current1_next not in snake1) else (Vector2((current1_next.x - neighbour.x), (current1_next.y - neighbour.y)) if (neighbour not in snake1 for neighbour in current1_next.neighbours) else (Vector2(0, -1))))) 
			elif current1.x < current1.camefrom.x and current1.y == current1.camefrom.y: 
				dir_array1.append(Vector2(-1,0) if int(self.snake.direction.x) != 1 else (self.snake.direction if (current1_next not in snake1) else (Vector2((current1_next.x - neighbour.x), (current1_next.y - neighbour.y)) if (neighbour not in snake1 for neighbour in current1_next.neighbours) else (Vector2(1, 0))))) 
			elif current1.x > current1.camefrom.x and current1.y == current1.camefrom.y:
				dir_array1.append(Vector2(1,0) if int(self.snake.direction.x) != -1 else (self.snake.direction if (current1_next not in snake1) else (Vector2((current1_next.x - neighbour.x), (current1_next.y - neighbour.y)) if (neighbour not in snake1 for neighbour in current1_next.neighbours) else (Vector2(-1, 0))))) 
			current1 = current1.camefrom
   
		for i in range(cell_number):
			for j in range(cell_number):
				self.ai_grid[i][j].camefrom = []
				self.ai_grid[i][j].obstacle = False
				self.ai_grid[i][j].f = 0
				self.ai_grid[i][j].h = 0
				self.ai_grid[i][j].g = 0
		return dir_array1, food1
 

	def draw_elements(self):
		self.draw_grass() #draw the grass by calling upon the function
		self.fruit.draw_fruit() #call upon the function that draws the fruit
		self.snake.draw_snake() #draw the snake
		self.draw_score() #show the score


	def check_collision(self):
		if self.fruit.pos == self.snake.body[0]: #if the apples position is equal to the first element in the snakes body (the head)  
			self.fruit.randomize() #call upon the randomise function
			self.snake.add_block() #call upon the add_block fuunction

		[self.fruit.randomize() for block in self.snake.body[1:] if block == self.fruit.pos] #for blocks in elements after the first element (for every other element other than the first) (precaution if apple spawns on snakes body) if block is equal the apples position call upon the randomise function

	def check_fail(self):
		i=0
		if bound == False:
			while i < len(self.snake.body):  #while i is less than the number of elements in snake.body
				if not 0 <= self.snake.body[i].x < cell_number: #if snake.body.x is less than 0 or more than the number of cels
					if not 0 <= self.snake.body[i].x:  # if snake.body.x is less than 0 (width)
						self.snake.body[i].x = self.snake.body[i].x + cell_number  # add the max width to the snake.body.x to translate the snake to the opposit side
					if not self.snake.body[i].x < cell_number:  #is snake.body.x is more thn the number of cells(width) 
						self.snake.body[i].x = self.snake.body[i].x - cell_number #subtract the maxwidth from snake.body.x to translate the snake to the opposit side
		
				if not 0 <= self.snake.body[i].y < cell_number: #if snake.body.x is less than 0 or more than the number of cels
					if not 0 <= self.snake.body[i].y: # if snake.body.x is less than 0 (width)
						self.snake.body[i].y = self.snake.body[i].y + cell_number # add the max width to the snake.body.x to translate the snake to the opposit side
					if not self.snake.body[i].y < cell_number: #is snake.body.x is more thn the number of cells(width) 
						self.snake.body[i].y = self.snake.body[i].y - cell_number #subtract the maxwidth from snake.body.x to translate the snake to the opposit side
				i=i+1
		else: 
			if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number: self.game_over()
   			
		[self.game_over() for block in self.snake.body[1:] if self.snake.body[0] == block and len(self.snake.body) > 3] #for blocks in elements after the first element (for every other element other than the first) if the blocks position is equal to the head of the snake's position or the first element in the array end the game as the player has collided with themselves 

	
	def game_over(self):  
		self.died = True
	
	def draw_grass(self):
		grass_color = (167,209,61)  #set's the colour of the grass 
		for row in range(cell_number): #for every row in cell_number
			if row % 2 == 0:  #checks for even rows (if row is even)
				for col in range(cell_number): #for every column in cell_number
					if col % 2 == 0: #checks for even columns (if column is even)
						grass_rect = Rect(col * cell_size,row * cell_size,cell_size,cell_size) #grass demensions 
						rect(screen,grass_color,grass_rect) #draw grass
			else: #if row is not even
				for col in range(cell_number): #for every column in cell_number
					if col % 2 != 0: #if col is not even
						grass_rect = Rect(col * cell_size,row * cell_size,cell_size,cell_size) #grass demensions
						rect(screen,grass_color,grass_rect)	#draw grass		

	def draw_score(self):
		score_text = str(len(self.snake.body) - 3) #set's the score to the legth of the snakes body minus (-) the starting values (3)
		score_surface = game_font.render(score_text,True,(56,74,12)) #renders the score using the specific game font declaired in a varibale and set it to grey
		score_x = int(cell_size * cell_number - 60) #sets the x position of the score to the cell size times the amount of cells - 60px
		score_y = int(cell_size * cell_number - 40) #sets the y position of the score to the cell size times the amount of cells - 40px
		score_rect = score_surface.get_rect(center = (score_x,score_y)) # creates a rectangle using the previous x and y cordinates as the center and is used to display the score
		apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))	#creates a rectange for a apple to sit left of the score rectangle while being centered vertically
		bg_rect = Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height) #this is the rectange used to hold both the apple and the score, and changes responsive according to the size of the score rectangle
		screen.blit(score_surface,score_rect) #displays the score
		screen.blit(apple,apple_rect) #displays the apple
		rect(screen,(56,74,12),bg_rect,2) #draws the rectange with a grey colour with a width of 2px

pygame.init() #initialises all imported pygame modules
pygame.mixer.pre_init(44100,-16,2,512) #presets the default mixer init arguments

cell_size = 40 #sets the size of each cell to 40px
cell_number = 16 #sets the number of cells to 16

screen = pygame.display.set_mode((cell_number * cell_size,((cell_number * cell_size)))) #uses the cell_size and cell_number to determine the width and height of the display
clock = pygame.time.Clock() #initialises the clock as a variable
apple = pygame.image.load('Graphics/apple.png').convert_alpha() #declairs the variable apple as the image
game_font = Font('Font/PoetsenOne-Regular.ttf', 25) #declairs the font used in the game
difficulty = 130  #the difficulty of the game (the delay in screen input (lower = faster (harder)))

SCREEN_UPDATE = pygame.USEREVENT 
pygame.time.set_timer(SCREEN_UPDATE,difficulty) #updates the screen using the delay

main_game = MAIN()
fruit = FRUIT()
wr = (cell_number*cell_size)/cell_number 
hr = (cell_number*cell_size)/cell_number



main_game.begin = False
main_game.died = False
bound = False

while True:
	for event in pygame.event.get():	# for event in user input
		if event.type == pygame.QUIT:   #if the exit button is presssed then quit
			pygame.quit()
			sys.exit()
   
		if event.type == SCREEN_UPDATE and main_game.begin == True:	#if Screen_update is called upon after the delay above then update the game
			main_game.update() #cProfile.run('main_game.update()') 
			
   
		if event.type == pygame.MOUSEBUTTONUP and main_game.begin == False:
			pos = pygame.mouse.get_pos()
			print(pos)
   
			if (abs(pos[0] - 214) <= 50) and (abs(pos[1] - 500) <= 25):
				main_game.begin = True
    
			elif (abs(pos[0] - 426) <= 50) and (abs(pos[1] - 500) <= 25):
				pygame.quit()
				sys.exit()

			# elif (abs(pos[0] - 426) <= 50) and (abs(pos[1] - 500) <= 25):
			# 	pygame.quit()
			# 	sys.exit()
    
			elif (abs(pos[0] - 320) <= 125) and (abs(pos[1] - 200) <= 25):
				# difficulty = difficulty + 150
				main_game.reset_ai()
				main_game.machine = True
				main_game.begin = True
    
    
			elif (abs(pos[0] - 130) <= 50) and (abs(pos[1] - 300) <= 25):
				difficulty = 150
				EASY = (27, 30, 25)
				MED = (254, 6, 255)
				HARD = (254, 6, 0)
				SCREEN_UPDATE = pygame.USEREVENT 
				pygame.time.set_timer(SCREEN_UPDATE,difficulty) 
    
			elif (abs(pos[0] - 320) <= 50) and (abs(pos[1] - 300) <= 25):
				difficulty = 125
				EASY = (27, 206, 25)
				MED = (27, 30, 25)
				HARD = (254, 6, 0)
				SCREEN_UPDATE = pygame.USEREVENT 
				pygame.time.set_timer(SCREEN_UPDATE,difficulty) 
    
			elif (abs(pos[0] - 515) <= 50) and (abs(pos[1] - 300) <= 25):
				difficulty = 100
				EASY = (27, 206, 25)
				MED = (254, 6, 255)
				HARD = (27, 30, 25)
				SCREEN_UPDATE = pygame.USEREVENT 
				pygame.time.set_timer(SCREEN_UPDATE,difficulty) 
    
			elif (abs(pos[0] - 320) <= 100) and (abs(pos[1] - 400) <= 25):
				if bound == False:
					bound = True
					BOUND_TEXT = "BOUNDRIES ON"
					BOUND = (155,0,0)
				else:
					bound = False
					BOUND_TEXT = "BOUNDRIES OFF"
					BOUND = (0,0,155)
    
		if event.type == pygame.MOUSEBUTTONUP and main_game.died == True:
			pos = pygame.mouse.get_pos()
			if (abs(pos[0] - 214) <= 50) and (abs(pos[1] - 450) <= 25):
				main_game.snake.reset() #resets the snake 
				main_game.reset_ai()
				begin = False
				main_game.died = False
    
			elif (abs(pos[0] - 426) <= 50) and (abs(pos[1] - 450) <= 25):
				pygame.quit()
				sys.exit()
    
		if event.type == pygame.KEYDOWN: #if a key is pressed
			if event.key == pygame.K_ESCAPE and main_game.begin == True and main_game.died == False:
				main_game.pause()
			if main_game.machine == False:
				if event.key == pygame.K_UP: #if user press' the up arrow 
					if main_game.snake.direction.y != 1:	#if snake vector is not (0,1) (snake going down) then change the snakes vector to (0,-1) (moving up) (to prevent snake from killing itself with backwards movement) 
						print(" --------------------------- NEW KEY EVENT -----------------------------")
						print('previous direction: ', main_game.snake.direction)
						main_game.snake.direction = Vector2(0,-1)
						print('Action: UP /',main_game.snake.direction, ' -- Fps: ', clock, ' -- Score: ', len(main_game.snake.body) - 3, ' -- difficulty: ', difficulty, '-- direction: ', main_game.snake.direction, ' -- snake body vectors: ', str(main_game.snake.body).strip())
		
				if event.key == pygame.K_RIGHT: #if user press' the right arrow
					if main_game.snake.direction.x != -1: #if snake vector is not (-1,0) (snake going left (user's view)) then change the snakes vector to (1,0) (moving right (user's view))
						print(" --------------------------- NEW KEY EVENT -----------------------------")
						print('previous direction: ', main_game.snake.direction)
						main_game.snake.direction = Vector2(1,0)
						print('Action: RIGHT /',main_game.snake.direction, ' -- Fps: ', clock, ' -- Score: ', len(main_game.snake.body) - 3, ' -- difficulty: ', difficulty, ' -- snake body vectors: ', str(main_game.snake.body).strip())
		
				if event.key == pygame.K_DOWN: #if user press' the down arrow
					if main_game.snake.direction.y != -1: #if snake vector is not (0,-1) (snake going up) then change the snakes vector to (0,1) (moving down)
						print(" --------------------------- NEW KEY EVENT -----------------------------")
						print('previous direction: ', main_game.snake.direction)
						main_game.snake.direction = Vector2(0,1)
						print('Action: DOWN /',main_game.snake.direction, ' -- Fps: ', clock, ' -- Score: ', len(main_game.snake.body) - 3, ' -- difficulty: ', difficulty, ' -- snake body vectors: ', str(main_game.snake.body).strip())
		
				if event.key == pygame.K_LEFT: #if user press' the left arrow
					if main_game.snake.direction.x != 1: #if snake vector is not (1,0) (snake going right (user's view)) then change the snakes vector to (-1,0) (moving left (user's view))
						print(" --------------------------- NEW KEY EVENT -----------------------------")
						print('previous direction: ', main_game.snake.direction)
						main_game.snake.direction = Vector2(-1,0)
						print('Action: LEFT /',main_game.snake.direction, ' -- Fps: ', clock, ' -- Score: ', len(main_game.snake.body) - 3, ' -- difficulty: ', difficulty, ' -- snake body vectors: ', str(main_game.snake.body).strip())
				for key, direction in (pygame.K_UP, Vector2(0,-1)), (pygame.K_RIGHT, Vector2(1,0)), (pygame.K_DOWN, Vector2(0,1)), (pygame.K_LEFT, Vector2(-1,0)):
					if event.key == key and main_game.snake.direction != -direction:
						main_game.snake.direction = direction
			if event.key == pygame.K_m:
				main_game.ai_grid = [[Spot(i, j) for j in range(0, cell_number)] for i in range(0,cell_number)]
				main_game.ai_snake = [main_game.ai_grid[int(i.x)][int(i.y)] for i in main_game.snake.body]
				for i, j in zip(main_game.ai_snake, main_game.snake.body):
					print(i.x,i.y, '--', j.x, j.y)
				print(len(main_game.snake.body))
				# The initial AI direction is a Vector2 object with values (1,0).
				main_game.ai_direction = main_game.snake.direction
				# The current AI position is set to the last element of the AI snake.
				main_game.ai_current = main_game.ai_snake[-1]
				main_game.machine = (True if main_game.machine == False else False)
				
			else: pass
	screen.fill((175,215,70)) #fill the screen with a light green colour that if different to the one used for the grass
	if main_game.died == False:
		if main_game.begin == True:
			main_game.draw_elements() #draw elements
		else:
			main_game.start_screen() 
	else:
		main_game.end_screen()
	pygame.display.update() #update display
	clock.tick(60)