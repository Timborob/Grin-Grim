from scene import *
from _scene import *
import sound
import math as ma
import random

clamp = lambda n, minn, maxn: max(min(maxn, n), minn)

class GG1(Scene):

	_pgwindowsize = (800,600)
	_pgwindowtitle = "Alex's Emulator Test"
	
	_boxa = [200,200]
	_boxp = [100,100]
	_boxc = [1,1,1]
	_boxd = [50,50]
	
	_touch1 = [0,0]
	_touch2 = [0,0]
	_Ismdo = False
	
	def setup( self ):
		self.background_color = 'green'
		pass
		
	def bounce( self ):
		for i in range( 0, 2 ):
			if (self._boxp[i] <= 0 or self._boxp[i] >= (self._pgwindowsize[i] - self._boxd[i] ) ):
				self._boxa[i] = -self._boxa[i]
				self.background_color = Color(self._boxc[0],self._boxc[1],self._boxc[2])
				self._boxc = [random.random(),random.random(),random.random()]
				sound.play_effect( "test.wav" )
	
	def draw(self):
		
		if self._Ismdo:
			stroke_weight( 1 )
			stroke( self._boxc[0], self._boxc[1], self._boxc[1], 1 )
			line( self._touch1[0], self._touch1[1], self._touch2[0], self._touch2[1] )
			stroke_weight( 0 )
		
		else:
			self.bounce()
			self._boxp = [ clamp( self._boxp[0] + self._boxa[0]*self.dt, 0,(self._pgwindowsize[0] - self._boxd[0] ) ) ,  clamp( self._boxp[1] + self._boxa[1]*self.dt ,0,(self._pgwindowsize[1] - self._boxd[1] ) ) ]
			
		fill(self._boxc[0], self._boxc[1], self._boxc[2], a=1.0)
		rect(self._boxp[0], self._boxp[1] , self._boxd[0], self._boxd[1])
		
	
	def touch_began(self,touch):
	
		self._Ismdo = True
	
		print( "Touched at x:"+ str(touch.location.x) + " y:" + str(touch.location.y) )
		self._boxp[0] = touch.location.x
		self._boxp[1] = touch.location.y
		
		self._touch1[0] = touch.location.x
		self._touch1[1] = touch.location.y
	
	def touch_moved(self, touch):
		self._touch2[0] = touch.location.x
		self._touch2[1] = touch.location.y
	
	def touch_ended(self,touch):
	
		self._boxa[0] = touch.location.x - self._touch1[0]
		self._boxa[1] = touch.location.y - self._touch1[1]
		
		self._Ismdo = False



run(GG1(),1,1,True)