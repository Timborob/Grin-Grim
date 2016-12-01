import math as ma

Bullets = []

class bullet(object):
	def __init__(self,position,type,rotation,spirit_node):
		self.position = position
		self.speed = 2000
		self.type = type
		self.theta = rotation
		self.spirit_node = spirit_node or SpriteNode('spc:LaserBlue13')
		
		Bullets.append( self )
		_S.add_child( self.spirit_node )
		
	def Remove( self )
		Bullets.remove( self )
		self.spirit_node.remove_from_parent()
				
		
	def Update( self )
		self.position = self.position += (ma.cos(self.theta)*self.speed, ma.sin(self.theta)*self.speed)
		if self.position >= _SCENE.size of self.position <= (0,0):
			self:Remove()