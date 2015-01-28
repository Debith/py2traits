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
# to contain property 'trait_property', thus it won't work as a stand-alone object.
class ExampleTrait(object):
    @property
    def trait_property(self):
        return self._value


# FIXME: We are not yet supporting of cherry-picking property from the class.
#        It is possible to add properties by adding whole class as a trait.
#        This is because property does not know what is the name of the
#        variable it is assigned to.
#        See from except block how things work at the moment.
try:
    # TODO: working cherry-pick
    raise NotImplementedError('')
except NotImplementedError:
    ExampleClass.add_traits(ExampleTrait)


    # Here are the proofs that new method works as part of new class. Also we show
    # that there is no inheritance done for ExampleClass.
    assert hasattr(ExampleClass, 'trait_property'), "Failed to compose property to class!"
    assert ExampleClass.__bases__ == (object, ), "Inheritance has occurred!"
    assert ExampleClass().trait_property == 42, "Cherry-picked method not working properly in new class!"

