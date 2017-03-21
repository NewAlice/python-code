import os
import sys

path=sys.argv[1]

for path, dirs, files in os.walk(path):
  print(path)
  print()
  for file in files:
    print(file)

print("all done!")