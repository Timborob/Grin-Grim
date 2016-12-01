colors = {'a':'pzl:Gray3','b':'pzl:Gray2'}

level1 = ( ('''aaaaaaaa    '''),
		('''a     aaa     '''), 
		('''a.        aaaa'''),
		('''a aaaaa       a'''),
		('''aaaaaaaaaaaaa a'''))


Levels = []

def LoadLevel( level )

	Blocks = []

	block_w = _S.size.w/(len(level1[1]))
	block_h = _S.size.h/(len(level1))
	
	min_x = block_w/2
	min_y = block_h/2

	for y, line in enumerate(reversed(level1)):
		for x, char in enumerate(line):
			if char == ' ': continue
			pos = Point(x * block_w + min_x, min_y + y * block_h)
			block = Block(char, position=pos, parent=self.game_node)
			block.size = (block_w, block_h)
			self.blocks.append(block)