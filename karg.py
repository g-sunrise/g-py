def foo(x, y, z, *args, **kargs):
    print x
    print y
    print z
    print args
    print kargs

foo("qwsir", 6, 7, a=1, b=2, c=3)