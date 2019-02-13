import numpy as np
import matplotlib.pyplot as plt
import math

A=np.array([2,3])
B=np.array([4,5])

def mid_pt(B,C):
	D=(B+C)/2
	return D

D=mid_pt(A,B)
AB=np.vstack((A,B)).T
d_vec=np.array([-1,1])
m=np.matmul(AB,d_vec)
omat=np.array([[0,1],[-1,0]])

temp1=np.matmul(m,omat.T)

A2=np.matmul(omat,temp1)
B2=np.matmul(A2.T,D)
A1=np.array([-1,4])
B1=-3

A_vec=np.vstack((A1,A2))
B_vec=np.vstack((B1,B2))
X_vec=np.matmul(np.linalg.inv(A_vec),B_vec)

temp_stack=np.vstack((A,X_vec.T)).T
temp3=np.matmul(temp_stack,d_vec)

radius=math.sqrt(np.matmul(temp3,temp3.T))
print("The radius of the circle is:",end="")
print(radius)

c1=float(X_vec[0])
c2=float(X_vec[1])
C=np.array([c1,c2])
p=np.array([3,0])
q=np.array([-12,-3])

len=100
lam_1=np.linspace(-20,1,len)
len1=25
lam_2=np.linspace(-5,1,len1)
lam=np.linspace(0,1,len)

x_AB=np.zeros((2,len))
x_CD=np.zeros((2,len))
x_PQ=np.zeros((2,len1))

for i in range(len):
	temp1=A+lam[i]*(B-A)
	x_AB[:,i]=temp1.T
	temp2=C+lam_1[i]*(D-C)
	x_CD[:,i]=temp2.T

for i in range(len1):
	temp10=p+lam_2[i]*(q)
	x_PQ[:,i]=temp10.T

plt.plot(x_AB[0,:],x_AB[1,:],label='$Chord$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$Line Perpendicular To Chord$')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$Given Line$')

circle1=plt.Circle((c1,c2),radius,color='r',fill=False)
ax=plt.gca()
plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1+0.1),A[1]*(1-0.1),'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1+0.1),B[1]*(1-0.1),'B')
plt.plot(D[0],D[1],'o')
plt.text(D[0]*(1+0.1),D[1]*(1-0.1),'D')
plt.plot(X_vec[0],X_vec[1],'o')
plt.text(X_vec[0]*(1+0.1),X_vec[1]*(1-0.1),'C')

ax.set_xlim((0,13))
ax.set_ylim((-4, 7))
ax.add_artist(circle1)
plt.grid()
plt.legend(loc='best')
plt.show()
