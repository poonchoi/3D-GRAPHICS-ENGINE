import numpy as np

w, h = 600, 480

point = np.array([1, 1, 100, 1])
cam = np.array([0, 0, 0, 1])
rot = np.array([0, 0, 0])

f = 0.1
px, py = w/1000, h/1000
offx, offy = w/2, h/2

# idk what this is
pix = 12
skew = 0

offset = np.array([
    [1,0,0,offx],
    [0,-1,0,offy],
    [0,0,1,0],
    [0,0,0,1]
])

P = np.array([
    [(f*w)/(2*px),skew,0,0],
    [0,(f*h)/(2*py),0,0],
    [0,0,-1,0],
    [0,0,0,1]
])

C = np.array([
    [1,0,0,-cam[0]],
    [0,1,0,-cam[1]],
    [0,0,1,-cam[2]],
    [0,0,0,1]
])

rx = np.array([
    [1,0,0,0],
    [0,np.cos(rot[0]),-np.sin(rot[0]),0],
    [0,np.sin(rot[0]),np.cos(rot[0]),0],
    [0,0,0,1]
])

ry = np.array([
    [np.cos(rot[1]),0,np.sin(rot[1]),0],
    [0,1,0,0],
    [-np.sin(rot[1]),0,np.cos(rot[1]),0],
    [0,0,0,1]
])

rz = np.array([
    [np.cos(rot[2]),-np.sin(rot[2]),0,0],
    [np.sin(rot[2]),np.cos(rot[2]),0,0],
    [0,0,1,0],
    [0,0,0,1]
])

G = np.array([
    [1,0,0,-point[0]],
    [0,1,0,-point[1]],
    [0,0,1,-point[2]],
    [0,0,0,1]
])

new_point = point @ P @ rx @ ry @ rz @ G 
proj = [None, None]
proj[0] = new_point[0]/new_point[3]
proj[1] = new_point[1]/new_point[3]

print(point)
print(new_point)
print(proj)