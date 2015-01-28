#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
from pytraits import extendable


# Let's start by creating a simple class with some values. It contains
# one class variable and one private member. Composed methods will have
# access to all these variables.
@extendable
class ExampleClass(object):
    VALUE = 24

    def __init__(self):
        self._value = 42


# Then we create class, which will act as a Trait. It relies target class to
# contain some state in order to work. This example shows that each type of
# method can be composed to target class and that they will work as if they
# were written there in the first place.
class ExampleTrait(object):
    @classmethod
    def class_method(cls):
        return cls.VALUE

    @staticmethod
    def static_method():
        return 42

    def instance_method(self):
        return self._value

    @property
    def value(self):
        return self._value


# Here we combine instance of ExampleTrait into ExampleClass, which will result
# Example class to contain all ExampleTrait classes method, in this case
# just trait_method.
ExampleClass.add_traits(ExampleTrait())


# Here are the proofs that new method works as part of new class. Also we show
# that there is no inheritance done for ExampleClass.
assert ExampleClass.__bases__ == (object, ), "Inheritance has occurred!"
assert ExampleClass.static_method() == 42, "Class composition fails with static method!"
assert ExampleClass.class_method() == 24, "Class composition fails with class method!"
assert ExampleClass().instance_method() == 42, "Class composition fails with instance method!"
assert ExampleClass().value == 42, "Class composition fails with property!"
