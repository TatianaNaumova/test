import sys
from copy import copy 


def wall_alignment(wall):
  wall_copy = copy(wall)
  wall.sort()
  mediana = 0
  wall_length = len(wall)
  if wall_length % 2 == 0:
    i = wall_length // 2
    mediana = (wall[i] + wall[i - 1]) // 2
  else:
    i = wall_length // 2
    mediana = wall[i]

  wall = wall_copy
  min_steps = 0
  for i in wall:
    min_steps += abs(i - mediana)

  steps_counter = 0
  for i in range(wall_length):
    while wall[i] != mediana:
      if wall[i] < mediana:
        wall[i] += 1
      elif wall[i] > mediana:
        wall[i] -= 1
      steps_counter += 1
  print(steps_counter)

if __name__ == "__main__": 
  filename = sys.argv[1]
  file = open(filename, "r")
  lines = file.readlines()
  wall = []
  for line in lines:
    wall.append(int(line))
  wall_alignment(wall)
