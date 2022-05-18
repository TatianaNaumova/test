import sys

if __name__ == "__main__":
  n = int(sys.argv[1])
  m = int(sys.argv[2])

  arr = [x for x in range(1, n + 1)]
  
  path = ""
  index_first = 0
  index_last = m - 1
  
  while True:
    if arr[0] == arr[index_last]:
      print(path + str(arr[index_first]))
      break
    path += str(arr[index_first])
    index_first = (index_first + m - 1) % n
    index_last = (index_first + m - 1) % n 
