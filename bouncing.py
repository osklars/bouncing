import math
import random
#import pygame
#modules for convenience
#without variable access
def bcolliding(s1,s2,r1,r2):
	"Decides whether ball at coordinates s1 and radius r1 and ball 2 respectively intersect"
	return (s1[0]-s2[0])**2+(s1[1]-s2[1])**2<=(r1+r2)**2
def xcoll(si,ri):
	return not ri<si[0]<xmax-ri
def ycoll(si,ri):
	return not ri<si[1]<ymax-ri
def wcolliding(si,ri):
	"Decides whether ball at coordinates si and radius ri intersects with edges of playground"
	return xcoll(si,ri) or ycoll(si,ri)
#with variable access
def step(i):
	for j in range(2):
		s[i][j]+=v[i][j]
def back(i):
	for j in range(2):
		s[i][j]-=v[i][j]
def bounce(i,j):
	back(i)
	back(j)
	ds=[s[i][0]-s[j][0],s[i][1]-s[j][1]]
	normal=[ds[0]/(ds[0]**2+ds[1]**2),ds[1]/((ds[0]**2+ds[1]**2))]
	vold=[v[i],v[j]]
	dv=[v[j][0]-v[i][0],v[j][1]-v[i][1]]
	vn=dv[0]*normal[0]+dv[1]*normal[1]
	vin=2*vn/(1+m[i]/m[j])
	vjn=(1-m[i]/m[j])*vn/(1+m[i]/m[j])
	v[i]=[vold[0][0]+vin*normal[0],vold[0][1]+vin*normal[1]
	v[j]=[vold[0]-vn[0]*normal[0]+vjn*normal[0],vold[1]-vn[1]*normal[1]+vjn*normal[1]]
	step(i,j)
def bigbounce(ind):
	print 'vafan gör jag nu?!'
#playground variables
xmax=400
ymax=250
#ball variables
n=3		#number of balls
r=[]	#radii
m=[]	#masses
s=[]	#coordinates
v=[]	#velocities
rmax=60
vmax=4	#maximum initial speed
#initaion of ball variables
for i in range(n):
	r.append(random.random()*rmax)
	m.append(random.random())
	v.append([random.random()*vmax, random.random()*vmax])
for i in range(n):
	loop=True
	while loop:
		x=random.random()*xmax
		y=random.random()*ymax
		if not wcolliding([x,y], r[i]):
			if len(s)==0:
				loop=False
			else:
				for j in range(len(s)):
					if not bcolliding([x,y], s[j], r[i], r[j]):
						loop=False
					else:
						print('retry')
	s.append([x,y])
#framegame variables
ft=0.1
fps=100
#framegame
loop=True
print(s)
print(v)
while loop:
	for i in range(n):
		step(i)
	wcs=[]
	for i in range(n):
		wcs.append([xcoll(s[i],r[i]) or ycoll(s[i],r[i])])
	bcs=[]
	for i in range(n):
		bci=[]
		for j in range(n):
			bci.append(bcolliding(s[i],s[j],r[i],r[j]))
		bcs.append(bci)
	for i in range(n):
		if wcs[i] and bcs[i].count(True)==0:
			back(i)
			if xcoll(s[i],r[i]):
				v[i][0]=-v[i][0]
			if ycoll(s[i],r[i]):
				v[i][1]=-v[i][1]
			step(i)
		if not wcs[i] and bcs[i].count(True)==1:
			j=bcs[i].index(True)
			bounce(i,j)	
		else if wcs[i]+bcs[i].count(True)>1: 
			bigbounce()



	loop=False

print(s)