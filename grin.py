from scene import *
import sound
import math as ma
#from GG_Levels import levels, colors
import photos

A = Action

###Player Attributes
class Player(object):#(self, stamina, position, can_move, SpriteNode):
	def __init__(self, stamina, position, can_move):
		self.stamina = stamina
		self.position = position
		self.can_move = can_move

				
class enemy(object):
	def __init__(self,stamina,position,can_move):			
		self.stamina = stamina
		self.position = position
		self.can_move = can_move

class Block(SpriteNode):
	def __init__(self,block_type, *args, **kwargs):
		img = colors.get(block_type,'pzl:Blue3')
		SpriteNode.__init__(self,img,*args,**kwargs)
		self.block_type = block_type
						
def Magnitude(point1,point2):
	a, b = point1
	x, y = point2
	
	d = ma.sqrt((x-a)**2+(y-b)**2)	
	
	return d
	
def New_Angle(position,target):
	x,y = target
	a,b = position							
	if x - a == 0:
		theta = ma.pi/2
	else:
		v = (y-b)/(x-a)
		theta = abs(ma.atan(v))

	if x-a > 0 and y-b > 0:
		newtheta = theta
	elif x-a < 0 and y-b > 0:
		newtheta = ma.pi - theta
	elif y-b < 0 and x-a > 0:
		newtheta = 2*ma.pi - theta
	elif x-a < 0 and y-b < 0:
		newtheta = ma.pi + theta
	return newtheta

###New position 0.2 - Moves to target if below maxdistance else move towards target at maxdistance 
def New_position(position,target,maxdistance): 
					a, b = position
					x, y = target
					d = Magnitude(position,target)	
					
					if d < maxdistance:
						newx, newy = x, y
					else:
						theta = New_Angle(position,target)
						newx = a + maxdistance*ma.cos(theta)
						newy = b + maxdistance*ma.sin(theta)
									
					return newx, newy
### *** /// Character Creation - Players					
	
#####___GRiM - initial stamina, position and can move
GRiM_STaMina = 100
GriM_position = (256,120)
GRim_can_move = True
grim = Player(GRiM_STaMina,GriM_position,GRim_can_move)
							

#####___GRiN 
GRin_StaMina = 100
GRIN_positiON = (140,568)
GRIn_can_move = False
grin = Player(GRin_StaMina,GRIN_positiON,GRIn_can_move)

#######---enemies

#######Projectiles
class bullet(object):
	def __init__(self,position,type,rotation):
		self.position = position
		self.speed = 2000
		self.type = type
	
##%%## -GG1 -Grin n Grim Test Room ***
class GG1(Scene):
		
	###SetUp Conditions 
	def setup(self):
		self.level = 0
	###grim start
		
		self.grim = SpriteNode('plc:Character_Pink_Girl')
		self.grim.stamina = grim.stamina
		self.grim.position = grim.position
		self.grim.can_move = grim.can_move
	
		
		
		###grin start
		self.grin = SpriteNode('spc:CockpitGreen1')
		self.grin.stamina = grin.stamina
		self.grin.position = grin.position
		self.grin.can_move = grin.can_move
		
		###Loads Player and Object Sprites
		self.cursor = SpriteNode('iob:arrow_down_c_32')
	
		self.grim.anchor_point = (0.5,0.5)
		
		self.grin.anchor_point = (0.5,0.5)
		self.ripple = SpriteNode('shp:wavering')
		self.button = SpriteNode('plc:Selector')
		self.button.on = True
		self.bullet = SpriteNode('spc:LaserBlue13')
		self.bullet.scale = 0.5
		self.bullet.speed = 50
		self.bullets = []
		self.blocks = []
		self.block = SpriteNode('pzl:Gray4')
		self.effect_node = EffectNode(parent=self)
		self.effect_node.crop_rect = self.bounds
		self.effect_node.effects_enabled = False
		self.game_node = Node(parent=self.effect_node)
		self.expl = SpriteNode('shp:Explosion03')
		self.expl.scale = 0.25
		
		
		###Sends to Menu
		self.grim.can_move = True
		self.grin.can_move = False
		self.Menu()

		

	
	def update(self):
		
		pos = self.bullet.position
#		
		
		self.bullet.position = pos
		pos = self.bullet.position
		theta = self.bullet.rotation

		pos += (ma.cos(theta)*self.bullet.speed, ma.sin(theta)*self.bullet.speed)
		
	# Don't allow the ship to move beyond the screen bounds:
		if pos.x > self.size.w or pos.x < 0:
			self.bullet.remove_from_parent()
		elif pos.y > self.size.h or pos.y < 0:
			self.bullet.remove_from_parent()		
			
		if self.grim.can_move == False:
			if self.grin.bbox.contains_point(pos):
				theta = self.bullet.rotation
				self.bullet.remove_from_parent()
				self.grin.stamina += - 10
				sound.play_effect('digital:Laser3')
				self.expl.position = pos
				self.add_child(self.expl)
				self.Grin_Turn(grin)
				self.grin.position += 4*ma.cos(theta),4*ma.sin(theta)
				if self.grin.stamina == 0:
					self.grin.remove_from_parent()
					sound.play_effect('arcade:Explosion_2')					
					self.grin.position = self.size/2
					self.grin.stamina = 100
					self.add_child(self.grin)						
					sound.play_effect('arcade:Powerup_1')
						
		#update_grim(self,grim)

