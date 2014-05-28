#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
from pytraits import add_traits


class ExampleClass(object):
    pass


class ExampleTrait(object):
    def trait_method(self):
        return 42


add_traits(ExampleClass, ExampleTrait.trait_method)


assert hasattr(ExampleClass, 'trait_method'), "failed composition"
assert not issubclass(ExampleClass, ExampleTrait)
assert ExampleClass().trait_method() == 42, "composition incomplete"
