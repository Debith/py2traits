#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
from pytraits import extendable


# Let's start by creating a super simple class without any methods. Ok, we do add
# constructor there, but that is just for showing that our composition will really
# work.
@extendable
class ExampleClass(object):
    def __init__(self):
        self._value = 42


# Then we create a class which contains single method that will be transferred 
# as a part of the class above. Note that ExampleTrait requires target object
# to contain attribute '_value', thus it won't work as a stand-alone object.
class ExampleTrait(object):
    def trait_method(self):
        return self._value


# Compose an instance with other instance.
example_instance = ExampleClass()
my_trait_instance = ExampleTrait()
example_instance.add_traits(my_trait_instance.trait_method)


# Main requirement for extending instances is that the class should be 
# untouched and only the given instance gets extended.
assert hasattr(example_instance, 'trait_method'), "Method must be found from the instance"
assert not hasattr(ExampleClass, 'trait_method'), "Method must not found from the class!"
assert not issubclass(ExampleClass, ExampleTrait)
assert example_instance.trait_method() == 42, "composition incomplete"