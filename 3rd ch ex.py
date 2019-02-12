def collatz(number):
    global result
    if number % 2 == 0:
        print(str(number // 2))
        result = number // 2
        return result
    elif number % 2 == 1:
        print(str(3 * number + 1))
        result = 3 * number + 1
        return result

print('Enter value:')
while True:
    try:
        number = int(input())
    except ValueError:
        print('The value must be an integer!')
        continue
    collatz(number)
    if result == 1:
        break


###
1.it makes the program easy to read and reduce the duplicate code.
2. the code in a function excute when the function is called,not when the funciton is defiened.
3. def statement
4. a function consists of def statement and the code in its def statement.anda function call is when the program excutes
5. when a function is called there is one global scope and a local scope.
6. when the function calls returns the local scope variables is destroyed.
7. a return value is a function call evaluates to.
8. none value
9.
10. None is None Type
11. import a module
12.
13. correct the line of the code in a try clause.
