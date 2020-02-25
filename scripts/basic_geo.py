import maya.cmds as cmd
import random
import math

#-------------------------------------------------

def pipe(rad, thick):
	rad = rad - thick*2
	t_name = cmd.polyPipe(h=thick, r=rad, t=thick, sa=200)[0]
	rad = rad - thick/2
	return t_name, rad
	
#--------------------------------------------------

def rpoly(rad, thick):
	rad = rad - thick/2
	ranb = random.randrange(3,5)
	t_name = cmd.polyPipe(h=thick, r=rad, t=thick, sa=ranb)[0]
	rad = rad * math.cos(math.pi/ranb)
	return t_name, rad
	
#-------------------------------------------------

def rdpoly(rad, thick):
	rad = rad - thick/2
	ranb = random.randrange(3,5)
	x_name = cmd.polyPipe(h=thick, r=rad, t=thick, sa=ranb)[0]
	y_name = cmd.duplicate(x_name)
	cmd.rotate(0, 180/ranb, 0, y_name)
	t_name = cmd.polyUnite(x_name, y_name)[0]
	rad = rad * math.cos(math.pi/ranb)
	return t_name, rad
#-------------------------------------------------
	
def star(rad, thick):
	rad = rad - thick/2
	ranc = random.randrange(5,10)
	sa = ranc * 2
	t_name = cmd.polyPipe(h=thick, r=rad, t=thick, sa=sa)[0]
	shape = cmd.listRelatives(t_name, shapes=True)[0]
	radd = random.uniform(-rad/2,-rad/3)
			
	for n in range(sa*2):
		vert_str = shape + '.vtx[%d]' % (2*n)
		x,y,z = cmd.pointPosition(vert_str, w=True)
		ang = math.atan2(x,z)
		mx = math.sin(ang) * radd
		mz = math.cos(ang) * radd
		cmd.polyMoveVertex(vert_str,t=[mx,y,mz])
	rad = rad + radd		
	#rad = rad*math.cos(math.pi/ranc)+radd + (rad -)
	return t_name, rad
