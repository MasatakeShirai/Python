space = 4

if space == 4:
    print('inside a block')
    print('inside a block')

    if 2*space == 8:
        print('inside a nested block')
        print('inside a nested block')

else:
    print('inside another block')
    print('inside another block')
    
print('outside the blockes')

for i in range(3):
    print(i)

for i in [0,2,4]:
    print(i)