import numpy as np
from matplotlib import pyplot as plt

origin = (0, 0)
radius = 2
intersection = np.array([0.9001, 1.792])
radius_var = 15/float(4)
point = (2, 3)
centre = (17/float(4), 0)
A = np.array([-17/float(4),17/float(6)])

len = 10
lam_1 = np.linspace(-10,1,len)
x_A = np.zeros((2,len))

for i in range(len):
	temp_1 = centre + lam_1[i]*(A - centre)
	x_A[:,i] = temp_1.T
	
circle1 = plt.Circle(origin, radius, color='r', fill=False)
circle2 = plt.Circle(centre, radius_var, color='k', fill=False)

fig,ax = plt.subplots()
plt.axis('equal')
	
ax.set_xlim(-4, 10)
ax.set_ylim(-4, 4)
ax.add_artist(circle1)
ax.add_artist(circle2)

plt.plot(point[0], point[1], 'o')
plt.plot(centre[0], centre[1], 'o')
plt.plot(origin[0], origin[1], 'o')
plt.plot(0.9001, 1.792, 'o')
plt.plot((centre[0], intersection[0]), (centre[1], intersection[1]))
plt.plot((origin[0], intersection[0]), (origin[1], intersection[1]))
plt.plot((origin[0], centre[0]), (origin[1], centre[1]))

plt.text(2, -0.4, 'r1 + r2')
plt.text(0, -0.4, 'O')
plt.text(17/float(4), -0.4, 'C')
plt.text(2, 3.2, 'P (a,b)')
plt.text(0.9001, 1.792 + 0.4, 'A')

plt.grid()
plt.show()
fig.savefig('Locus.png')

fig = plt.figure()
plt.axis('equal')
circle_1 = circle1 = plt.Circle(origin, radius, color='r', fill=False)
circle_2 = plt.Circle(centre, radius_var, color='k', fill=False)
ax = plt.gca()	
ax.set_xlim(-4, 10)
ax.set_ylim(-4, 4)
ax.add_artist(circle_1)
ax.add_artist(circle_2)

plt.plot(point[0], point[1], 'o')
plt.plot(centre[0], centre[1], 'o')
plt.plot(origin[0], origin[1], 'o')
plt.plot(0.9001, 1.792, 'o')
plt.plot((centre[0], intersection[0]), (centre[1], intersection[1]))
plt.plot((origin[0], intersection[0]), (origin[1], intersection[1]))
plt.plot((origin[0], centre[0]), (origin[1], centre[1]))
plt.plot(x_A[0,:],x_A[1,:],label = '$Locus of centre$',color='g')

plt.text(2, -0.4, 'r1 + r2')
plt.text(0, -0.4, 'O')
plt.text(17/float(4), -0.4, 'C')
plt.text(2, 3.2, 'P (a,b)')
plt.text(0.9001, 1.792 + 0.4, 'A')

plt.grid()
plt.show()
fig.savefig('Locus_2.png')
