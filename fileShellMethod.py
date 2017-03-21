import os
import shutil
from os import path

def main():
  if path.exists("file1.txt"):
    src = path.realpath("file1.txt")
  else:
    src="no file with this name"
  location,filename = path.split(src)
  print(location)
  print(filename)
  print(src)
  print("making copy of file")
  dst=src+".bak"
  shutil.copy(src,dst)
  shutil.copystat(src,dst)
  root_dir,tail = path.split(src)
  shutil.make_archive("archive","zip",root_dir)
  
main()