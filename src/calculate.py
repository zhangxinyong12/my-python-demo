def add(*args):
    n = 0
    if len(args) > 1:
        for i in args:
            n += i
        return n
    else:
        print('至少需要2个参数')
        return None
