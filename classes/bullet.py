from scene import SpriteNode
import math as ma

Bullets = []

class bullet():
	def __init__(self,position,rotation):
		self.position = position
		self.speed = 50
		self.type = 1
		self.theta = rotation
		self.spirit_node = SpriteNode('spc:LaserBlue13')
		#self.spirit_node.size = 0.5
		
		Bullets.append( self )
		#_S.add_child( self.spirit_node )
		
	def GetAll():
		return Bullets
		
	def Remove( self ):
		Bullets.remove( self )
		self.spirit_node.remove_from_parent()
				
		
	def Update( self , _S):
		self.position += (ma.cos(self.theta)*self.speed, ma.sin(self.theta)*self.speed)
		#if self.position >= _S.size or self.position <= (0,0):
		if not _S.game_node.bbox.contains_point(self.position):
			self.Remove()
