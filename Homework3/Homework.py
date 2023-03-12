df = []
filename = 'tekst.txt'
with open(filename, 'r') as f:
    fizz = int(input())
    buzz = int(input())
    number = int(input())
    d = ''
    for i in range(1, number + 1):
        if i % fizz == 0 and i % buzz == 0:
            print(" FB ", end=" ")
            d += ' FB '
        elif i % fizz == 0:
            d += ' F '
            print(" F ", end="")
        elif i % buzz == 0:
            d += ' B '
            print(" B ", end=" ")
        else:
            d += str(i)
        print(i, end=" ")
    print()
    df.append(d)
print(df)
filename2 = 'tekst2.txt'
with open(filename2, 'w') as f1:
    for i in df:
        f1.write(i)







