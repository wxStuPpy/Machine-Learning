def outer(func):
    def inner():
        print('begin')
        func()
        print('end')
    return inner

@outer
def sleep():
    print('sleep')

sleep()