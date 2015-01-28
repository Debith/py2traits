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


# Then, here we do the actual composition, where we cherry-pick 'trait_method' from
# ExampleTrait and add it into ExampleClass.
ExampleClass.add_traits(ExampleTrait.trait_method)


# Here are the proofs that new method works as part of new class. Also we show
# that there is no inheritance done for ExampleClass.
assert hasattr(ExampleClass, 'trait_method'), "Failed to cherry-pick method to class!"
assert ExampleClass.__bases__ == (object, ), "Inheritance has occurred!"
assert ExampleClass().trait_method() == 42, "Cherry-picked method not working properly in new class!"
