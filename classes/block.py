Blocks = []

colors = {'a':'pzl:Gray3','b':'pzl:Gray2'}

class Block(SpriteNode):
	def __init__(self,block_type, *args, **kwargs):
		img = colors.get(block_type,'pzl:Blue3')
		SpriteNode.__init__(self,img,*args,**kwargs)
		self.block_type = block_type
		Blocks.append(self)
		
	def Remove( self )
		Blocks.remove( self )
		self.spirit_node.remove_from_parent()