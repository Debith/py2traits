#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
from pytraits import add_traits


class ExampleClass(object):
    def __init__(self):
        self._value = "instance method"


class ExampleTrait(object):        
    def trait_method(self):
        return self._value


# Here we have an instance of our class which we are going to extend by
# cherry-picking single method from the class and as it as a member of
# our instance.
example_instance = ExampleClass()
add_traits(example_instance, ExampleTrait.trait_method)


# Main requirement for extending instances is that the class should be 
# untouched and only the given instance gets extended.
assert hasattr(example_instance, 'trait_method'), "Method must be found from the instance!"
assert not hasattr(ExampleClass, 'trait_method'), "Method must not found from the class!"
assert example_instance.trait_method() == 'instance method', "Method should be part of new instance"
