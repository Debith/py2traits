#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

from pytraits import add_traits


class ExampleClass(object):
    def __init__(self):
        self._value = 42


class ExampleTrait(object):
    @property
    def trait_property(self):
        return self._value


my_trait_instance = ExampleTrait()

# FIXME: Cherrypicking from instance is not supported yet. One needs to able to choose
#        the name and also pick up the property properly
try:
    add_traits(ExampleClass, my_trait_instance.__class__.trait_property)
except TypeError:
    add_traits(ExampleClass, my_trait_instance)

    assert hasattr(ExampleClass, 'trait_property'), "failed composition"
    assert not issubclass(ExampleClass, ExampleTrait)
    assert ExampleClass().trait_property == 42, "composition incomplete"
