#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

from pytraits import add_traits


class ExampleClass(object):
    pass


class ExampleTrait(object):
    @property
    def trait_property(self):
        return 42


my_trait_instance = ExampleTrait()

# FIXME: We are not yet supporting adding property directly from the class.
#        It is possible to add properties by adding whole class as a trait.
#        This is because property does not know what is the name of the
#        variable it is assigned to.
#        See from except block how things work at the moment
try:
    add_traits(ExampleClass, my_trait_instance.trait_property)
except TypeError:
    add_traits(ExampleClass, my_trait_instance)

    assert hasattr(ExampleClass, 'trait_property'), "failed composition"
    assert not issubclass(ExampleClass, ExampleTrait)
    assert ExampleClass().trait_property == 42, "composition incomplete"
