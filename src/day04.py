#
def add(a):
    try:
        print(10 + a)
    except Exception as err:
        print('错误信息', err)
    finally:
        print('最终都会执行的')


add(23)
add('23')
