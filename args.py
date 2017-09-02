#参数传递
def debug(func):
    def wrapper(**kwargs):  # 指定宇宙无敌参数
        print ("[DEBUG]: enter {}()".format(func.__name__))
        print('Prepare and say...')
        return func(*args, **kwargs)
    return wrapper  # 返回

#@debug
def say(**kwargs):
	#print(type(kwargs))
	print(kwargs)
	print(kwargs['k1'])
	print ("hello {}{}!".format(kwargs['k1'],kwargs['k2']))
  
debug(say(k1='3',k2='5'))#此处参数关键字用的什么，接收依然用什么，返回为字典。*args返回为元组，可索引。
#函数调用时也可以这样用。
def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3
 
args = ("two", 3)
test_var_args_call(1, *args)

def test_var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3
 
kwargs = {"arg3": 3, "arg2": "two"}
test_var_args_call(1, **kwargs)