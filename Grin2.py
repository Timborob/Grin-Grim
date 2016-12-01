from scene import *
import sound
import math as ma

from classes.player import Player
from classes.block import Block
from classes.bullet import bullet

import util.gg_math

from GG_Levels import levels, colors

A = Action

#####___GRiM - initial stamina, position and can move
GRiM_STaMina = 100
GriM_position = (256,120)
GRim_can_move = True
grim = Player(GRiM_STaMina, GriM_position, GRim_can_move, SpriteNode('spc:CockpitRed1'))							

#####___GRiN 
GRin_StaMina = 100
GRIN_positiON = (140,568)
GRIn_can_move = False
grin = Player(GRin_StaMina, GRIN_positiON, GRIn_can_move, SpriteNode('spc:CockpitGreen1') )



##%%## -GG1 -Grin n Grim Test Room ***
class GG1(Scene):
		
	###SetUp Conditions 
	def setup(self):
	
		_S = self
		
		self.level = 0
		
		###Loads Player and Object Sprites
		self.cursor = SpriteNode('iob:arrow_down_c_32')
		self.ripple = SpriteNode('shp:wavering')
		
		self.button = SpriteNode('plc:Selector')
		self.button.on = True
		
		self.bullet = SpriteNode('spc:LaserBlue13')
		self.bullet.scale = 0.5
		self.bullet.speed = 50
		
		self.blocks = []
		
		self.block = Block in enumerate(self.blocks)
		
		self.effect_node = EffectNode(parent=self)
		self.effect_node.crop_rect = self.bounds
		self.effect_node.effects_enabled = False
		
		self.game_node = Node(parent=self.effect_node)
		self.expl = SpriteNode('shp:Explosion03')
		self.expl.scale = 0.25
		
		
		###Sends to Menu
		grim.can_move = True
		grin.can_move = False
		
		self.Menu()
	
	def update(self)
		
		for k,player in Players:
			player:Update()
			
		for k,bullet in Bullets:
			player:Update()
			
				
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
			
			ply = self.GetActivePlayer()
			ply:MoveBegin( touch )
			
	###TOUCH_WHILE									
	def touch_moved(self, touch):
		self.cursor.position = touch.location
		ply = self.GetActivePlayer()
		ply:MoveWhile( touch )

	###TOUCH_ENDED
	def touch_ended(self,touch):
		self.cursor.remove_from_parent()
		###Interactive_Cursor
		self.target = touch.location
		self.ripple.position = self.target
		self.add_child(self.ripple)
		
		ply = self.GetActivePlayer()
		ply:MoveEnded( touch )
					
	###Start	
	def GameStart(self):		
	
		###Background
		self.background_color = 'blue'
		
		self.add_child( grim.spirit_node )
		self.add_child( grin.spirit_node )
		
		###Buttons And Switches
		self.button.position = self.size/2
		self.add_child(self.button)
		

		level1 = ( ('''aaaaaaaa    '''),
		('''a     aaa     '''), 
		('''a.        aaaa'''),
		('''a aaaaa       a'''),
		('''aaaaaaaaaaaaa a'''))

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
			
			
	def GetActivePlayer()
		return self.ActivePlayer
		
	def SetActivePlayer( ply )
		self.ActivePlayer = ply

run(GG1(), LANDSCAPE)
