
pHit = sensor_right
pMiss = 1 - sensor_right

pExact = p_move
pOvershoot = pUndershoot = (1.0 - p_move)/2.

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
      s = pExact * p[y][(x-U[1]) % len(p[y])]
      s = s + pOvershoot * p[y][(x-U[1]-1) % len(p[y])]
      s = s + pUndershoot * p[y][(x-U[1]+1) % len(p[y])]
      r.append(s)
    q.append(r)
  return q

for m in range(len(motions)):
  p = move(p, motions[m])
  p = sense(p, measurements[m])

def show(p):
  for i in range(len(p)):
    print p[i]


