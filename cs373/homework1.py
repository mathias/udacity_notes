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


###### HOMEWORK 1 PROGRAMMING ###########

colors = [['red', 'green', 'green', 'red' , 'red'],
    ['red', 'red', 'green', 'red', 'red'],
    ['red', 'red', 'green', 'green', 'red'],
    ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
  for i in range(len(p)):
    print p[i]

# CODE GOES AFTER

pHit = sensor_right
pMiss = 1 - sensor_right

pExact = p_move
pNoMove = 1 - p_move

p = []

# Initialize the probabilities
total_number_of_cells = 0
for y in range(len(colors)):
  total_number_of_cells += len(colors[y])

for y in range(len(colors)):
  q = []
  for x in range(len(colors[y])):
    q.append( 1. / total_number_of_cells)
  p.append(q)

def sense(p, Z):
  q = []
  for y in range(len(p)):
    r = []
    for x in range(len(p[y])):
      hit = (Z == colors[y][x])
      r.append(p[y][x] * (hit * pHit + (1-hit) * pMiss))
    q.append(r)
  s = 0
  for y in range(len(q)):
    s += sum(q[y])
  z = []
  for y in range(len(q)):
    r = []
    for x in range(len(q[y])):
      r.append(q[y][x] / s)
    z.append(r)
  return z


def move(p, U):
  q = []
  for y in range(len(p)):
    r = []
    for x in range(len(p[y])):
      s = pExact * p[y-U[0]][(x-U[1]) % len(p[y])]
      s = s + pNoMove * p[y][x]
      r.append(s)
    q.append(r)
  return q

for m in range(len(motions)):
  p = move(p, motions[m])
  p = sense(p, measurements[m])

#Your probability array must be printed
#with the following code.

show(p)

# Example 1:
colors = [['green', 'green', 'green'],
          ['green', 'red', 'green'],
          ['green', 'green', 'green']]

measurements = ['red']

motions=[[0,0]]

sensor_right = 1.0
p_move = 1.0

# Paste above code in here

print "p should equal:"
print "[0.0, 0.0, 0.0]"
print "[0.0, 1.0, 0.0]"
print "[0.0, 0.0, 0.0]"

print "p actually equals:"
show(p)

# Example 2:
colors = [['green', 'green', 'green'],
          ['green', 'red', 'red'],
          ['green', 'green', 'green']]

measurements = ['red']

motions=[[0,0]]

sensor_right = 1.0
p_move = 1.0

# Paste above code in here

print "p should equal:"
print "[0.0, 0.0, 0.0]"
print "[0.0, 0.5, 0.5]"
print "[0.0, 0.0, 0.0]"

print "p actually equals:"
show(p)

# Example 3:
colors = [['green', 'green', 'green'],
          ['green', 'red', 'red'],
          ['green', 'green', 'green']]

measurements = ['red']

motions=[[0,0]]

sensor_right = 0.8
p_move = 1.0

# Paste above code in here

print "p should equal:"
print "[0.0666, 0.0666, 0.0666]"
print "[0.0666, 0.2666, 0.2666]"
print "[0.0666, 0.0666, 0.0666]"

print "p actually equals:"
show(p)


# Example 4:
colors = [['green', 'green', 'green'],
          ['green', 'red', 'red'],
          ['green', 'green', 'green']]

measurements = ['red', 'red']

motions=[[0,0], [0,1]]

sensor_right = 0.8
p_move = 1.0

# Paste above code in here

print "p should equal:"
print "[0.0333, 0.0333, 0.0333]"
print "[0.1333, 0.1333, 0.5333]"
print "[0.0333, 0.0333, 0.0333]"

print "p actually equals:"
show(p)

# Example 4:
colors = [['green', 'green', 'green'],
          ['green', 'red', 'red'],
          ['green', 'green', 'green']]

measurements = ['red', 'red']

motions=[[0,0], [0,1]]

sensor_right = 1.0
p_move = 1.0

# Paste above code in here

print "p should equal:"
print "[0.0, 0.0, 0.0]"
print "[0.0, 0.0, 1.0]"
print "[0.0, 0.0, 0.0]"

print "p actually equals:"
show(p)

# Example 5:
colors = [['green', 'green', 'green'],
          ['green', 'red', 'red'],
          ['green', 'green', 'green']]

measurements = ['red', 'red']

motions=[[0,0], [0,1]]

sensor_right = 0.8
p_move = 0.5

# Paste above code in here

print "p should equal:"
print "[0.0289, 0.0289, 0.0289]"
print "[0.0724, 0.0289, 0.4637]"
print "[0.0289, 0.0289, 0.0289]"

print "p actually equals:"
show(p)

