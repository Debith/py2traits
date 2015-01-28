#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
from pytraits import extendable


# We declare a class here we want to expand with new traits.
# The class contains one class variable and one instance variable.
@extendable
class ExampleClass(object):
    VALUE = 'class member'

    def __init__(self):
        self._value = 'instance member'


# Functions with 'self' as a first parameter will be added as
# new methods. They can access all the variables of the class instance.
def new_method(self):
    return self._value


# Functions with 'cls' as a first parameter will be added as
# new class methods. They can access class variables of the class.
def new_class_function(cls):
    return cls.VALUE


# Functions without 'self' or 'cls' parameter will be normal static
# methods.
def new_static_function():
    return 'static'


# Lets bind these functions to our class
ExampleClass.add_traits(new_method, new_class_function, new_static_function)


# Here we demonstrate new functions work inside the class
assert ExampleClass().new_method() == 'instance member'
assert ExampleClass.new_class_function() == 'class member'
assert ExampleClass.new_static_function() == 'static'
