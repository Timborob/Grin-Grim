from scene import *
import sound
import math as ma

from classes.player import Player
from classes.block import Block
from classes.bullet import bullet


import util.gg_math

from GG_Levels import *

A = Action

#####___GRiM - initial stamina, position and can move
GRiM_STaMina = 100
GriM_position = (256,120)
grim = Player(GRiM_STaMina, GriM_position,True,'spc:CockpitRed1')					

#####___GRiN 
GRin_StaMina = 100
GRIN_positiON = (140,568)
grin = Player(GRin_StaMina, GRIN_positiON,False,'spc:CockpitGreen1') 

##%%## -GG1 -Grin n Grim Test Room ***
class GG1(Scene):
		
	###SetUp Conditions 
	def setup(self):
	
		_S = self
		
		###Loads Player and Object Sprites
		self.cursor = SpriteNode('iob:arrow_down_c_32')
		self.ripple = SpriteNode('shp:wavering')
		
		self.button = SpriteNode('plc:Selector')
		self.button.on = True
		
		self.effect_node = EffectNode(parent=self)
		self.effect_node.crop_rect = self.bounds
		self.effect_node.effects_enabled = False
		
		self.game_node = Node(parent=self.effect_node)
		self.expl = SpriteNode('shp:Explosion03')
		self.expl.scale = 0.25
		
		self.SetActivePlayer( grim )
		
		self.Menu()
	
	def update(self):
		
		for k,player in enumerate(Player.GetAll()):
			player.Update()
			
		for k,bullets in enumerate(bullet.GetAll()):
			bullets.Update(self)
			
				
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
			self.GetActivePlayer().MoveBegin( touch )
			
	###TOUCH_WHILE									
	def touch_moved(self, touch):
		self.cursor.position = touch.location
		self.GetActivePlayer().MoveWhile( touch )

	###TOUCH_ENDED
	def touch_ended(self,touch):
		self.cursor.remove_from_parent()
		###Interactive_Cursor
		self.target = touch.location
		self.ripple.position = self.target
		self.add_child(self.ripple)
		
		self.GetActivePlayer().MoveEnded( touch )
					
	###Start	
	def GameStart(self):		
	
		###Background
		self.background_color = 'blue'
		
		
		self.grim = SpriteNode('iob:alert_24')
		self.grin =SpriteNode('iob:alert_24')
		
		self.add_child( self.grim )
		self.add_child( self.grin )
		
		###Buttons And Switches
		self.button.position = self.size/2
		self.add_child(self.button)
	
		LoadLevel(self,level1 )
	
	def Button_Press(self,button):
		
		sound.play_effect('arcade:Hit_3')
		
		if self.button.on == False:
			self.button.on = True
			self.background_color = 'orange'
			
		elif self.button.on == True:
			self.button.on = False
			self.background_color = 'purple'
			
			
	def GetActivePlayer(self):
		return self.ActivePlayer
		
	def SetActivePlayer( self, ply ):
		self.ActivePlayer = ply
		
	def SwapActivePlayer(self):
		if self.ActivePlayer == grin:
			self.SetActivePlayer( grim )
		else:
			self.SetActivePlayer( grin )
			
run(GG1(), LANDSCAPE)
