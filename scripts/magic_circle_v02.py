
#maya/scripts/magic_circle_v02.py
# -*- coding: utf-8 -*

'''
max_rad = 10.0
min_rad =0.3
thick = 0.1
h_max =0.0
h_os = 0.0
r_max = 0.0
r_os = 0.0
circle = 1
'''

import maya.cmds as cmd
import random
import math
import basic_geo as bg
reload(bg)


def magic_circle(max_rad, min_rad, thick, h_max, h_os, r_max, r_os, circle):
	
	allg = []
	if circle == True:
		t_name, rad = bg.pipe(max_rad, thick)
		allg.append(t_name)

		h_ran = random.uniform(-100.00,100.00)
		index = len(allg) -1
		cmd.addAttr( longName = 'index', defaultValue = index , attributeType = 'byte')

		h_ran = random.uniform(-100.00,100.00)
		rx_ran = random.uniform(-100.00,100.00)
		ry_ran = random.uniform(-100.00,100.00)
		rz_ran = random.uniform(-100.00,100.00)

		cmd.addAttr( longName = 'h_ran', defaultValue = h_ran )
		cmd.addAttr( longName = 'rx_ran', defaultValue = rx_ran )
		cmd.addAttr( longName = 'ry_ran', defaultValue = ry_ran )
		cmd.addAttr( longName = 'rz_ran', defaultValue = rz_ran )
		

	else :
		rad = max_rad

	
	while rad > min_rad:
		rana = random.randrange(0,4)
		
		if rana == 0:
			t_name, rad = bg.pipe(rad, thick)
	
		if rana == 1:
			t_name, rad = bg.rpoly(rad, thick)
					
		if rana == 2:
			t_name, rad = bg.rdpoly(rad, thick)

		if rana == 3:
			t_name, rad = bg.star(rad, thick)
			
		allg.append(t_name)

		h_ran = random.uniform(-100.00,100.00)
		rx_ran = random.uniform(-100.00,100.00)
		ry_ran = random.uniform(-100.00,100.00)
		rz_ran = random.uniform(-100.00,100.00)

		cmd.addAttr( longName = 'h_ran', defaultValue = h_ran )
		cmd.addAttr( longName = 'rx_ran', defaultValue = rx_ran )
		cmd.addAttr( longName = 'ry_ran', defaultValue = ry_ran )
		cmd.addAttr( longName = 'rz_ran', defaultValue = rz_ran )

		index = len(allg) -1
		cmd.addAttr( longName = 'index', defaultValue = index , attributeType = 'byte')
		
	gname = cmd.group(allg, n = 'magic_circle')	
	count = len(allg)

	cmd.addAttr( longName = 'h_max', defaultValue = h_max )
	cmd.addAttr( longName = 'h_os', defaultValue = h_os )
	cmd.addAttr( longName = 'r_max', defaultValue = r_max )
	cmd.addAttr( longName = 'r_os', defaultValue = r_os )
	cmd.addAttr( longName = 'count', defaultValue = count )

	
	for n in allg:

		atth_name = n + '.translateY'
		exp_h = atth_name + '=' + gname + '.h_max/' + gname + '.count* '+ '(' + gname + '.count -' +  n +'.index - 1) + (('+ n + '.h_ran + 100)/200*'+ gname + '.h_os)'
		cmd.expression(s = exp_h)

		attrx_name = n + '.rotateX'
		exp_rx = attrx_name + '=' + gname + '.r_max/' + gname + '.count* '+ '(' + gname + '.count -' +  n +'.index - 1) + (('+ n + '.rx_ran + 100)/200*'+ gname + '.r_os)'
		cmd.expression(s = exp_rx)

		attrx_name = n + '.rotateY'
		exp_ry = attrx_name + '=' + gname + '.r_max/' + gname + '.count* '+ '(' + gname + '.count -' +  n +'.index - 1) + (('+ n + '.rx_ran + 100)/200*'+ gname + '.r_os)'
		cmd.expression(s = exp_ry)

		attrx_name = n + '.rotateZ'
		exp_rz = attrx_name + '=' + gname + '.r_max/' + gname + '.count* '+ '(' + gname + '.count -' +  n +'.index - 1) + (('+ n + '.rx_ran + 100)/200*'+ gname + '.r_os)'
		cmd.expression(s = exp_rz)

		


