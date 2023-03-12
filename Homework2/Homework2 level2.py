numb = 7
n = numb -2
w = n*2-1
ar  = [ ]

for y in range(w):
   ar.append([])
   for x in range(w):
       d = n - abs(x+1-n) - abs(y+1-n)
       ar[y].append( "*" if d > 0 else " ")

for l in ar:
    print(*l,sep='')