class Block(SpriteNode): 
  def __init__(self,block_type, *args, **kwargs):  img = colors.get(block_type,'pzl:Blue3')  SpriteNode.__init__(self,img,*args,**kwargs)  self.block_type = block_type
