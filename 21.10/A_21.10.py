print('---A---')

liczby = [20,40,50,30,10]


print(liczby[-1])
print(liczby[0])

print((max(liczby)) - (min(liczby)))

liczby.sort()
print(liczby)

print('---B---')

print(liczby[-2] - liczby[1])

print('---C---')

for us in liczby:
    print(f'oblicz = {liczby*2}')
    