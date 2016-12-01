def Magnitude(point1,point2):
	a, b = point1
	x, y = point2	
	d = ma.sqrt((x-a)**2+(y-b)**2)		
	return d
	
def New_Angle(position,target):
	x,y = target
	a,b = position							
	if x - a == 0:
		theta = ma.pi/2
	else:
		v = (y-b)/(x-a)
		theta = abs(ma.atan(v))

	if x-a > 0 and y-b > 0:
		newtheta = theta
	elif x-a < 0 and y-b > 0:
		newtheta = ma.pi - theta
	elif y-b < 0 and x-a > 0:
		newtheta = 2*ma.pi - theta
	elif x-a < 0 and y-b < 0:
		newtheta = ma.pi + theta
	return newtheta