# 	def update_grin(self,grin):
		if self.grin.can_move == False:
			if self.grim.bbox.contains_point(pos):
				theta = self.bullet.rotation
				self.bullet.remove_from_parent()
				self.grim.stamina += - 10	
				sound.play_effect('digital:Laser3')
				self.expl.position = pos
				self.add_child(self.expl)
				self.Grim_Turn(grim)
				self.grim.position += 4*ma.cos(theta),4*ma.sin(theta)
				if self.grim.stamina == 0:
					self.grim.remove_from_parent()
					sound.play_effect('arcade:Explosion_2')									
					self.grim.position = self.size/2
					self.grim.stamina = 100
					self.add_child(self.grim)
					sound.play_effect('arcade:Powerup_2')
		#update_grin(self.grin)
					
		self.bullet.position = pos
		

			
	###Menu Screen
	def Menu(self):
		self.gamesetting = 'Menu'
		
		#Menu Screen Contents		
		self.background_color = 'green'	
		self.startbutton = SpriteNode('iob:arrow_right_b_256')
		self.startbutton.position = self.size/2
		self.add_child(self.startbutton)
		
		
	###TOUCH_START	
	def touch_began(self,touch):
		self.expl.remove_from_parent()
		self.cursor.position = touch.location
		self.add_child(self.cursor)
		
		###Removes Placeholder
		self.ripple.remove_from_parent()		
				
		###Menu Setting
		if self.gamesetting == 'Menu':
			self.gamesetting = 'Play'
			self.startbutton.remove_from_parent()
			sound.play_effect('game:Ding_1')
			self.GameStart()
			
		###Play Setting
		elif self.gamesetting == 'Play':
			
				###Grins Turn			
				if self.grin.can_move == True: 
					
					#%#Movement using New_Position 0.1
					newx, newy = New_position(self.grin.position,touch.location,self.grin.stamina+ 100)
					move_action = Action.move_to(newx,newy,1.2, TIMING_LINEAR)
					self.grin.run_action(move_action)
					grim.position = self.grim.position
					
					#%#Sound fx and end turn
					sound.play_effect('game:Spaceship')
						
					self.Grim_Turn(grim)
					
				###Grims Turn
				elif self.grim.can_move == True:
										
					#%#Movement using New_position
					newx, newy = New_position(self.grim.position,touch.location,self.grim.stamina+100)
					move_action = Action.move_to(newx,newy,1.2, TIMING_LINEAR)
					self.grim.run_action(move_action)
					self.grim.position = newx, newy
					
					###ButtonPressed
					if Magnitude(self.grim.position,self.button.position)<30:
						self.Button_Press(self.button)
					
					#%#Sound fx and end turn
					sound.play_effect('game:Spaceship')
			#		self.grim.can_move = False
					self.Grin_Turn(grin)
						
	###TOUCH_WHILE									
	def touch_moved(self, touch):
		self.cursor.position = touch.location
		if self.grim.can_move == False:
			theta = New_Angle(self.grim.position,touch.location)			
			self.grim.rotation = ma.pi/2+theta
			
		if self.grin.can_move == False:
			theta = New_Angle(self.grin.position,touch.location)
			self.grin.rotation =ma.pi/2+ theta

	###TOUCH_ENDED
	def touch_ended(self,touch):
		self.cursor.remove_from_parent()
		###Interactive_Cursor
		self.target = touch.location
		self.ripple.position = self.target
		self.add_child(self.ripple)
		
		if self.grim.can_move == False:
			theta = New_Angle(self.grim.position,touch.location)
			self.bullet.position = self.grim.position
			self.bullet.rotation = theta
			self.add_child(self.bullet)
			sound.play_effect('arcade:Laser_1')
						
		elif self.grin.can_move == False:
			theta = New_Angle(self.grin.position,touch.location)
			self.bullet.position = self.grin.position
			self.bullet.rotation = theta 
			self.add_child(self.bullet)
			sound.play_effect('arcade:Laser_1')
					
	###Start	
	def GameStart(self):		
	
		###Background
		self.background_color = 'blue'
		
		self.add_child(self.grim)
		self.add_child(self.grin)
		
		###Buttons And Switches
		self.button.position = self.size/2
		self.add_child(self.button)
		
		#lines = level_str.splitlines()
		
		level1 = (	('''aaaaaaaaaaaa'''),
				('''aaaaa    aaa'''), 
				('''aaaaaa  aaaa'''),
				('''a aaa      a'''),
				('''aaaaaaaaaaaa'''))

		block_w = self.size.w/(len(level1[1]))
		block_h = self.size.h/(len(level1))
		
		min_x = block_w/2
		min_y = block_h/2

		for y, line in enumerate(reversed(level1)):
			for x, char in enumerate(line):
				if char == ' ': continue
				pos = Point(x * block_w + min_x, min_y + y * block_h)
				block = Block(char, position=pos, parent=self.game_node)
				block.size = (block_w, block_h)
				self.blocks.append(block)
		for i, b in enumerate(self.blocks):
			b.scale = 0
			b.run_action(A.sequence(A.wait(i*0.01), A.scale_to(1, 0.25, 4)))
		
				
	###Grim Turn Start 	
	def Grim_Turn(self, grim):
		self.grim.can_move = True
		self.grin.can_move = False
		print( str('Tim') + str(self.grim.stamina))

	###Grin Turn Start
	def Grin_Turn(self,grin):
		self.grin.can_move = True		
		self.grim.can_move = False
		print(str('n00b')+str(self.grin.stamina))
	
	def Button_Press(self,button):
		
		sound.play_effect('arcade:Hit_3')
		
		if self.button.on == False:
			self.button.on = True
			self.background_color = 'orange'
			
		elif self.button.on == True:
			self.button.on = False
			self.background_color = 'purple'
								
run(GG1(), LANDSCAPE)
