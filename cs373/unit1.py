p=[]
print p

p=[0.2,0.2,0.2,0.2,0.2]
world = ['green', 'red', 'red', 'green', 'green']

Z = 'red'

pHit = 0.6
pMiss = 0.2


def sense(p, Z):
  q = []
  for i in range(len(p)):
    hit = (Z == world[i])
    q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
  s = sum(q)
  for i in range(len(q)):
    q[i] = (q[i] / s)
  return q

print sense(p,Z)

print sum(sense(p,Z))

# 1.17
# Simpler p
#Program a function that returns a new distribution
#q, shifted to the right by U units. If U=0, q should
#be the same as p.

p=[0, 1, 0, 0, 0]

def move(p, U):
  q = []
  if U == 0:
    q = p
  else:
    for i in range(len(p)):
      q.append(p[(i-U) % len(p)])
  return q

# 1.21 Inexact Motion
#Modify the move function to accommodate the added
#probabilities of overshooting or undershooting
#the intended destination.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

print move(p, 1)

# 1.23

#Write code that makes the robot move twice and then prints
#out the resulting distribution, starting with the initial
#distribution p = [0, 1, 0, 0, 0]

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

p = move(p, 1)
p = move(p, 1)
print p

# 1.24 Move 1000 times

for i in range(1000):
  p = move(p,1)

print p

# 1.25 Sense after move
#Given the list motions=[1,1] which means the robot
#moves right and then right again, compute the posterior
#distribution if the robot first senses red, then moves
#right one, then senses green, then moves right again,
#starting with a uniform prior distribution.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for m in range(len(motions)):
  p = sense(p, measurements[m])
  p = move(p, motions[m])

print p


