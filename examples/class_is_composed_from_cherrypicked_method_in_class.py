#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
from pytraits import add_traits


# Let's start by creating a super simple class without any methods. Ok, we do add
# constructor there, but that is just for showing that our composition will really
# work.
class ExampleClass(object):
    def __init__(self):
        self._variable = 42


# Then we create a class which contains single method that will be transferred 
# as a part of the class above.
class ContainerClass(object):
    def trait_method(self):
        return self._variable


# Then, we do the actual composition, where we add 'trait_method' directly
# into ExampleClass.
add_traits(ExampleClass, ContainerClass.trait_method)


assert hasattr(ExampleClass, 'trait_method'), "Failed to compose class trait into class!"
assert ExampleClass().trait_method() == 42, "ClassTrait to class is not working properly"
