Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help(*args, **kwds)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    help(*args, **kwds)
NameError: name 'args' is not defined
>>> help(*args)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    help(*args)
NameError: name 'args' is not defined
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> print ("Hello")
Hello
>>> print ("Hello World!")
Hello World!
>>> 