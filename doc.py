#装饰器。实现某部分代码的重用，整合另外一个函数，实现更加丰富的功能。
def d(fp):
    def _d(*arg, **karg):
        print("do sth before fp..") 
        r= fp(*arg, **karg)
        print ("do sth after fp..")
        return r
    return _d
 
@d
def f():
    print ("call f")
#上面使用@d来表示装饰器和下面是一个意思，表示将下面的函数当做参数调用@后面的函数。
#f = d(f)       
f()#调用f，此时的f不是定义的函数f。而是经过d函数以后的f。就是f = d(f) 中的新量f。