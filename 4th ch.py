''''z = ['apples', 'bananas', 'tofu', 'cats']
def function(x):
    x.insert(-1, ('and ' + x[-1]))
    del x[-1]
    numbers = len(x)
    spam = x[0]
    for i in range(1,numbers):
        spam = spam + ', ' + x[i]
    print(spam)

function(z)'''

###
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

newString = ''

for i in range(len(grid)):
    newString += str(grid[i][0])

newString1 = '\n'
for i in range(len(grid)):
    newString1 += str(grid[i][1])

newString2 = '\n'
for i in range(len(grid)):
    newString2 += str(grid[i][2])

newString3 = '\n'
for i in range(len(grid)):
    newString3 += str(grid[i][3])

newString4 = '\n'
for i in range(len(grid)):
    newString4 += str(grid[i][4])

newString5 = '\n'
for i in range(len(grid)):
    newString5 += str(grid[i][5])

print(newString+newString1+newString2+newString3+newString4+newString5)

1.  empty list value which has no value
2.
3.
4. negative indexs
5.['a','b']
6. 1
7.3.14,11,'cat',T,99
8.3.14,11,'cat', T
9.
10.append() will add values only to the end of a list, insert() can add them anywhere in the list.
11. del statement and remove()
12.
13.
14.(42,)
15. list(),tuple()
16.
17.

