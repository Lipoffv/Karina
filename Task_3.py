print('x', 'y', 'z', 'f', sep='\t')
print()
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            f = (not y) & (x | (not z))
            print(x, y, z, f, sep='\t')