"""
 the variable that we associate with the * becomes an iterable

"""


def myfunc(*args):
    print(f"[myfunc] type(args): {type(args)}")  # type of args is tuple
    for arg in args:
        print(arg, end='\t')


# myfunc("adnan", 23, True)


def myfunc2(first, *args):
    print(f"[myfunc2]first: {first}")
    for arg in args:
        print(f"{arg}", end='\t')
    print()


# myfunc2('birinci', "adnan", 23, True)
# myfunc()
# myfunc2('birinci deneme')

#################### kwargs ###################


def myF(**kwargs):
    print(f"[myF] type(args): {type(kwargs)}")  # type of args is dict
    for key, value in kwargs.items():
        print(f"{key},{value}")

# myF(name='adnan', lname='kaya')
# myF(name='zenn', lname='kaya', age=22)

def myFun(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 
      
# Now we can use *args or **kwargs to 
# pass arguments to this function :  
"""args = ("adnan", "kaya", "ce") 
myFun(*args) 
  
kwargs = {"arg1" : "adnan", "arg2" : "kaya", "arg3" : "ce"} 
myFun(**kwargs) """


#######################
def myFun(*args,**kwargs): 
    print("args: ", args) 
    print("kwargs: ", kwargs) 
  
  
# Now we can use both *args ,**kwargs 
# to pass arguments to this function : 
# myFun('adnan','kaya','ce',proglang="python",framework="django",myos="linux")

##############################
# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

