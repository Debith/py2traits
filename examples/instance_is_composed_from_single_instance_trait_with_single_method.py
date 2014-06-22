#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

from pytraits import add_traits


class ExampleClass(object):
    pass


class ExampleTrait(object):
    def trait_method(self):
        return 42


my_trait_instance = ExampleTrait()
add_traits(ExampleClass, my_trait_instance.trait_method)

assert hasattr(ExampleClass, 'trait_method'), "failed composition"
assert not issubclass(ExampleClass, ExampleTrait)
assert ExampleClass().trait_method() == 42, "composition incomplete"
