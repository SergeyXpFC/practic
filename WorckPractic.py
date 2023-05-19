def task_1():
    for i in range(101):
        if i%3 == 0 and i%5 == 0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)

def task_2():
    a = [1, 4, 6]
    b = [11, 33, 22]
    c = [a for _, a in sorted(zip(b, a))]
    print(c)

task_2()
