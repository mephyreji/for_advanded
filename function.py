#block of code usinging for specfic task
#def function_name()
#block of code
#def function_name(para1,para2)
#block of code
#def function_name(arg1,arg2)
#
#def fun():
  #  a=10
 #   b=20
#    c=a+b
 #   print(c)
#fun()
#argument and parameter
#def fun(a,b):
    #c=a+b
    #print(c)
#fun(10,20)
#return
#def fun(a,b):
    #c=a+b
    #return c
#res=fun(10,20)
#t=100
#print(res=t)
#ARGUMENT TYPES
def fun(a,b):
    print(a)
    print(b)

fun(10,20)
#arbitary argument=to get the balance in tuple form,space alotationg
def fun(a,*b):
    print(a)
    print(b)

fun(10,20,5,6,4)
a=(1,2,3)
print(type(a))
#arbatiory key
def fun(a,**b):
    print(a)
    print(b)

fun(a=10,b=20,c=5,d=3)
#normal arbatory(default)
def fun(a,b=2):
    print(a)
    print(b)

fun(10,)

#scope=accessibility
#two type:global scope and local variable
a=10#gobal
def fun():
    global b
    b=2
    print(a)
    print(a)
print(a)
print(b)
fun(10,20,5,6,4)
print(b)
