import sys

print(sys.platform)

if sys.platform == "win32":
  import ntpath
  pathmodule=ntpath

print(pathmodule)