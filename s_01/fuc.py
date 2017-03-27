# Author:zfCode

# def func(name):
#     print(name)
# func("ZF")

# def func(name, name2):
#     print(
#         '''
#         name1:{0}
#         name2:{1}
#         '''.format(name, name2)
#     )
# func("ZF", " CYT")

# def func(name="ZF", *args):
#     print(name)
#     print(args.index("CYT2"))
# 元组  不方便使用
# func()
# func("CYT")

# 接收字典参数
# def func(**kwargs):
#     print(kwargs)
#     print(kwargs["name1"])
#     print(kwargs["name2"])
# func(name1="CYT", name2="CYT2")

# 递归
# def func(n):
#     print(n)
#     if int(n/2)==0:
#         return n
#     return func(int(n/2))
#
# func(10)

# 匿名函数
# calc = lambda x: x * x
# print(calc(5))

# map与匿名函数结合
# res = map(lambda x: x * x, range(11))
# for i in res:
#     print(i)

# 嵌套函数
# def func():
#     print("func")
#     def func_1():
#         print("func_1")
#     return func_1
# fun=func()
# print("------")
# fun()

# 生成器
# g = (x * x for x in range(10))
# print(g.__next__())
# print(g.__next__())
#
# for i in g:
#     print(i)

# 斐波那契数列
def fun(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return "done"


f = fun(10)


# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# while True:
#     try:
#         x = next(f)
#         print('f:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break


# 装饰器
def login(func):
    def inner(*args, **kwargs):
        print("====打印参数===")
        for a in args:
            print(a)
        for k in kwargs:
            print(k, kwargs[k])
        print("这是装饰器的内部逻辑、")
        print("至于怎么写你随意、")
        print("最后调用一下调用你的函数、")
        func(*args, **kwargs)

    return inner


@login  # 这个东西就是装饰器
def home(name, name2, name3):
    print("这是首页")


home("zf", "zf1", name3="zf3")
