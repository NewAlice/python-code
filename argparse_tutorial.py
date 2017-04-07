import argparse
'''
python argparse_tutorial.py
python argparse_tutorial.py -h
python argparse_tutorial.py 4 5 add
Two types argsments are supported:
position argsments
optional argment
To make argument optional just add -- in front of argument name.
python argparse_tutorial.py 4 5
python argparse_tutorial.py --number1 4 --operation add --number2 5
python argparse_tutorial.py -h
python argparse_tutorial.py --number1 4 --number2 5
'''
if __name__== "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--number1",help="first numer")
  parser.add_argument("--number2",help="second numer")
  parser.add_argument("--operation",help="operation",\
                         choices=["add","substract","multiply"])
  
  args = parser.parse_args()
  print(args.number1)
  print(args.number2)
  print(args.operation)
  
  n1=int(args.number1)
  n2=int(args.number2)
  result = None
  if args.operation == "add":
      result = n1+n2
  elif args.operation == "substract":
      result = n1-n2
  elif args.operation == "multiply":
      result = n1*n2
  else:
      print("unsupported operation")
	  
  print("result: ", result)