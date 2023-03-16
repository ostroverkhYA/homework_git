fizz = int(input())
buzz = int(input())
number = int(input())
[print(' FB '  if i % fizz == 0 and i % buzz == 0 else " F " if i % fizz == 0 else " B " if i % buzz == 0 else i) for i in range (1,number + 1)]



