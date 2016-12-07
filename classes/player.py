from classes.bullet import bullet
from util.gg_math import *
import sound
from scene import SpriteNode

Players = []


class Player(SpriteNode):#(self, stamina, position, can. y. gghhffh_move, SpriteNode):
	def __init__(self, stamina, position, can_move, spirit_node):
		self.stamina = stamina
		self.position = position
		self.can_move = can_move
		self.spirit_node = SpriteNode(spirit_node)
		self.spirit_node.anchor_point = (0.5,0.5)
		Players.append( self )
		
	def GetAll():
		return Players
		
	def Remove( self ):
		Players.remove(self)
		self.spirit_node.remove_from_parent()
		
	def SetStamina(self, stamina):
		self.stamina = stamina
		
	def GetStamina(self):
		return self.stamina
		
	def AddStamina(self, delta):
		self.stamina = self.stamina + delta
		
	def SetPosition(self, pos):
		self.position = pos
		
	def GetPosition(self):
		return self.position
		
	def MoveBegin(self, touch):
		newx, newy = New_position(self.position,touch.location,self.stamina+100)
		
		move_action = A.move_to(newx,newy,1.2, TIMING_LINEAR)
		
		self.spirit_node.run_action(move_action)
		self.SetPosition( (newx, newy) )
		
#		if Magnitude(self.position,self.button.position)<30:
#			_S.Button_Press(self.button)
		
		sound.play_effect('game:Spaceship')
		_S.SwapActivePlayer()
		
	def MoveWhile(self, touch):
		theta = New_Angle(self.position,touch.location)			
		self.rotation = ma.pi/2+theta
		
	def MoveEnded(self, touch):
		theta = New_Angle(self.position ,touch.location)
		bullet( self.position, rotation=theta )
		sound.play_effect('arcade:Laser_1')
		
	def Update( self):
		
		for k,bullets in enumerate(bullet.GetAll()):
			if self.spirit_node.bbox.contains_point( bullets.position ):
				self.AddStamina(-10)
				bullets.Remove()
				sound.play_effect('digital:Laser3')
				
				_S.expl.position = pos
				_S.add_child(self.expl)
				_S.Grin_Turn(grin)
				
				self.SetPosition( self.position + (4*ma.cos(bullets.rotation),4*ma.sin(bullets.rotation)) )
				if self.stamina == 0:
					self.spirit_node.remove_from_parent()
					sound.play_effect('arcade:Explosion_2')					
					self.SetPosition( _S.size/2 )
					self.SetStamina( 100 )
					_S.add_child( self.spirit_node )						
					sound.play_effect('arcade:Powerup_1')
		

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
			
