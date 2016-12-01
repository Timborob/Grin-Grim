import bullet as *
import sound

Players = []

class Player(object):#(self, stamina, position, can. y. gghhffh_move, SpriteNode):
	def __init__(self, stamina, position, can_move, spirit_node):
		self.stamina = stamina
		self.position = position
		self.can_move = can_move
		self.spirit_node = spirit_node
		self.spirit_node.anchor_point = (0.5,0.5)
		Players.append( self )
		
	def Remove( self )
		Players.remove(self)
		
	def SetStamina(self, stamina)
		self.stamina = stamina
		
	def GetStamina(self)
		return self.stamina
		
	def AddStamina(self, delta)
		self.stamina = self.stamina + delta
		
	def SetPosition(self, pos)
		self.position = pos
		
	def GetPosition(self)
		return self.position
		
	def Update( )
		if self.can_move != True:
			return
		
		for k,bullet in Bullets:
			if self.spirit_node.bbox.contains_point( bullet.position ):
				self:AddStamina(-10)
				bullet:Remove()
				sound.play_effect('digital:Laser3')
				
				_S.expl.position = pos
				_S.add_child(self.expl)
				_S.Grin_Turn(grin)
				
				self:SetPosition( self.position + (4*ma.cos(bullet.rotation),4*ma.sin(bullet.rotation)) )
				if self.stamina == 0:
					self.spirit_node.remove_from_parent()
					sound.play_effect('arcade:Explosion_2')					
					self:SetPosition( _S.size/2 )
					self:SetStamina( 100 )
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
			