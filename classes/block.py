from scene import SpriteNode

Blocks = []

colors = {'a':'pzl:Gray3','b':'pzl:Gray2'}

class Block():
	def __init__(self,block_type, *args, **kwargs):
		img = colors.get(block_type,'pzl:Blue3')
		self.spirit_node = SpriteNode(img,*args,**kwargs)
		self.block_type = block_type
		Blocks.append(self)
		
	def Remove( self ):
		Blocks.remove( self )
		self.spirit_node.remove_from_parent()
