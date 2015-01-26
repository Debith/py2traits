#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
from pytraits import add_traits


# Let's start by creating a super simple class without any methods. Ok, we do add
# constructor there, but that is just for showing that our composition will really
# work.
class ExampleClass(object):
    def __init__(self):
        self._variable = 42


# Then we create class, which will act as a Trait. It contains some behavior
# that relies on the state of the ExampleClass. 
class ExampleTrait(object):
    custom_value = "class attribute"

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass

    def trait_method(self):
        return self._variable

    @property
    def value(self):
        pass


# Here we combine ExampleTrait into ExampleClass, which will result
# Example class to contain all ExampleTrait classes method, in this case
# just trait_method.
add_traits(ExampleClass, ExampleTrait)


#assert hasattr(ExampleClass, 'trait_method'), "Failed to compose trait method into class!"
assert not issubclass(ExampleClass, ExampleTrait), "Trait composition should do inheritance."
assert ExampleClass().trait_method() == 42, "class method to class composition is not working properly"
