import sys

if __name__ == "__main__": 
  circle_file = sys.argv[1]
  points_file = sys.argv[2]
  circle = open(circle_file, "r")
  lines = circle.readlines()
  x_0, y_0 = map(lambda x: float(x), lines[0].split())
  r = float(lines[1])
  circle.close()
  points = open(points_file, "r")
  lines = points.readlines()
  points_list = []
  for line in lines:
    x, y = line.split()
    points_list.append((float(x), float(y)))
  points.close()

  for point in points_list:
    x = point[0]
    y = point[1]
    if (x - x_0) ** 2 + (y - y_0) ** 2 < r ** 2:
      print(1)
    elif (x - x_0) ** 2 + (y - y_0) ** 2 == r ** 2:
      print(0)
    elif (x - x_0) ** 2 + (y - y_0) ** 2 > r ** 2:
      print(2)  
