#%% [markdown]
# In Python, null or no value or empty is referred as None. It is a built-in constant object of NoneType and we cannot create custom None object or variables. This type is a singleton which always return a same object. 
#
# None is place holder variable that can be used later.  There is difference between variable defined with None and variable not define at all. If simply type var1 well through a exception  "name 'var1' is not defined". If assign None to var1 then it will not give any result  as well as no exception.   
## None is an Object
#
# None is not a basic type like digits or constant like 1 or true. It a object of a class NoneType.
#%%
type(None)
#%% [markdown]
## None is Singletone
#
# we can check uniqueness of object by using identity function id(). This is an in-build function accept object as a parameter and return identity of a object. This is an integer which is unique for the given object and remain constant during its lifetime.
#%%
a= None
b= None
print('a reference id : '+str(id(a)))
print('b reference id : '+str(id(b)))
print('None reference id : '+str(id(None)))

#%% [markdown]
# Here you can see all the identity is same. which means all the above object refers to same memory location. Each time when we refer the None return a same object.
## Compare variable is None
# There are several ways to check if a variable is None. 
#
### Using is keyword
#%%
var1 = None
if var1 is None:
    print('True')
else: print('False')
### Using boolean cast
#%%
var1 = None
if var1 :
    print('True')
else: print('False')
#%% [markdown]
#The value is return as false. This because the None is convert to Boolean type False.
### Using == Syntax
#%%
var1 = None
if var1 == None:
    print('True')
#%% [markdown]
# Comparisons to singletons like None should always be done with 'is' or 'is not', never the equality operators. where __eq__() method opens is open for overwrite. 
#%%
class MyClass:
    def __eq__(self, my_object):
        return True

my_class = MyClass()
 
if my_class is None:
    print('my_class is None, using the is keyword')
else:
    print('my_class is not None, using the is keyword')
 
if my_class == None:
    print('my_class is None, using the == syntax')
else:
    print('my_class is not None, using the == syntax')  

#%% [markdown]
# Using None as a boolean
#%%
print(bool(None))
print(not None)
print(bool([]))
print(not [])
#%%
class MyFalsey(object):
     def __bool__(self):
         return False

f = MyFalsey()
print(bool(f))



#%%
a =[]
b=[None]

if(a is b):
    print('True')
else: print('False')

if(a == b):
    print('True')
else: print('False')

print(len(a))
print(len(b))

#%% [markdown]
# best practice to comparisons to singletons like None should always be done with 'is' or 'is not'.